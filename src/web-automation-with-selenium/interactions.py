from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = 'https://www.google.com.tw/maps/'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(url)
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="assistive-chips"]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/button/span/span[2]')))
launchEarthButton.click()
