import os
import re
import glob

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
html_files = glob.glob(os.path.join(base_dir, 'pages', '*.html'))

for file_path in html_files:
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add RTL stylesheet link in <head>
    if 'rtl.css' not in content:
        content = content.replace('    <link rel="stylesheet" href="../assets/css/dark-mode.css">', 
                                  '    <link rel="stylesheet" href="../assets/css/dark-mode.css">\n    <link rel="stylesheet" href="../assets/css/rtl.css">')

    # 2. Update desktop nav-actions
    # We replace the whole nav-actions div to be safe.
    nav_actions_pattern = r'<div class="nav-actions">.*?</div>'
    
    login_active = ' class="btn btn-outline btn-sm active"' if filename == 'login.html' else ' class="btn btn-outline btn-sm"'
    signup_active = ' class="btn btn-primary btn-sm active"' if filename == 'signup.html' else ' class="btn btn-primary btn-sm"'
    
    new_nav_actions = f'''<div class="nav-actions">
                <button class="rtl-toggle" aria-label="Toggle RTL Layout">
                    <i data-lucide="languages"></i>
                </button>
                <button class="theme-toggle" aria-label="Toggle Dark Mode">
                    <i data-lucide="moon"></i>
                </button>
                <a href="login.html"{login_active}>Login</a>
                <a href="signup.html"{signup_active}>Sign Up</a>
            </div>'''
    
    content = re.sub(nav_actions_pattern, new_nav_actions, content, flags=re.DOTALL)

    # 3. Update mobile-nav-links
    # Add Login and Sign Up before the closing </div> of mobile-nav-links
    if 'href="login.html"' not in content:
        # Find the end of the mobile-nav-links div
        mobile_nav_end_pattern = r'(<div class="mobile-nav-links">.*?)(</div>)'
        
        login_link = '\n            <a href="login.html">Login</a>'
        signup_link = '\n            <a href="signup.html" style="font-weight: 600;">Sign Up</a>'
        
        content = re.sub(mobile_nav_end_pattern, r'\1' + login_link + signup_link + r'\2', content, flags=re.DOTALL)

    # 4. Update mobile theme toggle button to include RTL
    if 'Toggle RTL' not in content:
        # Looking for the Toggle Theme button block
        mobile_theme_pattern = r'(<button class="theme-toggle btn btn-secondary"[^>]*>.*?</button>)'
        
        rtl_btn = '\n        <button class="rtl-toggle btn btn-secondary" style="justify-content: center; width: auto;" aria-label="Toggle RTL Layout">Toggle RTL</button>'
        
        content = re.sub(mobile_theme_pattern, r'\1' + rtl_btn, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Global navigation updated across {len(html_files)} files.")
