from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#google chrome webdriver
driver = webdriver.Chrome()
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

#clicking on the button to go to continue  page
new_customer_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/a')
new_customer_btn.click()

#Register Account
#Personal Details

#Checking firstname 'required' on the registration page
firstname_field = driver.find_element_by_xpath('//fieldset/div[2]')  #  //*[@id="input-firstname"]  not working using XPATH //account/div[2]/div/input
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

#filling firstname input
firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Marine")

#Checking lastname 'required' on the registration page
lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")  #//account/div[3]/div/input or //*[@id="input-lastname"] not working
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

#filling Lastname input
lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Olvera")

#Checking Email 'required' on the registration page
email_field = driver.find_element_by_xpath("//fieldset/div[4]")  #//account/div[4]/div/input"
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class

#filling Email input
email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("marineolvera07@gmail.com")

#Checking Telephone 'required' on the registration page
telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")  #//account/div[5]/div/input
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

#filling Telephone input
telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("312-871-1101")

#Checking Address1 'required' on the registration page
address1_field = driver.find_element_by_xpath("//fieldset[2]/div[2]")
address1_field_class = address1_field.get_attribute("class")
assert "required" in address1_field_class
#filling address1 input
address1_input = driver.find_element_by_id("input-address-1")
address1_input.clear()
address1_input.send_keys("6045 N fairfield ave")

#Checking City 'required' on the registration page
city_field = driver.find_element_by_xpath("//fieldset[2]/div[4]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class
#filling city input
city_input = driver.find_element_by_id("input-city")
city_input.clear()
city_input.send_keys("Chicago")


#Checking Password 'required' on the registration page
password_field = driver.find_element_by_xpath("//fieldset[3]/div[1]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
# filling password input
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("123password")

#Checking password confirm 'required' on the registration page
confirm_field = driver.find_element_by_xpath("//fieldset[3]/div[2]")
confirm_field_class = confirm_field.get_attribute("class")
assert "required" in confirm_field_class

#filling passwordconfirm input
confirm_input = driver.find_element_by_id("input-confirm")
confirm_input.clear()
confirm_input.send_keys("123password")



#webdriverwait
returning_customer_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input') #returning cutsomer Login button XPATH //*[@id="content"]/div/div[2]/div/form/input
returning_customer_btn.click()
wd_wait = WebDriverWait(driver, 10)
returning_customer_btn = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'login')]")))


driver.quit()

