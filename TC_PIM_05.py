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


# Navigate to Employee List page
employee_list_link = driver.find_element_by_id("menu_pim_viewEmployeeList")
employee_list_link.click()

# Fill out employee details
employee_name = driver.find_element_by_id("firstName")
employee_name.send_keys("John")
employee_id = driver.find_element_by_id("employeeId")
employee_id.send_keys("12345")
employment_status = driver.find_element_by_id("employmentStatus")
employment_status.send_keys("Full Time")
supervisor_name = driver.find_element_by_id("supervisorName")
supervisor_name.send_keys("Jane Doe")
job_title = driver.find_element_by_id("jobTitle")
job_title.send_keys("Software Engineer")
personal_details = driver.find_element_by_id("personalDetails")
personal_details.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

# Click save button
save_button = driver.find_element_by_id("btnSave")
save_button.click()

# Validate filled details are present
wait = WebDriverWait(driver, 10)
validation_message = wait.until(EC.visibility_of_element_located((By.ID, "validationMessage")))
if validation_message.text == "Details saved successfully.":
    print("Employee details saved successfully.")
else:
    print("Failed to save employee details.")

# Close the browser
driver.quit()
