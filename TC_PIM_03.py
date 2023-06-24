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

# Wait for the Admin menu option to be visible and click it
admin_menu = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "menu_admin_viewAdminModule"))
)
admin_menu.click()

# Wait for the PIM menu option to be visible and click it
pim_menu = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "menu_pim_viewPimModule"))
)
pim_menu.click()

# Validate the menu options are displayed on the PIM page
menu_options = driver.find_elements(By.CSS_SELECTOR, ".menu")
if len(menu_options) > 0:
    print("Menu options are displayed on the PIM page")
else:
    print("Menu options are not displayed on the PIM page")

# Click the +Add button on the PIM page
add_button = driver.find_element(By.ID, "btnAdd")
add_button.click()

# Toggle the "Create login details" checkbox and fill in the mandatory fields
create_login_details = driver.find_element(By.ID, "chkLogin")
create_login_details.click()

# Fill in the mandatory fields
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("John")
last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Doe")
employee_id = driver.find_element(By.ID, "employeeId")
employee_id.send_keys("12345")

# Select the "Enabled" radio button
enabled_radio = driver.find_element(By.CSS_SELECTOR, "input[name='status'][value='Enabled']")
enabled_radio.click()

# Click the Save button
save_button = driver.find_element(By.ID, "btnSave")
save_button.click()

# Check if the page has moved to the Employee List
employee_list_header = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".head h1"))
)
if employee_list_header.text == "Employee Information":
    print("Employee created successfully. Page moved to Employee List")
else:
    print("Employee creation failed")

# Close the browser
driver.quit()
