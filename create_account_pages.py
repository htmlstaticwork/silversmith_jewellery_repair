import os
import re

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
index_file = os.path.join(base_dir, 'pages', 'index.html')
login_file = os.path.join(base_dir, 'pages', 'login.html')
signup_file = os.path.join(base_dir, 'pages', 'signup.html')

with open(index_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Replace <title> and <main> for Login
login_main = '''    <main>
        <section class="account-section">
            <div class="account-card reveal-up">
                <div class="account-header">
                    <h1>Welcome Back</h1>
                    <p style="color: var(--text-secondary);">Access your custom orders and favorites.</p>
                </div>
                
                <form id="loginForm">
                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" id="email" class="form-control" placeholder="name@example.com" required>
                    </div>
                    <div class="form-group">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label for="password">Password</label>
                            <a href="#" style="font-size: 0.75rem; font-weight: 500; color: var(--accent-color);">Forgot Password?</a>
                        </div>
                        <input type="password" id="password" class="form-control" placeholder="••••••••" required>
                    </div>
                    
                    <div class="form-group" style="display: flex; align-items: center; gap: 0.5rem; margin-top: -0.5rem;">
                        <input type="checkbox" id="remember" style="cursor: pointer;">
                        <label for="remember" style="margin-bottom: 0; cursor: pointer; font-size: 0.8125rem;">Remember me</label>
                    </div>

                    <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Sign In</button>
                    
                    <div class="form-footer">
                        Don't have an account? <a href="signup.html">Create an Account</a>
                    </div>
                </form>
            </div>
        </section>
    </main>'''

login_content = re.sub(r'<title>.*?</title>', '<title>Login | Silver</title>', template_content)
login_content = re.sub(r'<main>.*?</main>', lambda m: login_main, login_content, flags=re.DOTALL)

with open(login_file, 'w', encoding='utf-8') as f:
    f.write(login_content)

# Replace <title> and <main> for Signup
signup_main = '''    <main>
        <section class="account-section">
            <div class="account-card reveal-up">
                <div class="account-header">
                    <h1>Join Us</h1>
                    <p style="color: var(--text-secondary);">Create an account for personalized jewelry experiences.</p>
                </div>
                
                <form id="signupForm">
                    <div class="form-group">
                        <label for="fullname">Full Name</label>
                        <input type="text" id="fullname" class="form-control" placeholder="John Doe" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" id="email" class="form-control" placeholder="name@example.com" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" class="form-control" placeholder="Create a password" required>
                    </div>
                    <div class="form-group">
                        <label for="confirmPassword">Confirm Password</label>
                        <input type="password" id="confirmPassword" class="form-control" placeholder="Confirm your password" required>
                    </div>

                    <div class="form-group" style="display: flex; align-items: flex-start; gap: 0.5rem; margin-top: -0.5rem;">
                        <input type="checkbox" id="terms" style="cursor: pointer; margin-top: 0.25rem;" required>
                        <label for="terms" style="margin-bottom: 0; cursor: pointer; font-size: 0.8125rem;">I agree to the <a href="#">Terms & Conditions</a> and <a href="#">Privacy Policy</a>.</label>
                    </div>

                    <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Create Account</button>
                    
                    <div class="form-footer">
                        Already have an account? <a href="login.html">Sign In</a>
                    </div>
                </form>
            </div>
        </section>
    </main>'''

signup_content = re.sub(r'<title>.*?</title>', '<title>Sign Up | Silver</title>', template_content)
signup_content = re.sub(r'<main>.*?</main>', lambda m: signup_main, signup_content, flags=re.DOTALL)

with open(signup_file, 'w', encoding='utf-8') as f:
    f.write(signup_content)

print("Login and Signup pages created successfully!")
