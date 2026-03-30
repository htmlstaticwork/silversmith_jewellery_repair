import os
import re
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Blog link from the footer specifically
    # It looks exactly like: <li><a href="blog.html">Blog</a></li>
    content = re.sub(r'\s*<li><a href="blog\.html">Blog</a></li>', '', content)
    
    # Rename Reviews to Testimonials
    content = re.sub(r'<li><a href="testimonials\.html">Reviews</a></li>', r'<li><a href="testimonials.html">Testimonials</a></li>', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Footer links systematically updated in {len(html_files)} standard pages.")
