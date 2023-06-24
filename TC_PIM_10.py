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
pim_module = driver.find_element_by_id("menu_pim_viewPimModule")
pim_module.click()

# Click on the Employee List
employee_list = driver.find_element_by_id("menu_pim_viewEmployeeList")
employee_list.click()

# Select an employee record
employee_record = driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr[1]/td[1]/input")
employee_record.click()

# Click on the Job details
job_details = driver.find_element_by_id("btnJobDetails")
job_details.click()

# Click on the Employee Termination/Activation Link
termination_link = driver.find_element_by_id("btnTerminateEmployment")
termination_link.click()

# Fill in the Termination Date, Termination Reason, and Note
termination_date = driver.find_element_by_id("terminationDate")
termination_date.send_keys("2022-12-31")
termination_reason = driver.find_element_by_id("terminationReason")
termination_reason.send_keys("Resignation")
note = driver.find_element_by_id("note")
note.send_keys("Employee decided to pursue other opportunities")

# Click on the Terminate Employee Button
terminate_button = driver.find_element_by_id("btnTerminate")
terminate_button.click()

# Wait for the details to be saved
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "activationEmployment"))
)

# Verify that the Activation Employment is visible
activation_employment = driver.find_element_by_id("activationEmployment")
if activation_employment.is_displayed():
    print("Employee termination successful. Activation Employment is visible.")
else:
    print("Employee termination failed. Activation Employment is not visible.")

# Close the browser
driver.quit()
