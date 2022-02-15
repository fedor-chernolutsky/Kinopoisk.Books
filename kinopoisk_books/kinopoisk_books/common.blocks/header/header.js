// JS code for header
window.addEventListener("load", function() {
  function togglesearch() {
    document.querySelector('.header__index-block').classList.toggle('display-none');
    document.querySelector('.header__fresh-block').classList.toggle('display-none');
    document.querySelector('.header__genres-block').classList.toggle('display-none');
    document.querySelector('.header__selections-block').classList.toggle('display-none');
    document.querySelector('.header__saved-block').classList.toggle('display-none');
    document.querySelector('.header__media__block').classList.toggle('display-none');
    document.querySelector('.header__loop-block').classList.toggle('display-none');
    document.querySelector('.header__search-bar-block').classList.toggle('display-none');
    document.querySelector('.header__close-block').classList.toggle('display-none');

    document.querySelector('.header__search-bar-input').value = '';
    document.querySelector('.header__search-bar-input').focus();
  }
  document.querySelector('.header__loop-block').onclick = togglesearch;
  document.querySelector('.header__close-block').onclick = togglesearch;
  document.querySelector('.header__search-bar-input').onblur = togglesearch;
});
