/* Responsive Navigation Menu */
const menuBtn = document.getElementById("menuBtn");
    const navLinks = document.getElementById("navLinks");

    menuBtn.addEventListener("click", function () {

        navLinks.classList.toggle("active");

    });


    /* Close mobile menu after clicking link */

    document.querySelectorAll(".nav-links a").forEach(function(link) {

        link.addEventListener("click", function() {

            navLinks.classList.remove("active");

        });

    });


    /* Scroll To Top */

    const topBtn = document.getElementById("topBtn");

    window.addEventListener("scroll", function() {

        if (window.scrollY > 500) {

            topBtn.style.display = "flex";

        } else {

            topBtn.style.display = "none";

        }

    });


    topBtn.addEventListener("click", function() {

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    });


    /* Testimonial Auto Slide */

    const testimonialSlides = document.querySelectorAll(".testimonial-slide");
    const testimonialSlider = document.querySelector(".testimonial-slider");
    const testimonialPrev = document.querySelector(".testimonial-prev");
    const testimonialNext = document.querySelector(".testimonial-next");

    if (testimonialSlides.length > 0) {

        let testimonialIndex = 0;
        let testimonialInterval;

        function showTestimonial(index) {

            testimonialSlides.forEach((slide, i) => {
                slide.classList.toggle("active", i === index);
            });
        }

        function startTestimonialInterval() {
            clearInterval(testimonialInterval);
            testimonialInterval = setInterval(function () {
                testimonialIndex = (testimonialIndex + 1) % testimonialSlides.length;
                showTestimonial(testimonialIndex);
            }, 4000);
        }
        if (testimonialPrev) {
            testimonialPrev.addEventListener("click", function () {
                testimonialIndex = (testimonialIndex - 1 + testimonialSlides.length) % testimonialSlides.length;
                showTestimonial(testimonialIndex);
                startTestimonialInterval();
            });
        }

        if (testimonialNext) {
            testimonialNext.addEventListener("click", function () {
                testimonialIndex = (testimonialIndex + 1) % testimonialSlides.length;
                showTestimonial(testimonialIndex);
                startTestimonialInterval();
            });
        }

        if (testimonialSlider) {
            testimonialSlider.addEventListener("mouseenter", function () {
                clearInterval(testimonialInterval);
            });

            testimonialSlider.addEventListener("mouseleave", function () {
                startTestimonialInterval();
            });
        }

        startTestimonialInterval();
    }