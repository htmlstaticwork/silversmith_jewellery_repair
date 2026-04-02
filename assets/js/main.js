// main.js
document.addEventListener('DOMContentLoaded', () => {

    /* --- Mobile Menu Toggle --- */
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileNav = document.querySelector('.mobile-nav');
    const mobileClose = document.querySelector('.mobile-close');

    if (mobileMenuBtn && mobileNav && mobileClose) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileNav.classList.add('active');
        });

        mobileClose.addEventListener('click', () => {
            mobileNav.classList.remove('active');
        });

        // Mobile Submenu Toggles
        const mobileToggles = document.querySelectorAll('.mobile-nav-toggle');
        mobileToggles.forEach(toggle => {
            toggle.addEventListener('click', (e) => {
                const submenu = toggle.nextElementSibling;
                const isOpen = toggle.classList.contains('is-open');
                const isIconClick = e.target.classList.contains('mobile-nav-toggle-icon') || 
                                   e.target.closest('.mobile-nav-toggle-icon');
                
                // If it's closed, open it on first click (anywhere)
                if (!isOpen) {
                    e.preventDefault();
                    toggle.classList.add('is-open');
                    if (submenu) submenu.classList.add('is-open');
                } 
                // If it's open and the user clicks the ICON, close it.
                // If they click the text, let it navigate.
                else if (isIconClick) {
                    e.preventDefault();
                    toggle.classList.remove('is-open');
                    if (submenu) submenu.classList.remove('is-open');
                }
            });
        });
    }

    /* --- Dark Mode Toggle --- */
    const themeToggleBtn = document.querySelectorAll('.theme-toggle');
    const currentTheme = localStorage.getItem('theme');
    
    // Check local storage for theme preference
    if (currentTheme) {
        document.body.classList.toggle('dark-mode', currentTheme === 'dark');
    }

    themeToggleBtn.forEach(btn => {
        btn.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            let theme = 'light';
            if (document.body.classList.contains('dark-mode')) {
                theme = 'dark';
            }
            localStorage.setItem('theme', theme);
        });
    });

    /* --- RTL Toggle --- */
    const rtlToggleBtn = document.querySelectorAll('.rtl-toggle');
    const currentDir = localStorage.getItem('dir');
    
    if (currentDir) {
        document.documentElement.setAttribute('dir', currentDir);
    }

    rtlToggleBtn.forEach(btn => {
        btn.addEventListener('click', () => {
            let dir = document.documentElement.getAttribute('dir') === 'rtl' ? 'ltr' : 'rtl';
            document.documentElement.setAttribute('dir', dir);
            localStorage.setItem('dir', dir);
        });
    });

    /* --- Before/After Slider --- */
    const baSlider = document.querySelector('.ba-slider');
    const baImageAfter = document.querySelector('.ba-image-after');
    const baContainer = document.querySelector('.ba-container');
    
    if (baSlider && baImageAfter && baContainer) {
        let isDown = false;

        const moveSlider = (x) => {
            const rect = baContainer.getBoundingClientRect();
            let position = ((x - rect.left) / baContainer.offsetWidth) * 100;
            if (position < 0) position = 0;
            if (position > 100) position = 100;
            
            baSlider.style.left = `${position}%`;
            // The after image covers the right side.
            // Polygon definition: Left-Top, Right-Top, Right-Bottom, Left-Bottom
            // We want to show from the right edge inward. So we hide left of the slider
            baImageAfter.style.clipPath = `polygon(${position}% 0, 100% 0, 100% 100%, ${position}% 100%)`;
        };

        baContainer.addEventListener('mousedown', (e) => {
            isDown = true;
            moveSlider(e.clientX);
        });
        
        baContainer.addEventListener('touchstart', (e) => {
            isDown = true;
            moveSlider(e.touches[0].clientX);
            // Prevent scroll while sliding
            if(e.cancelable) e.preventDefault(); 
        }, { passive: false });

        window.addEventListener('mouseup', () => { isDown = false; });
        window.addEventListener('touchend', () => { isDown = false; });

        window.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            moveSlider(e.clientX);
        });
        
        window.addEventListener('touchmove', (e) => {
            if (!isDown) return;
            moveSlider(e.touches[0].clientX);
            // Prevent scroll while sliding
            if(e.cancelable) e.preventDefault();
        }, { passive: false });
    }

    /* --- Gallery Zoom Component --- */
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    if (portfolioItems.length > 0) {
        const lightbox = document.createElement('div');
        lightbox.className = 'lightbox';
        lightbox.innerHTML = `
            <button class="lightbox-close" aria-label="Close Lightbox">&times;</button>
            <div class="lightbox-content">
                <img src="" alt="Gallery View">
            </div>
        `;
        document.body.appendChild(lightbox);

        const lightboxImg = lightbox.querySelector('img');
        const lightboxCloseBtn = lightbox.querySelector('.lightbox-close');

        portfolioItems.forEach(item => {
            item.addEventListener('click', () => {
                const img = item.querySelector('img');
                if (img) {
                    lightboxImg.src = img.src;
                    lightbox.classList.add('active');
                }
            });
        });

        lightboxCloseBtn.addEventListener('click', () => {
            lightbox.classList.remove('active');
        });

        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                lightbox.classList.remove('active');
            }
        });
    }

    /* --- Scroll to Top --- */
    const scrollTopBtn = document.querySelector('.scroll-top-btn');
    if (scrollTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        });

        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    /* --- Reveal Animations --- */
    const revealElements = document.querySelectorAll('.reveal-up, .fade-in, .scale-up');
    
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target); // Only trigger once
                }
            });
        }, {
            root: null,
            threshold: 0.15, // Trigger when 15% visible
            rootMargin: "0px 0px -50px 0px"
        });

        revealElements.forEach(el => revealObserver.observe(el));
    }

});
