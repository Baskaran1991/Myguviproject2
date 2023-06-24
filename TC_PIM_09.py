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

# Update Job Details
join_date = driver.find_element_by_id("join_date")
join_date.clear()
join_date.send_keys("2022-01-01")

job_title = driver.find_element_by_id("job_title")
job_title.clear()
job_title.send_keys("Software Engineer")

job_category = driver.find_element_by_id("job_category")
job_category.clear()
job_category.send_keys("IT")

job_specification = driver.find_element_by_id("job_specification")
job_specification.clear()
job_specification.send_keys("Python Developer")

sub_unit = driver.find_element_by_id("sub_unit")
sub_unit.clear()
sub_unit.send_keys("Development")

location = driver.find_element_by_id("location")
location.clear()
location.send_keys("New York")

# Save the details
save_button = driver.find_element_by_id("save_button")
save_button.click()

# Verify the updated details in the Emergency Contact Details page
emergency_contact_details = driver.find_element_by_id("emergency_contact_details")
emergency_contact_details.click()

# Assert the updated job details are present
assert join_date.get_attribute("value") == "2022-01-01"
assert job_title.get_attribute("value") == "Software Engineer"
assert job_category.get_attribute("value") == "IT"
assert job_specification.get_attribute("value") == "Python Developer"
assert sub_unit.get_attribute("value") == "Development"
assert location.get_attribute("value") == "New York"

# Close the browser
driver.quit()
