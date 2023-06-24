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

# Wait for the dashboard page to load
dashboard = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dashboard"))
)

# Navigate to the PIM module
pim_module = driver.find_element_by_id("pim")
pim_module.click()

# Click on Employee List
employee_list = driver.find_element_by_id("employee_list")
employee_list.click()

# Select an employee record
employee_record = driver.find_element_by_xpath("//table[@id='employee_table']/tbody/tr[1]")
employee_record.click()

# Click on Edit button to update dependents details
edit_button = driver.find_element_by_id("editBtn")
edit_button.click()

# Update the dependents details (Name, Relationship, Date of Birth)
dependent_name = driver.find_element_by_id("dependent_name")
dependent_relationship = driver.find_element_by_id("dependent_relationship")
dependent_dob = driver.find_element_by_id("dependent_dob")

dependent_name.clear()
dependent_name.send_keys("John Doe")

dependent_relationship.clear()
dependent_relationship.send_keys("Spouse")

dependent_dob.clear()
dependent_dob.send_keys("01/01/1990")

# Save the details
save_button = driver.find_element_by_id("saveBtn")
save_button.click()

# Verify the updated details in the Emergency Contact Details page
emergency_contact_details = driver.find_element_by_id("emergency_contact_details")
assert "John Doe" in emergency_contact_details.text
assert "Spouse" in emergency_contact_details.text
assert "01/01/1990" in emergency_contact_details.text

# Close the browser
driver.quit()
