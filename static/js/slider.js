window.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('slider');
    const slides = slider.getElementsByClassName('slide');
    const totalSlides = slides.length;
    let currentSlide = 0;
  
    function showSlide(n) {
      if (n < 0) {
        currentSlide = totalSlides - 1;
      } else if (n >= totalSlides) {
        currentSlide = 0;
      } else {
        currentSlide = n;
      }
  
      for (let i = 0; i < totalSlides; i++) {
        slides[i].classList.remove('active');
      }
  
      slides[currentSlide].classList.add('active');
    }
  
    function nextSlide() {
      showSlide(currentSlide + 1);
    }
  
    function startSlider() {
      setInterval(nextSlide, 4000);
    }
  
    startSlider();
  });
  