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
    EC.presence_of_element_located((By.ID, "dashboard__EmployeeDistributionWidget"))
)

# Navigate to the PIM module
pim_module = driver.find_element(By.ID, "menu_pim_viewPimModule")
pim_module.click()

# Click on Employee List
employee_list = driver.find_element(By.ID, "menu_pim_viewEmployeeList")
employee_list.click()

# Select an employee record
employee_record = driver.find_element(By.XPATH, "//a[contains(text(),'John Doe')]")
employee_record.click()

# Click on Tax Exemptions
tax_exemptions = driver.find_element(By.ID, "sidenav-menu-item-taxExemptions")
tax_exemptions.click()

# Fill in Federal Income Tax details
federal_income_tax_status = driver.find_element(By.ID, "taxExempt_federalStatus")
federal_income_tax_status.send_keys("Single")
federal_income_tax_exceptions = driver.find_element(By.ID, "taxExempt_federalExceptions")
federal_income_tax_exceptions.send_keys("2")

# Fill in State Income Tax details
state_income_tax_state = driver.find_element(By.ID, "taxExempt_state")
state_income_tax_state.send_keys("California")
state_income_tax_status = driver.find_element(By.ID, "taxExempt_stateStatus")
state_income_tax_status.send_keys("Married")
state_income_tax_exceptions = driver.find_element(By.ID, "taxExempt_stateExceptions")
state_income_tax_exceptions.send_keys("1")
state_income_tax_work_state = driver.find_element(By.ID, "taxExempt_workState")
state_income_tax_work_state.send_keys("California")

# Save the tax exemptions details
save_button = driver.find_element(By.ID, "btnSaveTaxExempt")
save_button.click()

# Toggle the Direct Deposit Details
direct_deposit_toggle = driver.find_element(By.ID, "directDepositToggle")
direct_deposit_toggle.click()

# Validate the visibility of the fields
direct_deposit_fields = driver.find_elements(By.CLASS_NAME, "direct-deposit-field")
if len(direct_deposit_fields) > 0:
    print("Direct Deposit Details fields are visible")
else:
    print("Direct Deposit Details fields are not visible")

# Save the changes
save_button = driver.find_element(By.ID, "btnSaveDirectDeposit")
save_button.click()

# Close the browser
driver.quit()
