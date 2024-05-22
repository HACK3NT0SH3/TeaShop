var screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
var screenHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

if (screenWidth < screenHeight) {
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 2,
        spaceBetween: 20,
        autoplay: {
            delay: 2500,
            disableOnInteraction: true,
        },
        loop: true,
        keyboard: {
            enabled: true,
        }
    
    });
} else {
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 3,
        spaceBetween: 10,
        autoplay: {
            delay: 2500,
            disableOnInteraction: true,
        },
        loop: true,
        keyboard: {
            enabled: true,
        }
    
    });
}
