import os
import re
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

for file_path in html_files:
    filename = os.path.basename(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop Nav Replacement
    # Match: <a href="index.html" class="active">Home</a> or <a href="index.html">Home</a>
    desktop_pattern = r'<a\s+href="index\.html"(?:\s+class="active")?>Home</a>'
    
    desktop_replacement = r'''<div class="dropdown">
                    <a href="index.html"\1>Home <i data-lucide="chevron-down" style="width: 16px; height: 16px;"></i></a>
                    <div class="dropdown-content">
                        <a href="index.html">Home 1 (Classic)</a>
                        <a href="index-2.html">Home 2 (Premium)</a>
                    </div>
                </div>'''
    
    # We need to preserve the active class if it exists.
    def desktop_replacer(match):
        original = match.group(0)
        active_class = ' class="active"' if 'class="active"' in original else ''
        return f'''<div class="dropdown">
                    <a href="index.html"{active_class}>Home <i data-lucide="chevron-down" style="width: 16px; height: 16px;"></i></a>
                    <div class="dropdown-content">
                        <a href="index.html">Home 1 (Classic)</a>
                        <a href="index-2.html">Home 2 (Premium)</a>
                    </div>
                </div>'''

    new_content = re.sub(desktop_pattern, desktop_replacer, content)

    # Mobile Nav Replacement
    # In mobile nav it strictly looks like: <a href="index.html">Home</a>
    # Wait, the mobile nav might just get updated along with the desktop if it matches `desktop_pattern`.
    # Let's ensure mobile nav uses indented instead of dropdown by checking context.
    # It's better to explicitly search inside the <div class="mobile-nav-links">.
    # Actually, we can just find the <div class="mobile-nav-links"> and modify inside it.
    
    mobile_nav_match = re.search(r'<div class="mobile-nav-links">(.*?)</div>', new_content, re.DOTALL)
    if mobile_nav_match:
        old_mobile_inner = mobile_nav_match.group(1)
        # remove any existing Home elements strictly to avoiding double replacing
        cleaned = re.sub(r'\s*<a href="index\.html"(?:\s+class="active")?>Home</a>', '', old_mobile_inner)
        cleaned = re.sub(r'\s*<a href="index\.html"[^>]*>- Home 1 \(Classic\)</a>', '', cleaned)
        cleaned = re.sub(r'\s*<a href="index-2\.html"[^>]*>- Home 2 \(Premium\)</a>', '', cleaned)
        
        new_mobile_inner = f'''
            <a href="index.html">Home</a>
            <a href="index.html" style="margin-left: 1rem; font-size: 1.1rem; color: var(--text-secondary);">- Home 1 (Classic)</a>
            <a href="index-2.html" style="margin-left: 1rem; font-size: 1.1rem; color: var(--text-secondary);">- Home 2 (Premium)</a>{cleaned}'''
            
        new_content = new_content.replace(mobile_nav_match.group(0), f'<div class="mobile-nav-links">{new_mobile_inner}</div>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Home dropdown successfully added to {len(html_files)} HTML files.")
