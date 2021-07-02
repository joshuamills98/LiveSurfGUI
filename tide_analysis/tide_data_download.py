from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
# chrome_options.add_argument("--headless")


driver = webdriver.Chrome(ChromeDriverManager(version="91.0.4472.101").install(), options=chrome_options)
url = "https://tides.willyweather.com.au/nsw/south-coast/moruya-heads.html"

driver.get(url)
try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "block tide-clock"))
    )
finally:
    element.screenshot('foo.png')
    driver.quit()

print("end...")