// The page-turning utility itself: a real page-curl over a list of page images.
//
// This is the piece worth reusing. Give it a container and an ordered list of
// image URLs and it sizes the spread to the viewport, lazy-loads page-flip
// (StPageFlip) on first use, wires arrow keys, and rebuilds itself on resize —
// which page-flip cannot do on its own.
//
//   const book = await mountFlipbook(el, { pages, aspect: 0.77 });
//   book.next(); book.prev(); book.destroy();
const DEFAULTS = {
    startPage: 0,
    singlePageBreakpoint: 640,
    chromeHeight: 150,
    chromeWidth: 48,
    maxPageHeight: 1100,
    flippingTime: 700,
    drawShadow: true,
    maxShadowOpacity: 0.4,
    keyboard: true,
};
/**
 * Work out the page size that fits the current viewport, keeping `aspect` and
 * leaving room for chrome. Exported because callers often want to reserve
 * layout space before the book itself is built.
 */
export function fitPageSize(aspect, opts) {
    const chromeH = opts.chromeHeight ?? DEFAULTS.chromeHeight;
    const chromeW = opts.chromeWidth ?? DEFAULTS.chromeWidth;
    const maxH = Math.min(opts.viewportHeight - chromeH, opts.maxPageHeight ?? DEFAULTS.maxPageHeight);
    const maxW = opts.viewportWidth - chromeW;
    let height = Math.max(maxH, 120);
    let width = height * aspect;
    const spreadWidth = opts.single ? width : width * 2;
    if (spreadWidth > maxW) {
        const scale = maxW / spreadWidth;
        width *= scale;
        height *= scale;
    }
    return { width: Math.round(width), height: Math.round(height) };
}
/**
 * Mount a page-turning book of images into `container`.
 *
 * Resolves once the curl is live. The returned handle stays valid across
 * resizes: the instance is rebuilt underneath at the new size, holding the
 * reader's place.
 */
export async function mountFlipbook(container, options) {
    const opt = { ...DEFAULTS, ...options };
    if (!opt.pages.length)
        throw new Error("mountFlipbook: `pages` is empty");
    const mod = (await import("page-flip"));
    const PageFlip = mod.PageFlip;
    let flip = null;
    let page = Math.min(Math.max(opt.startPage, 0), opt.pages.length - 1);
    let destroyed = false;
    let resizeTimer = null;
    const build = () => {
        if (destroyed)
            return;
        const single = opt.singlePageBreakpoint > 0 &&
            window.matchMedia(`(max-width: ${opt.singlePageBreakpoint}px)`).matches;
        const { width, height } = fitPageSize(opt.aspect, {
            single,
            viewportWidth: window.innerWidth,
            viewportHeight: window.innerHeight,
            chromeWidth: opt.chromeWidth,
            chromeHeight: opt.chromeHeight,
            maxPageHeight: opt.maxPageHeight,
        });
        flip = new PageFlip(container, {
            width,
            height,
            size: "fixed",
            showCover: true,
            usePortrait: single,
            maxShadowOpacity: opt.maxShadowOpacity,
            mobileScrollSupport: true,
            flippingTime: opt.flippingTime,
            drawShadow: opt.drawShadow,
        });
        flip.loadFromImages(opt.pages.slice());
        flip.on("flip", (e) => {
            page = e.data;
            opt.onFlip?.(page);
        });
        if (page > 0) {
            try {
                flip.turnToPage(page);
            }
            catch {
                // Older page-flip builds reject a jump before the images decode; the
                // reader simply starts at the cover.
            }
        }
        opt.onReady?.();
    };
    const teardown = () => {
        if (!flip)
            return;
        try {
            flip.destroy();
        }
        catch {
            // page-flip throws if the container was already removed from the DOM.
        }
        flip = null;
        container.innerHTML = "";
    };
    // page-flip has no live re-fit, so a resize means rebuild. Debounced, because
    // a drag-resize fires continuously and each rebuild re-decodes the images.
    const onResize = () => {
        if (resizeTimer)
            clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            teardown();
            build();
        }, 200);
    };
    const onKey = (e) => {
        if (e.key === "ArrowLeft")
            flip?.flipPrev();
        else if (e.key === "ArrowRight")
            flip?.flipNext();
    };
    build();
    window.addEventListener("resize", onResize);
    if (opt.keyboard)
        document.addEventListener("keydown", onKey);
    return {
        next: () => flip?.flipNext(),
        prev: () => flip?.flipPrev(),
        goTo: (n) => flip?.turnToPage(n),
        currentPage: () => page,
        pageCount: () => opt.pages.length,
        destroy: () => {
            if (destroyed)
                return;
            destroyed = true;
            if (resizeTimer)
                clearTimeout(resizeTimer);
            window.removeEventListener("resize", onResize);
            document.removeEventListener("keydown", onKey);
            teardown();
        },
    };
}
//# sourceMappingURL=flipbook.js.map