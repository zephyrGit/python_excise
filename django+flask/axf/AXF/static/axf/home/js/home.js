$(function () {
    var mySwiper = new Swiper ('#topSwiper', {
    // direction: 'vertical',
    loop: true,
    autoplay:2000,

    // 如果需要分页器
    pagination: '.swiper-pagination',

    // 如果需要前进后退按钮
    nextButton: '.swiper-button-next',
    prevButton: '.swiper-button-prev',
  });
    initMustBy();
})
function initMustBy() {
    var mySwiper = new Swiper ('#swiperMenu', {
    slidesPerView: 3,
    paginationClickable: true
  })
}