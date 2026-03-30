import os
import re
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

for file_path in html_files:
    filename = os.path.basename(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    about_pattern = r'(<a\s+href="about\.html"[^>]*>About</a>)'
    
    def replacer(match):
        about_tag = match.group(1)
        active_class = ' class="active"' if filename == 'contact.html' else ''
        return f'{about_tag}\n                <a href="contact.html"{active_class}>Contact</a>'

    new_content = re.sub(about_pattern, replacer, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Contact page carefully inserted into navigation flow for {len(html_files)} HTML files.")
