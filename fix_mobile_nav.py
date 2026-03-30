import os
import re
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    mobile_nav_match = re.search(r'<div class="mobile-nav-links">(.*?)</div>', content, re.DOTALL)
    if mobile_nav_match:
        inner = mobile_nav_match.group(1)
        
        # Remove the generated dropdown block from mobile-nav only
        dropdown_pattern = r'\s*<div class="dropdown">\s*<a href="index\.html"(?:\s+class="active")?>Home <i data-lucide="chevron-down"[^>]*></i></a>\s*<div class="dropdown-content">\s*<a href="index\.html">Home 1 \(Classic\)</a>\s*<a href="index-2\.html">Home 2 \(Premium\)</a>\s*</div>\s*</div>'
        
        cleaned = re.sub(dropdown_pattern, '', inner, flags=re.DOTALL)
        
        content = content.replace(inner, cleaned)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Fixed mobile nav in {len(html_files)} files.")
