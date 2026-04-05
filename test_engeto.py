import pytest
from playwright.sync_api import sync_playwright, Page, expect


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        
        page.goto("https://www.engeto.cz/")
       
        cookie_banner = page.locator("#cookiescript_injected")
        if cookie_banner.is_visible(timeout=5000):
            page.get_by_role("button", name="Chápu a přijímám!").click()
        
        page.wait_for_load_state("domcontentloaded")
        yield page
        
        browser.close()

def test_hlavni_stranka_se_nacita_spravne(page: Page):
    """Test 1: Ověření načtení hlavní stránky + titulku."""
    expect(page).to_have_title("Kurzy programování a dalších IT technologií | ENGETO")
    expect(page.get_by_role("heading", name="Získej náskok s tech & AI dovednostmi")).to_be_visible()

def test_hero_sekce_a_cta_tlacitka(page: Page):
    """Test 2: Hlavní hero sekce + CTA tlačítka."""
    hero_heading = page.get_by_role("heading", name="Získej náskok s tech & AI dovednostmi")
    expect(hero_heading).to_be_visible()
    
    cta_link = page.get_by_role("link", name="Akademie s lektorem")
    expect(cta_link).to_be_visible()
    expect(cta_link).to_have_attribute("href", "/prehled-kurzu/")

def test_navigace_do_prehledu_kurzu(page: Page):
    """Test 3: Navigace do přehledu všech kurzů a ověření, že se načetla správná stránka"""
    kurzy_link = page.get_by_role("link", name="Kurzy", exact=True)
    kurzy_link.click()
    
    expect(page).to_have_url("https://engeto.cz/prehled-kurzu/")    
    expect(page.get_by_role("heading", name="Kurzy programování, digitálních dovedností & AI")).to_be_visible()    
    expect(page.get_by_role("heading", name="Datový analytik s Pythonem")).to_be_visible()

def test_presmerovani_na_Reference_a_příběhy(page: Page):
    """Test 4: Testuje přesměrování na stránku "Reference a příběhy" po kliknutí na odkaz v hlavním menu."""
    link = page.get_by_role("link", name="Reference a příběhy")
    link.click()
    expect(page).to_have_url("https://engeto.cz/absolventi/")

def test_footer_existuje(page: Page):
    """Test 5: Ověření existence a obsahu patičky."""
    footer = page.locator("footer")
    
    expect(footer).to_be_visible()
    expect(footer).to_contain_text("ENGETO")