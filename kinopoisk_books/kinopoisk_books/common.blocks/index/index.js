// JS script for index page
window.addEventListener("load", function() {
  document.getElementById('banner').onclick = function(event) {
    let path = event.path || (event.composedPath && event.composedPath());  // cross - browser compatibility
    if (path.includes(document.getElementById('banner__button-group'))) { event.preventDefault(); }
  }
});
