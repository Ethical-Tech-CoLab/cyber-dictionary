// read-as-book — a "Read as book" page-turning viewer for any website.
//
//   mountFlipbook(el, { pages, aspect })  — the page-turn utility on its own
//   openBookViewer({ pages, aspect })     — the full-screen reader built on it
//   loadBookManifest(url)                 — read a manifest.json from the CLI
//
// The React component lives at "read-as-book/react"; the default styles at
// "read-as-book/styles.css".
export { mountFlipbook, fitPageSize } from "./flipbook.js";
export { openBookViewer } from "./viewer.js";
/**
 * Fetch a manifest.json produced by the CLI and resolve its page paths against
 * the manifest's own URL, so the result can be handed straight to the viewer.
 */
export async function loadBookManifest(manifestUrl, init) {
    const res = await fetch(manifestUrl, init);
    if (!res.ok) {
        throw new Error(`read-as-book: could not load ${manifestUrl} (${res.status})`);
    }
    const manifest = (await res.json());
    const base = new URL(manifestUrl, globalThis.location?.href ?? "http://localhost/");
    return {
        ...manifest,
        // Manifest paths are web-root relative; the images sit next to the
        // manifest, so resolve each against its directory.
        pages: manifest.pages.map((p) => new URL(p.split("/").pop(), base).toString()),
    };
}
//# sourceMappingURL=index.js.map