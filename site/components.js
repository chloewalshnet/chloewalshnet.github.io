/**
 * Shared Components System
 * This file contains functions to load and render shared components across pages
 */

document.addEventListener('DOMContentLoaded', () => {
    // Load all shared components
    loadNavbar();
    loadFooter();
    
    // Add active class to current page in navbar
    highlightCurrentPage();
});

// Load the navbar component into designated elements
function loadNavbar() {
    const navbarPlaceholders = document.querySelectorAll('#navbar-placeholder');
    
    const navbarHTML = `
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="index.html">Chloe Walsh</a>
            
            <!-- Social icons moved next to brand -->
            <div class="social-icons-container d-none d-sm-flex">
                <a href="https://linkedin.com/" target="_blank" class="social-icon"><i class="fab fa-linkedin"></i></a>
                <a href="https://github.com/" target="_blank" class="social-icon"><i class="fab fa-github"></i></a>
                <a href="mailto:email@email.com" class="social-icon"><i class="fas fa-envelope"></i></a>
            </div>
            
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="index.html">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="portfolio.html">Portfolio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="about.html">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="resume.html">Resume</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="blog.html">Blog</a>
                    </li>
                </ul>
                <!-- Social icons for mobile only -->
                <div class="social-icons-container d-flex d-sm-none mt-3">
                    <a href="https://linkedin.com/" target="_blank" class="social-icon"><i class="fab fa-linkedin"></i></a>
                    <a href="https://github.com/" target="_blank" class="social-icon"><i class="fab fa-github"></i></a>
                    <a href="mailto:email@email.com" class="social-icon"><i class="fas fa-envelope"></i></a>
                </div>
            </div>
        </div>
    </nav>`;
    
    navbarPlaceholders.forEach(placeholder => {
        placeholder.innerHTML = navbarHTML;
    });
}

// Load the footer component into designated elements
function loadFooter() {
    const footerPlaceholders = document.querySelectorAll('#footer-placeholder');
    
    const footerHTML = `
    <footer class="footer mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <h4>Chloe Walsh</h4>
                    <p>Video Game Developer specializing in narrative design and immersive gameplay experiences.</p>
                </div>
                <div class="col-md-3">
                    <h5>Links</h5>
                    <ul class="list-unstyled">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="portfolio.html">Portfolio</a></li>
                        <li><a href="about.html">About</a></li>
                        <li><a href="resume.html">Resume</a></li>
                        <li><a href="blog.html">Blog</a></li>
                    </ul>
                </div>
                <div class="col-md-3">
                    <h5>Connect</h5>
                    <div class="footer-social">
                        <a href="https://linkedin.com/" target="_blank" class="social-icon"><i class="fab fa-linkedin"></i></a>
                        <a href="https://github.com/" target="_blank" class="social-icon"><i class="fab fa-github"></i></a>
                        <a href="mailto:email@email.com" class="social-icon"><i class="fas fa-envelope"></i></a>
                    </div>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col-12 text-center">
                    <p class="copyright">© ${new Date().getFullYear()} Chloe Walsh. All rights reserved.</p>
                </div>
            </div>
        </div>
    </footer>`;
    
    footerPlaceholders.forEach(placeholder => {
        placeholder.innerHTML = footerHTML;
    });
}

// Highlight the current page in the navigation menu
function highlightCurrentPage() {
    const currentPage = window.location.pathname.split('/').pop();
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        link.removeAttribute('aria-current');
        
        const linkPage = link.getAttribute('href');
        if ((currentPage === '' || currentPage === '/' || currentPage === 'index.html') && linkPage === 'index.html') {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        } else if (linkPage === currentPage) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        }
    });
}
