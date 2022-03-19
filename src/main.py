from pathlib import Path
import datetime
import pytz
# import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def update_footer():
    timestamp = datetime.datetime.now(pytz.timezone("Canada/Central")).strftime("%c")
    footer = Path('../FOOTER.md').read_text()
    return footer.format(timestamp=timestamp)

## retrieve screenshot from Kaggle using Selenium
PATH = "/usr/bin/chromedriver"
Xpath = '//*[@id="site-container"]/div/div[5]/div/div[2]/div'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--headless")

try:
    from webdriver_manager.chrome import ChromeDriverManager
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
except ImportError as e: # module doesn't exist, define driver by executable path
    # driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
    driver = webdriver.Chrome(PATH, options=chrome_options) #main.py:25: DeprecationWarning: executable_path has been deprecated, please pass in a Service object

driver.implicitly_wait(10)

driver.get("https://kaggle.com/yongwonjin")
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.XPATH, Xpath)))
driver.find_element(by=By.XPATH, value=Xpath).click() # main.py:31: DeprecationWarning: find_element_by_xpath is deprecated. Please use find_element(by=By.XPATH, value=xpath) instead
driver.save_screenshot("kaggleprofile.png")

# img_data = requests.get("https://capture-website-api.herokuapp.com/capture?url=https://www.kaggle.com/yongwonjin").content
# with open(Path('./kaggleprofile.png'), 'wb') as handler:
#   handler.write(img_data)

readme = Path('../README.md').read_text()
readme_base = readme[:readme.find('<hr>')] # anchor position

with open('../README.md', "w+") as f:
    f.write(readme_base + update_footer())
