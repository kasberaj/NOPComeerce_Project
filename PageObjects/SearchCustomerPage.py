from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Search_Customer:

    Email = (By.XPATH, "//input[@id='SearchEmail']")
    FirstName = (By.XPATH, "//input[@id='SearchFirstName']")
    LastName = (By.XPATH, "//input[@id='SearchLastName']")
    DobMonthSelect = (By.XPATH, "//select[@id='SearchMonthOfBirth']")
    DobDaySelect = (By.XPATH, "//select[@id='SearchDayOfBirth']")

    RegistrationDateFrom = (By.XPATH, "//input[@id='SearchRegistrationDateFrom']")
    RegistrationDateTo = (By.XPATH, "//input[@id='SearchRegistrationDateTo']")

    LastActiveFrom = (By.XPATH, "//input[@id='SearchLastActivityFrom']")
    LastActiveTo = (By.XPATH, "//input[@id='SearchLastActivityTo']")
    Company = (By.XPATH, "//input[@id='SearchCompany']")
    IpAddress = (By.XPATH, "// input[ @ id = 'SearchIpAddress']")
    CustomerRoleDeselect = (By.XPATH, "// span[ @ title = 'delete']")
    CustomerRoleSelect = (By.XPATH, "//div[@role='listbox']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,5)

    def enter_email(self, email):
        self.driver.find_element(*Search_Customer.Email).send_keys(email)

    def