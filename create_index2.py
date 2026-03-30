import os
import re

base_dir = r"c:\Users\prasa\OneDrive\Desktop\SF\March websites 2026\2nd\silversmith_jewellery_repair"
index_file = os.path.join(base_dir, 'pages', 'index.html')
index_2_file = os.path.join(base_dir, 'pages', 'index-2.html')

with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <title> to differentiate
content = content.replace('<title>Silver & Jewelry Repair</title>', '<title>Silver | Premium Experience</title>')

premium_main = '''    <main>
        <!-- Premium Hero -->
        <section class="premium-hero" style="background-image: url('https://images.unsplash.com/photo-1611591437281-460bfbe1220a?auto=format&fit=crop&q=80&w=1920');">
            <div class="premium-hero-overlay"></div>
            <div class="premium-content">
                <h1 class="premium-title reveal-up">The Art of <br>Silver</h1>
                <p class="premium-subtitle reveal-up delay-200">Where timeless tradition meets contemporary elegance. Immerse yourself in the mastery of fine silversmithing.</p>
                <div class="reveal-up delay-400">
                    <a href="portfolio.html" class="btn btn-secondary" style="border-color: #fff; color: #fff;">Explore the Collection</a>
                </div>
            </div>
            <div class="scroll-indicator fade-in delay-500">
                <span>Scroll to Discover</span>
                <i data-lucide="chevron-down"></i>
            </div>
        </section>

        <!-- Storytelling Section 1 -->
        <section class="editorial-section section" style="background-color: var(--surface-color);">
            <div class="container editorial-grid">
                <div class="editorial-image scale-up">
                    <img src="https://images.unsplash.com/photo-1577908331566-6ec423d249f3?auto=format&fit=crop&q=80&w=800" alt="Master silversmith at work">
                </div>
                <div class="editorial-text reveal-up delay-200">
                    <h2>Forged with <br>Passion</h2>
                    <p>Every piece of silver holds a story. From the molten flame to the final, meticulous polish, our hands guide the transformation of raw elements into wearable art.</p>
                    <p>Our workshop is a sanctuary of focus, where century-old techniques are preserved and celebrated in every strike of the hammer.</p>
                    <a href="about.html" class="btn btn-primary" style="margin-top: 1rem;">Our Heritage</a>
                </div>
            </div>
        </section>

        <!-- Visual Portfolio Teaser -->
        <section class="section" style="padding-top: var(--spacing-xl);">
            <div class="container">
                <div class="section-header reveal-up">
                    <span class="section-subtitle">Exquisite Detail</span>
                    <h2 class="section-title">The Collection</h2>
                </div>
                
                <div class="portfolio-grid" style="margin-top: 4rem;">
                    <div class="portfolio-item scale-up delay-100">
                        <img src="https://images.unsplash.com/photo-1599643478524-fb524fa0a8c7?auto=format&fit=crop&q=80&w=800" alt="Silver Ring">
                    </div>
                    <div class="portfolio-item scale-up delay-200">
                        <img src="https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&q=80&w=800" alt="Silver Chain">
                    </div>
                    <div class="portfolio-item scale-up delay-300">
                        <img src="https://images.unsplash.com/photo-1610652492500-ded49ceeb378?auto=format&fit=crop&q=80&w=800" alt="Silver Bracelet">
                    </div>
                </div>
                <div class="reveal-up delay-400" style="text-align: center; margin-top: 3rem;">
                    <a href="portfolio.html" class="btn btn-secondary">View Full Gallery &rarr;</a>
                </div>
            </div>
        </section>

        <!-- Storytelling Section 2 (Reversed) -->
        <section class="editorial-section section" style="background-color: var(--surface-color);">
            <div class="container editorial-grid reversed">
                <div class="editorial-image scale-up delay-100">
                    <img src="https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&q=80&w=800" alt="Restored Silver Heirloom">
                </div>
                <div class="editorial-text reveal-up delay-200">
                    <h2>Restoring <br>Legacies</h2>
                    <p>Time takes its toll on all things, but true silver can always be revived.</p>
                    <p>Our restoration experts breathe life back into tarnished family heirlooms, repairing broken links and polishing surfaces until they reflect their original glory.</p>
                    <a href="services.html" class="btn btn-secondary" style="margin-top: 1rem;">Restoration Services</a>
                </div>
            </div>
        </section>

        <!-- Minimalist CTA -->
        <section class="section" style="background: var(--text-primary); color: var(--bg-color); text-align: center; padding: 8rem 0;">
            <div class="container reveal-up">
                <i data-lucide="gem" style="width: 48px; height: 48px; color: var(--accent-light); margin-bottom: 2rem;"></i>
                <h2 style="color: var(--bg-color); font-size: 3rem; margin-bottom: 1.5rem; font-weight: 300;">Ready to Craft Your Vision?</h2>
                <p style="color: #a0a0a0; max-width: 500px; margin: 0 auto 3rem; font-size: 1.125rem;">Reach out to schedule a private consultation with our master designers.</p>
                <a href="contact.html" class="btn" style="background: var(--bg-color); color: var(--text-primary); padding: 1rem 3rem;">Inquire Now</a>
            </div>
        </section>
    </main>'''

new_content = re.sub(r'<main>.*?</main>', lambda m: premium_main, content, flags=re.DOTALL)

with open(index_2_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Home 2 created successfully at index-2.html!")
