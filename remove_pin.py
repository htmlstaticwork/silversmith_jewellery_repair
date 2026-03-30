import os
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

target_string1 = '                        <a href="#" aria-label="Pinterest" style="color: #fff;"><i data-lucide="pin"></i></a>\n'
target_string2 = '<a href="#" aria-label="Pinterest" style="color: #fff;"><i data-lucide="pin"></i></a>'

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    if target_string1 in content:
        content = content.replace(target_string1, '')
        modified = True
    elif target_string2 in content:
        content = content.replace(target_string2, '')
        modified = True

    if modified:
        count += 1
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Pinterest button successfully removed from {count} files out of {len(html_files)} total HTML files.")
