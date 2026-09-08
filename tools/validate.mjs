// Everything that has to be true about the data, checked in one place.
//
// Each rule here corresponds to a mistake actually made in this repository:
// a duplicate headword, a term filed under a domain that does not exist, HTML
// tags in a definition that render as literal text, a case study citing a term
// nobody wrote, a reference with no URL. The point of the file is that those
// stop being things someone has to remember.
//
//   node tools/validate.mjs          check the data
//   node tools/validate.mjs --page   also check that index.html's script parses
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const problems = [];
const fail = (m) => problems.push(m);

// The data files are browser scripts that assign to window; give them one.
const sandbox = { window: {} };
vm.createContext(sandbox);
for (const f of ["terms.js", "library.js", "cases.js"]) {
  try {
    vm.runInContext(readFileSync(join(root, f), "utf8"), sandbox, { filename: f });
  } catch (e) {
    fail(`${f} does not parse: ${e.message}`);
  }
}
const { TERMS, DOMAINS, SOURCES, SHELVES, CASES } = sandbox.window;
if (!TERMS || !SOURCES || !CASES) {
  console.error("✗ data did not load\n  " + problems.join("\n  "));
  process.exit(1);
}

// ---- the dictionary ----
const seen = new Map();
for (const t of TERMS) {
  if (!t.t || !t.d || !t.def) fail(`term missing a field: ${JSON.stringify(t).slice(0, 90)}`);
  const key = (t.t || "").toLowerCase();
  if (seen.has(key)) fail(`duplicate headword: "${t.t}"`);
  seen.set(key, t);
  if (!DOMAINS.includes(t.d)) fail(`"${t.t}" is in an undeclared domain: "${t.d}"`);
  // Definitions are HTML-escaped when rendered, so markup shows up literally.
  if (/<[a-z/][^>]*>/i.test(t.def)) fail(`"${t.t}" has HTML in its definition`);
  if (t.def.trim().length < 25) fail(`"${t.t}" has a definition too short to be one`);
  if (!/[.!?]"?$/.test(t.def.trim())) fail(`"${t.t}" definition does not end in a full stop`);
  if (t.s && /(^,)|(,,)|(,\s*$)/.test(t.s)) fail(`"${t.t}" has a malformed synonym list`);
}
for (const d of DOMAINS) {
  if (!TERMS.some((t) => t.d === d)) fail(`domain "${d}" has no terms`);
}

// ---- the library ----
const shelfSeen = new Set();
for (const s of SOURCES) {
  for (const k of ["n", "o", "u", "s", "w", "h", "c"]) {
    if (!s[k]) fail(`library entry "${s.n || "?"}" is missing "${k}"`);
  }
  if (!SHELVES.includes(s.s)) fail(`"${s.n}" is on an undeclared shelf: "${s.s}"`);
  if (!/^https?:\/\//.test(s.u || "")) fail(`"${s.n}" has a non-http url: ${s.u}`);
  if (shelfSeen.has(s.n)) fail(`duplicate library entry: "${s.n}"`);
  shelfSeen.add(s.n);
}
for (const s of SHELVES) {
  if (!SOURCES.some((x) => x.s === s)) fail(`shelf "${s}" is empty`);
}

// ---- the case studies ----
const HEADINGS = ["What happened", "How it worked", "How it was found", "What changed"];
for (const c of CASES) {
  if (!c.title || !c.year) fail(`case "${c.id}" is missing a title or year`);
  const got = c.sections.map((s) => s.heading);
  for (const h of HEADINGS) if (!got.includes(h)) fail(`case "${c.id}" is missing "${h}"`);
  for (const s of c.sections) {
    if (!s.paragraphs.length) fail(`case "${c.id}" has an empty "${s.heading}"`);
  }
  for (const t of c.terms) {
    if (!seen.has(t.toLowerCase())) fail(`case "${c.id}" cites an unknown term: "${t}"`);
  }
  if (c.sources.length < 2) fail(`case "${c.id}" has fewer than two references`);
  for (const s of c.sources) {
    if (!s.title || !s.url) fail(`case "${c.id}" has a reference missing a title or url`);
    // A reference becomes an href; anything but http(s) would execute.
    if (!/^https?:\/\//.test(s.url || "")) fail(`case "${c.id}" has a non-http reference: ${s.url}`);
  }
}

// ---- the page itself, on request ----
if (process.argv.includes("--page")) {
  const html = readFileSync(join(root, "index.html"), "utf8");
  const m = html.match(/<script>\n\(function\(\)\{[\s\S]*?\n\}\)\(\);\n<\/script>/);
  if (!m) fail("index.html: could not find the main script block");
  else {
    try {
      new vm.Script(m[0].replace(/^<script>|<\/script>$/g, ""));
    } catch (e) {
      fail(`index.html script does not parse: ${e.message}`);
    }
  }
}

if (problems.length) {
  console.error(`✗ ${problems.length} problem(s):\n  ` + problems.join("\n  "));
  process.exit(1);
}
console.log(`✓ ${TERMS.length} terms, ${SOURCES.length} sources, ${CASES.length} cases — all valid`);
