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

# Wait for the dashboard to load
dashboard = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dashboard__EmployeeDistributionBySubunit"))
)

# Navigate to the PIM module
pim_module = driver.find_element(By.ID, "menu_pim_viewPimModule")
pim_module.click()

# Click on the Employee List
employee_list = driver.find_element(By.ID, "menu_pim_viewEmployeeList")
employee_list.click()

# Select a specific employee record
employee_record = driver.find_element(By.XPATH, "//a[contains(text(),'John Doe')]")
employee_record.click()

# Update contact details
contact_details = driver.find_element(By.ID, "sidenav_employee_details")
contact_details.click()

# Update phone number
phone_number = driver.find_element(By.ID, "contact_emp_mobile")
phone_number.clear()
phone_number.send_keys("1234567890")

# Update email address
email_address = driver.find_element(By.ID, "contact_emp_work_email")
email_address.clear()
email_address.send_keys("john.doe@example.com")

# Save the changes
save_button = driver.find_element(By.ID, "btnSave")
save_button.click()

# Close the browser
driver.quit()
