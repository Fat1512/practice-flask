window.addEventListener("load", function () {
    const x = document.querySelector(".test");
    x.addEventListener("click", function () {
        fetch("/api/barcode");
    })
})