from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
# To use the Python Selenium Selector you have to use the By class
from selenium.webdriver.common.by import By


class Baskar:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = 'Admin'
    password = 'admin123'
    # username_locator is a TagName
    username_locator = 'username'
    # password_locator is a TagName
    password_locator = 'password'
    # Submit Button Locator as XPATH
    submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    # Startup method for the CRM application
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # Method for login into the CRM application
    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitBox_locator).click()


Baskar().Browsing()

Baskar().login()

# Wait for the PIM module to be visible and click on it
pim_module = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "menu_pim_viewPimModule"))
)
pim_module.click()

# Click on the Employee List option
employee_list = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "menu_pim_viewEmployeeList"))
)
employee_list.click()

# Select an employee record (replace 'employee_id' with the actual ID of the employee)
employee_id = "12345"
employee_record = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, f"//a[text()='{employee_id}']"))
)
employee_record.click()

# Click on the Edit button for the Emergency Contact Details section
edit_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "btnSaveEContact"))
)
edit_button.click()

# Update the emergency contact details
name_input = driver.find_element(By.ID, "emgcontacts_name")
name_input.clear()
name_input.send_keys("John Doe")

relationship_input = driver.find_element(By.ID, "emgcontacts_relationship")
relationship_input.clear()
relationship_input.send_keys("Spouse")

home_telephone_input = driver.find_element(By.ID, "emgcontacts_homePhone")
home_telephone_input.clear()
home_telephone_input.send_keys("1234567890")

mobile_input = driver.find_element(By.ID, "emgcontacts_mobilePhone")
mobile_input.clear()
mobile_input.send_keys("9876543210")

work_telephone_input = driver.find_element(By.ID, "emgcontacts_workPhone")
work_telephone_input.clear()
work_telephone_input.send_keys("5555555555")

# Save the updated details
save_button = driver.find_element(By.ID, "btnSaveEContact")
save_button.click()

# Verify that the updated details are displayed correctly on the Emergency Contact Details page
updated_name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "emgcontacts_name"))
).get_attribute("value")

updated_relationship = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "emgcontacts_relationship"))
).get_attribute("value")

updated_home_telephone = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "emgcontacts_homePhone"))
).get_attribute("value")

updated_mobile = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "emgcontacts_mobilePhone"))
).get_attribute("value")

updated_work_telephone = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "emgcontacts_workPhone"))
).get_attribute("value")

# Close the browser
driver.quit()
