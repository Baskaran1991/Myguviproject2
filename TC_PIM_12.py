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

# Wait for the PIM menu to load and click on it
pim_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu_pim_viewPimModule")))
pim_menu.click()

# Click on the Employee List submenu
employee_list_submenu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu_pim_viewEmployeeList")))
employee_list_submenu.click()

# Select an employee record
employee_record = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//table[@id='resultTable']/tbody/tr[1]/td[3]/a")))
employee_record.click()

# Click on the Salary tab
salary_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sidenav-salary")))
salary_tab.click()

# Go to the Assigned Salary Components section
assigned_salary_components = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu_salary_assignSalaryComponents")))
assigned_salary_components.click()

# Click on the +Add link
add_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "addSalaryComponentButton")))
add_link.click()

# Fill in the salary component details
salary_component_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "salary_component_name")))
salary_component_input.send_keys("Basic Salary")
pay_grade_input = driver.find_element(By.ID, "pay_grade")
pay_grade_input.send_keys("Grade A")
pay_frequency_input = driver.find_element(By.ID, "pay_frequency")
pay_frequency_input.send_keys("Monthly")
currency_input = driver.find_element(By.ID, "currency_id")
currency_input.send_keys("USD")
amount_input = driver.find_element(By.ID, "amount")
amount_input.send_keys("5000")

# Click the Save button
save_button = driver.find_element(By.ID, "btnSaveSalaryComponent")
save_button.click()

# Close the browser
driver.quit()
