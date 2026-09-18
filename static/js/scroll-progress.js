const progressBar = document.querySelector(".scroll-progress-bar");


function updateScrollProgress() {

    const scrollTop = window.scrollY;

    const scrollableHeight =
        document.documentElement.scrollHeight - window.innerHeight;

    const progress =
        scrollableHeight > 0
            ? (scrollTop / scrollableHeight) * 100
            : 0;

    progressBar.style.width = `${progress}%`;
}


window.addEventListener(
    "scroll",
    updateScrollProgress,
    { passive: true }
);

window.addEventListener(
    "resize",
    updateScrollProgress
);


updateScrollProgress();
