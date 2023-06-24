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

# Validate search text box
search_box = driver.find_element(By.ID, "searchSystemUser_userName")
if search_box.is_displayed():
    print("Search text box is displayed successfully")
else:
    print("Search text box is not displayed")

# Click on search button
search_button = driver.find_element(By.ID, "searchBtn")
search_button.click()

# Validate menu items
menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
for item in menu_items:
    menu_item = driver.find_element(By.LINK_TEXT, item)
    if menu_item.is_displayed():
        print(f"{item} menu item is displayed successfully")
    else:
        print(f"{item} menu item is not displayed")

# Click on Admin page
admin_page = driver.find_element(By.LINK_TEXT, "Admin")
admin_page.click()

# Click on Users under User Management
users_link = driver.find_element(By.LINK_TEXT, "Users")
users_link.click()

# Validate User Role dropdown
user_role_dropdown = Select(driver.find_element(By.ID, "searchSystemUser_userType"))
if user_role_dropdown.is_displayed():
    print("User Role dropdown is displayed successfully")
else:
    print("User Role dropdown is not displayed")

# Validate Status dropdown
status_dropdown = Select(driver.find_element(By.ID, "searchSystemUser_status"))
if status_dropdown.is_displayed():
    print("Status dropdown is displayed successfully")
else:
    print("Status dropdown is not displayed")

# Get the values in User Role dropdown
user_role_options = [option.text for option in user_role_dropdown.options]
print("User Role options:", user_role_options)

# Get the values in Status dropdown
status_options = [option.text for option in status_dropdown.options]
print("Status options:", status_options)

# Close the browser
driver.quit()
