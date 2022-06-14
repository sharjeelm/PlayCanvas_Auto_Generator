from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
print(f"Script Started at {now.strftime('%d/%m/%Y %H:%M:%S')}")

from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
#chromeOptions.add_experimental_option("detach", True)
#chromeOptions.add_experimental_option('useAutomationExtension', False)
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("https://playcanv.as/b/IGAbCnIk/")

total_wait_time_in_sec = 40
iframe = driver.find_element_by_xpath("//iframe[@id='frame']")
driver.switch_to.frame(iframe)
is_complete = False

while(not is_complete):
    try:
        WebDriverWait(driver, total_wait_time_in_sec).until(EC.presence_of_element_located((By.ID, "Div1")))
        is_complete=True
    except Exception as E:
        is_complete=False

now = datetime.now()
print(f"Script ended at {now.strftime('%d/%m/%Y %H:%M:%S')}")