window.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("tag a")
        .forEach(function(a) {
            tag_name = a.innerHTML;
            a.href = "tag.html?tag=" + encodeURIComponent(tag_name);
        });
});
