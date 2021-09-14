from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#google chrome webdriver
driver = webdriver.Chrome()
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

#Login Account
# Sending E-Mail Address to the login page

email_input = driver.find_element_by_xpath("//body/div[2]/div/div/div/div[2]/div/form/div[1]/input") # or write in the parenthese ('input-email")  inside inspect under div ID "content" and  div Class "form-group"
email_input.clear()
email_input.send_keys("marineolvera07@gmail.com")

#Sending Password to the login page

password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("123password")

#clicking on the button to go to login page
returning_customer_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input')
returning_customer_btn.click()

returning_customer_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input') #returning cutsomer Login button XPATH //*[@id="content"]/div/div[2]/div/form/input
returning_customer_btn.click()
wd_wait = WebDriverWait(driver, 10)
returning_customer_btn = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'login')]")))

driver.quit()