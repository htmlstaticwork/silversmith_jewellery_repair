import os
import re
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

# Read the full footer from index.html
index_path = os.path.join(base_dir, 'pages', 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

footer_match = re.search(r'(<footer>.*?</footer>)', index_content, re.DOTALL)
if footer_match:
    full_footer = footer_match.group(1)
    
    for file_path in html_files:
        if os.path.basename(file_path) == 'index.html':
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the existing simple footer with the full footer
        # Using lambda avoids regex group escape processing for the replacement string.
        new_content = re.sub(r'<footer[^>]*>.*?</footer>', lambda m: full_footer, content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    print(f"Full footer successfully added to {len(html_files) - 1} pages.")
else:
    print("Error: Could not find footer in index.html.")
