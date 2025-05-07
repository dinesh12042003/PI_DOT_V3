document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.slider-dots .dot');
    let currentSlide = 0;
    const slideCount = slides.length;
    let slideInterval;

    // Initialize slider
    function showSlide(index) {
      slides.forEach(slide => slide.classList.remove('active'));
      dots.forEach(dot => dot.classList.remove('active'));
      
      slides[index].classList.add('active');
      dots[index].classList.add('active');
      currentSlide = index;
    }

    // Next slide
    function nextSlide() {
      let newIndex = (currentSlide + 1) % slideCount;
      showSlide(newIndex);
    }

    // Auto-rotate slides every 5 seconds
    function startSlider() {
      slideInterval = setInterval(nextSlide, 5000);
    }

    // Dot navigation
    dots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        clearInterval(slideInterval);
        showSlide(index);
        startSlider();
      });
    });

    // Start the slider
    startSlider();

    // Pause on hover
    const slider = document.querySelector('.hero-slider');
    slider.addEventListener('mouseenter', () => clearInterval(slideInterval));
    slider.addEventListener('mouseleave', startSlider);
  });