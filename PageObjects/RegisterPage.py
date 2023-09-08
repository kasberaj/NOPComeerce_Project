import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Register:
    GenderClick = (By.XPATH, "//input[@id='gender-male']")
    FirstNameEnter = (By.XPATH, "//input[@id='FirstName']")
    LastnameEnter = (By.XPATH, "//input[@id='LastName']")
    DOBDaySelect = (By.XPATH, "//select[@name='DateOfBirthDay']")
    DOBMonthSelect = (By.XPATH, "//select[@name='DateOfBirthMonth']")
    DOBYearSelect = (By.XPATH, "//select[@name='DateOfBirthYear']")

    EmailEnter = (By.XPATH, "//input[@id='Email']")
    CompanyNameEnter = (By.XPATH, "//input[@id='Company']")
    PasswordEnter = (By.XPATH, "/html[1]/body[1]/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[2]/div[1]/input[1]")
    ConfirmedPasswordEnter = (By.XPATH, "/html[1]/body[1]/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[2]/div[2]/input[1]")

    RegisterClick = (By.XPATH, "//button[@id='register-button']")
    SuccessfulStatus = (By.XPATH, "//a[@class='button-1 register-continue-button']")

    # = (By.XPATH, ""
    # = (By.XPATH, ""
    # = (By.XPATH, ""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click_on_gender(self):
        self.driver.find_element(*Register.GenderClick).click()

    def enter_first_name(self, fname):
        self.driver.find_element(*Register.FirstNameEnter).send_keys(fname)

    def enter_last_name(self, lname):
        self.driver.find_element(*Register.LastnameEnter).send_keys(lname)

    def select_dob_day(self, day):
        Day = Select(self.driver.find_element(*Register.DOBDaySelect))
        Day.select_by_index(day)

    def select_dob_month(self, month):
        Month = Select(self.driver.find_element(*Register.DOBMonthSelect))
        Month.select_by_index(month)

    def select_dob_year(self, year):
        Year = Select(self.driver.find_element(*Register.DOBYearSelect))
        Year.select_by_index(year)

    def enter_email(self, email):
        self.driver.find_element(*Register.EmailEnter).send_keys(email)

    def enter_company_name(self, cname):
        self.driver.find_element(*Register.CompanyNameEnter).send_keys(cname)

    def enter_password(self, passwd):
        self.driver.find_element(*Register.PasswordEnter).send_keys(passwd)

    def enter_confirmed_password(self, conpasswd):
        self.driver.find_element(*Register.ConfirmedPasswordEnter).send_keys(conpasswd)

    def click_on_register(self):
        self.driver.find_element(*Register.RegisterClick).click()

    def check_status(self):
        try:
            self.wait = WebDriverWait(self.driver, 15)
            self.driver.find_element(*Register.SuccessfulStatus)
            return 1
        except:

            return 0
