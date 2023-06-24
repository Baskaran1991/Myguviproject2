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

# Wait for the PIM menu option to be visible
pim_menu = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "menu_pim_viewPimModule"))
)

# Click on the PIM menu option
pim_menu.click()

# Wait for the Employee List menu option to be visible
employee_list_menu = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "menu_pim_viewEmployeeList"))
)

# Click on the Employee List menu option
employee_list_menu.click()

# Validate the presence of menu options on the Employee List page
menu_options = [
    "Personal Details",
    "Contact Details",
    "Emergency Contacts",
    "Dependents",
    "Immigration",
    "Job",
    "Salary",
    "Tax Exemptions",
    "Report-to",
    "Qualifications",
    "Memberships"
]

for option in menu_options:
    option_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, option))
    )
    print(f"{option} is present on the Employee List page")

# Close the browser
driver.quit()
