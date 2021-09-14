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
lastname_field_class = lastname_field.get.attribute("class")
assert "required" in lastname_field_class

#filling Lastname input
lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Olvera")

#Checking Email 'required' on the registration page
email_field = driver.find_element_by_xpath("//fieldset/div[4]")  #//account/div[4]/div/input"
email_field_class = email_field.get.attribute("class")
assert "required" in email_field_class

#filling Email input
email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("marineolvera07@gmail.com")

#Checking Telephone 'required' on the registration page
telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")  #//account/div[5]/div/input
telephone_field_class = telephone_field.get.attribute("class")
assert "required" in telephone_field_class

#filling Telephone input
telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("312-871-1101")

#Checking Address1 'required' on the registration page
Address1_field = driver.find_element_by_xpath("//address/div[2]/div/input") # //*[@id="input-address-1"] or //address/div[2]/div/input OR "//fieldset[2]/div[2]/div/input"
Address1_field_class = Address1_field.get.attribute("class")
assert "required" in Address1_field_class

#filling Address1 input
Address1_input = driver.find_element_by_id("input-Address1")
Address1_input.clear()
Address1_input.send_keys("60659 N Northwest Highway")


#Checking City 'required' on the registration page
City_field = driver.find_element_by_xpath("//address/div[4]/div/input")  #//address/div[4]/div/input"
City_field_class = City_field.get.attribute("class")
assert "required" in City_field_class

#filling City input
City_input = driver.find_element_by_id("input-City")
City_input.clear()
City_input.send_keys("Chicago")

#Checking Country 'required' on the registration page
Country_field = driver.find_element_by_xpath("//address/div[6]/div/select")  #//address/div[6]/div/select
Country_field_class = Country_field.get.attribute("class")
assert "required" in Country_field_class

#filling Country input
Country_input = driver.find_element_by_id("input-Country")
Country_input.clear()
Country_input.send_keys("USA")

#Checking State 'required' on the registration page
State_field = driver.find_element_by_xpath("//address/div[7]/div/select")  #//address/div[7]/div/select
State_field_class = State_field.get.attribute("class")
assert "required" in State_field_class

#filling State input
State_input = driver.find_element_by_id("input-State")
State_input.clear()
State_input.send_keys("Illinois")

#Checking Password 'required' on the registration page
Password_field = driver.find_element_by_xpath("//fieldset[3]/div[1]/div/input") # //fieldset[3]/div[1]/div/input we dont have the id name for this fieldset only the name of legend
Password_field_class = Password_field.get.attribute("class")
assert "required" in Password_field_class

#filling Password input
Password_input = driver.find_element_by_id("input-Password")
Password_input.clear()
Password_input.send_keys("123password")

#Checking passwordconfirm 'required' on the registration page
passwordconfirm_field = driver.find_element_by_xpath("//fieldset[3]/div[2]/div/input")  #//fieldset[3]/div[2]/div/input
passwordconfirm_field_class = passwordconfirm_field.get.attribute("class")
assert "required" in passwordconfirm_field_class

#filling passwordconfirm input
passwordconfirm_input = driver.find_element_by_id("input-passwordconfirm")
passwordconfirm_input.clear()
passwordconfirm_input.send_keys("123password")

returning_customer_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input') #returning cutsomer Login button XPATH //*[@id="content"]/div/div[2]/div/form/input
returning_customer_btn.click()
wd_wait = WebDriverWait(driver, 10)
returning_customer_btn = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'login')]")))


driver.quit()
