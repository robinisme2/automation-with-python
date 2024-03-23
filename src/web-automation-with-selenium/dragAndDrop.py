from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
source = driver.find_element("xpath", '//*[@id="box3"]')
destination = driver.find_element("xpath", '//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
