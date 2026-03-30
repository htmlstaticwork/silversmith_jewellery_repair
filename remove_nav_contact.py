import os
import re
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the 'Get a Quote' button matching the nav bar styles
    content = re.sub(r'<a\s+href="contact\.html"\s+class="btn\s+btn-primary"[^>]*>Get a Quote</a>\s*', '', content)

    # Remove the pure 'Contact' text link located in the mobile nav links list
    content = re.sub(r'<a\s+href="contact\.html"\s*>Contact</a>\s*', '', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files.")
