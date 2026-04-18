from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    # Setup driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Open website
        driver.get("https://www.google.com")
        
        # Find search box and enter query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("QA Automation")
        search_box.submit()
        
        # Check if results loaded
        assert "QA Automation" in driver.title
    
    finally:
        driver.quit()
