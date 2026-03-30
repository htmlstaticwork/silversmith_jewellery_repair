import os
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

scroll_btn_html = '''    <!-- Scroll to Top Button -->
    <button class="scroll-top-btn" aria-label="Scroll to top">
        <i data-lucide="arrow-up"></i>
    </button>

    <!-- Scripts -->'''

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Only add if it doesn't already exist
    if 'class="scroll-top-btn"' not in content:
        content = content.replace('    <!-- Scripts -->', scroll_btn_html)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Scroll to top HTML added to {len(html_files)} files.")
