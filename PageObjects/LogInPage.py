from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:

    EmailEnter = By.XPATH, "//input[@id='Email']"
    PasswordEnter = By.XPATH, "//input[@id='Password']"
    LoginClick = By.XPATH, "//button[normalize-space()='Log in']"

    LoginStatus = By.XPATH, "//a[@class='ico-logout']"
    LogoutClick = By.XPATH, "//a[@class='ico-logout']"
    # LoginClick = By.XPATH, "//a[@class='ico-login']"
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.implicitly_wait(5)

    def enter_emai_id(self, email):
        self.wait.until(expected_conditions.visibility_of_element_located(self.EmailEnter))
        self.driver.find_element(*Login.EmailEnter).send_keys(email)

    def enter_password(self, passwd):
        self.driver.find_element(*Login.PasswordEnter).send_keys(passwd)

    def click_on_login_button(self):
        self.driver.find_element(*Login.LoginClick).click()

    def click_on_logout_button(self):
        self.driver.find_element(*Login.LogoutClick).click()
    def check_login_status(self):
        try:

            self.driver.find_element(*Login.LoginStatus)
            # self.driver.find_element(*Login.LoginStatus).click()
            # self.driver.find_element(*Login.LoginClick).click()
            return 1
        except NoSuchElementException:


            return 0
