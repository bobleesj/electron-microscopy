// Wrap every content image in an anchor pointing to the same image so a click
// opens the raw file in a new tab. Skips images that are already inside an
// anchor (e.g. authored as <a><img></a> in markdown).
(function () {
    function wrapImages() {
        var imgs = document.querySelectorAll('.content img');
        for (var i = 0; i < imgs.length; i++) {
            var img = imgs[i];
            if (img.parentElement && img.parentElement.tagName === 'A') continue;
            var a = document.createElement('a');
            a.href = img.getAttribute('src');
            a.target = '_blank';
            a.rel = 'noopener';
            img.parentNode.insertBefore(a, img);
            a.appendChild(img);
        }
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', wrapImages);
    } else {
        wrapImages();
    }
})();
