import os
import re
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

# Header logo structure for reference:
# <div class="logo">
#     <i data-lucide="gem" class="logo-icon"></i>
#     <a href="index.html">Silver</a>
# </div>

footer_logo_replacement = '''<div class="logo" style="margin-bottom: 1rem;">
                        <i data-lucide="gem" class="logo-icon" style="color: #fff;"></i>
                        <a href="index.html" style="color: #fff;">Silver</a>
                    </div>'''

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <h2>Silver</h2> inside .footer-brand and replace it
    # We use a non-greedy match for the content around it if needed, but simple string replace is safer if consistent.
    if '<h2>Silver</h2>' in content:
        # Check if it's inside footer-brand to be sure
        new_content = content.replace('<h2>Silver</h2>', footer_logo_replacement)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

print(f"Updated footer logo in {count} files.")
