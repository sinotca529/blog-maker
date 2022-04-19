window.addEventListener("DOMContentLoaded", function() {
    // process tag.
    let re = /(.*tag.html\?tag=)(.*)/;
    document.querySelectorAll("tag a")
        .forEach(function(a) {
            let match = re.exec(a.href);
            a.href = match[1] + encodeURIComponent(match[2])
        });

    // pseudo.js
    document.querySelectorAll(".algorithm")
        .forEach(e => {
            pseudocode.renderElement(e, {lineNumber: true, lineNumberPunc: ' '});
        });

    // viz.js (graphviz)
    document.querySelectorAll(".graphviz")
        .forEach(e => {
            e.innerHTML = Viz(e.innerText);
        });
});
