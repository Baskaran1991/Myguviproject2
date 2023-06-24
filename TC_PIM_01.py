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
search_box = driver.find_element(By.ID, "searchBox")
if search_box.is_displayed():
    print("Search text box is displayed successfully.")
else:
    print("Search text box is not displayed.")

# Validate menu items
menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
for item in menu_items:
    menu_item = driver.find_element(By.LINK_TEXT, item)
    if menu_item.is_displayed():
        print(f"{item} menu item is displayed successfully.")
    else:
        print(f"{item} menu item is not displayed.")

# Close the browser
driver.quit()
