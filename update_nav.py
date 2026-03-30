import os
import re

html_files = [
    'pages/index.html',
    'pages/services.html',
    'pages/portfolio.html',
    'pages/custom-jewelry.html',
    'pages/about.html',
    'pages/testimonials.html',
    'pages/blog.html',
    'pages/contact.html'
]

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"

for rel_path in html_files:
    file_path = os.path.join(base_dir, rel_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the nav-links div
    nav_links_pattern = r'<nav class="nav-links">(.*?)</nav>'
    match = re.search(nav_links_pattern, content, re.DOTALL)
    if not match:
        continue
    
    nav_inner = match.group(1)
    
    # We will build a new nav-inner, trying to preserve 'class="active"' if it was on a replaced element
    # We want: Home, Services, Dropdown(Custom Design -> Portfolio, Testimonials), About (and maybe Blog?)
    active_home = ' class="active"' if 'href="index.html" class="active"' in nav_inner else ''
    active_services = ' class="active"' if 'href="services.html" class="active"' in nav_inner else ''
    active_about = ' class="active"' if 'href="about.html" class="active"' in nav_inner else ''
    
    # Dropdown logic: Custom Design should be active if custom-jewelry is active.
    # What if portfolio or testimonials are active? We can add active class to them inside dropdown, or to the custom-design link itself.
    active_custom = ' class="active"' if 'href="custom-jewelry.html" class="active"' in nav_inner or 'href="portfolio.html" class="active"' in nav_inner or 'href="testimonials.html" class="active"' in nav_inner else ''
    
    # Rebuild nav-links
    new_nav = f'''
                <a href="index.html"{active_home}>Home</a>
                <a href="services.html"{active_services}>Services</a>
                <div class="dropdown">
                    <a href="custom-jewelry.html"{active_custom}>Custom Design <i data-lucide="chevron-down" style="width: 16px; height: 16px;"></i></a>
                    <div class="dropdown-content">
                        <a href="portfolio.html">Portfolio</a>
                        <a href="testimonials.html">Testimonials</a>
                    </div>
                </div>
                <a href="about.html"{active_about}>About</a>
            '''
            
    content = content.replace(match.group(0), f'<nav class="nav-links">\n{new_nav}</nav>')

    # Now the mobile nav
    mobile_pattern = r'<div class="mobile-nav-links">(.*?)</div>'
    match_mobile = re.search(mobile_pattern, content, re.DOTALL)
    if match_mobile:
        new_mobile = '''
            <a href="index.html">Home</a>
            <a href="services.html">Services</a>
            <a href="custom-jewelry.html">Custom Design</a>
            <a href="portfolio.html" style="margin-left: 1rem; font-size: 1.1rem; color: var(--text-secondary);">- Portfolio</a>
            <a href="testimonials.html" style="margin-left: 1rem; font-size: 1.1rem; color: var(--text-secondary);">- Testimonials</a>
            <a href="about.html">About</a>
            <a href="blog.html">Blog</a>
            <a href="contact.html">Contact</a>
        '''
        content = content.replace(match_mobile.group(0), f'<div class="mobile-nav-links">\n{new_mobile}</div>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML files updated")
