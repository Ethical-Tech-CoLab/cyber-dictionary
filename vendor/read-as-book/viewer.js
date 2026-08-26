// A ready-made full-screen reader built on mountFlipbook: dimmed backdrop,
// title bar, page counter, optional PDF download, prev/next arrows, Escape to
// close, and a body-scroll lock while open.
//
// Import "read-as-book/styles.css" once for the default look; every element
// carries a `rab-*` class you can restyle freely.
import { mountFlipbook } from "./flipbook.js";
function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className)
        node.className = className;
    if (text != null)
        node.textContent = text;
    return node;
}
/**
 * Open the full-screen book reader. Resolves once the page-curl is live.
 */
export async function openBookViewer(options) {
    const host = options.container ?? document.body;
    const total = options.pages.length;
    const root = el("div", `rab-overlay${options.className ? ` ${options.className}` : ""}`);
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.setAttribute("aria-label", `${options.title ?? "Document"} — page view`);
    const chrome = el("div", "rab-chrome");
    chrome.append(el("span", "rab-title", options.title ?? ""));
    const actions = el("div", "rab-actions");
    const counter = el("span", "rab-counter");
    actions.append(counter);
    if (options.pdfUrl) {
        const link = el("a", "rab-btn rab-download", "Download PDF ↗");
        link.href = options.pdfUrl;
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        actions.append(link);
    }
    const closeBtn = el("button", "rab-btn", "Close ✕");
    closeBtn.type = "button";
    closeBtn.setAttribute("aria-label", "Close book view");
    actions.append(closeBtn);
    chrome.append(actions);
    const stage = el("div", "rab-stage");
    const prevBtn = el("button", "rab-arrow rab-arrow-prev", "‹");
    prevBtn.type = "button";
    prevBtn.setAttribute("aria-label", "Previous page");
    const nextBtn = el("button", "rab-arrow rab-arrow-next", "›");
    nextBtn.type = "button";
    nextBtn.setAttribute("aria-label", "Next page");
    const holder = el("div", "rab-book");
    const loading = el("p", "rab-loading", "Opening the book…");
    const stack = el("div", "rab-book-wrap");
    stack.append(holder, loading);
    stage.append(prevBtn, stack, nextBtn);
    const hintText = options.hint ?? "Use the arrows or ← → keys to turn pages · Esc to close";
    const footer = el("p", "rab-hint", hintText);
    root.append(chrome, stage);
    if (hintText)
        root.append(footer);
    host.append(root);
    const setCounter = (page) => {
        counter.textContent = total ? `${Math.min(page + 1, total)} / ${total}` : "";
    };
    setCounter(options.startPage ?? 0);
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    let book = null;
    let closed = false;
    const close = () => {
        if (closed)
            return;
        closed = true;
        document.removeEventListener("keydown", onKey);
        document.body.style.overflow = previousOverflow;
        book?.destroy();
        root.remove();
        options.onClose?.();
    };
    const onKey = (e) => {
        if (e.key === "Escape")
            close();
    };
    document.addEventListener("keydown", onKey);
    closeBtn.addEventListener("click", close);
    try {
        book = await mountFlipbook(holder, {
            pages: options.pages,
            aspect: options.aspect,
            startPage: options.startPage,
            onFlip: (page) => {
                setCounter(page);
                options.onFlip?.(page);
            },
            onReady: () => loading.remove(),
        });
    }
    catch (err) {
        close();
        throw err;
    }
    // The viewer may have been closed while page-flip was still loading.
    if (closed) {
        book.destroy();
        return { close, next: () => { }, prev: () => { } };
    }
    prevBtn.addEventListener("click", () => book?.prev());
    nextBtn.addEventListener("click", () => book?.next());
    return {
        close,
        next: () => book?.next(),
        prev: () => book?.prev(),
    };
}
//# sourceMappingURL=viewer.js.map