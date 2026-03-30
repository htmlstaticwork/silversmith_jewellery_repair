import os
import re
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

# Standard footer logo structure:
standard_footer_logo = '''<div class="logo">
                        <i data-lucide="gem" class="logo-icon"></i>
                        <a href="index.html">Silver</a>
                    </div>'''

# We need to find the .footer-brand div and replace its current logo structure.
# It might look like <h2>Silver</h2> or the div we added earlier.

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match various existing patterns in footer-brand
    # Pattern 1: The one with inline styles we added earlier
    pattern1 = r'<div class="logo" style="margin-bottom: 1rem;">.*?<i data-lucide="gem" class="logo-icon"[^>]*></i>.*?<a href="index\.html"[^>]*>Silver</a>.*?</div>'
    
    # Pattern 2: Legacy h2
    pattern2 = r'<h2>Silver</h2>'

    new_content = re.sub(pattern1, standard_footer_logo, content, flags=re.DOTALL)
    new_content = re.sub(pattern2, standard_footer_logo, new_content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Standardized footer logo in {count} files.")
