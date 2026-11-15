/* Shared on every page */
document.documentElement.classList.add('js');
var yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();

/* Fade-ins: each .fade element appears once when it scrolls into view */
var io = new IntersectionObserver(function(entries){
  entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
},{threshold:0.12});
document.querySelectorAll('.fade').forEach(function(el){ io.observe(el); });

/* Header turns solid and the sticky button appears after scrolling */
var header = document.querySelector('header'), sticky = document.getElementById('sticky'), quoteBox = document.getElementById('quote');
var alwaysSolid = header.classList.contains('solid');
function onScroll(){
  if (!alwaysSolid) header.classList.toggle('solid', window.scrollY > 40);
  if (sticky){
    var nearForm = quoteBox ? quoteBox.getBoundingClientRect().top < window.innerHeight : false;
    sticky.classList.toggle('show', window.scrollY > 500 && !nearForm);
  }
}
window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
