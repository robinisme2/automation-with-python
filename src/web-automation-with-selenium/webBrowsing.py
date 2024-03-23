from selenium import webdriver
url = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(url)
messageField = driver.find_element("xpath", '//*[@id="user-message"]')
messageField.send_keys("Hello World")
showMessageButton = driver.find_element("xpath", '//*[@id="get-input"]/button')
showMessageButton.click()
additionField1 = driver.find_element("xpath", '//*[@id="value1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element("xpath", '//*[@id="value2"]')
additionField2.send_keys('12')
getTotalButton = driver.find_element("xpath", '//*[@id="gettotal"]/button')
getTotalButton.click()