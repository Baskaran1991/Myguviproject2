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
dashboard_title = "Dashboard - OrangeHRM"
WebDriverWait(driver, 10).until(EC.title_contains(dashboard_title))

# Go to PIM module
pim_menu = driver.find_element(By.ID, "menu_pim_viewPimModule")
pim_menu.click()

# Click on Employee List
employee_list_link = driver.find_element(By.ID, "menu_pim_viewEmployeeList")
employee_list_link.click()

# Select an employee record
employee_checkbox = driver.find_element(By.XPATH, "//input[@name='chkSelectRow[]'][1]")
employee_checkbox.click()

# Click on Job Details
job_details_button = driver.find_element(By.ID, "btnJobDetails")
job_details_button.click()

# Click on Employee Termination/Activation Link
termination_activation_link = driver.find_element(By.LINK_TEXT, "Employee Termination/Activation")
termination_activation_link.click()

# Click on Active Employment button
active_employment_button = driver.find_element(By.ID, "btnActivate")
active_employment_button.click()

# Validate that the employee's job is activated
status_message = driver.find_element(By.ID, "terminationStatus")
assert "Activated" in status_message.text

# Close the browser
driver.quit()
