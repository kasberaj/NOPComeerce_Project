from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomer:
    AdminUrl = "https://admin-demo.nopcommerce.com/admin/"
    EmailEnter = (By.XPATH, "//input[@id='Email']")
    PasswordEnter = (By.XPATH, "//input[@id='Password']")
    LoginClick = (By.XPATH, "//button[@type='submit']")

    CustomerClick = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    Customers_Click_Again = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    AddNewClick = (By.XPATH, "//a[@class='btn btn-primary']")

    Email = (By.XPATH, "//input[@id='Email']")
    Password = (By.XPATH, "// input[ @ id = 'Password']")
    FirstName = (By.XPATH, "//input[@id='FirstName']")
    LastName = (By.XPATH, "//input[@id='LastName']")

    GenderCheckMale = (By.XPATH, "//input[@id='Gender_Male']")
    GenderCheckFemale = (By.XPATH, "//input[@id='Gender_Female']")
    DobEnter = (By.XPATH, "//input[@id='DateOfBirth']")
    CompanyName = (By.XPATH, "//input[@id='Company']")
    IsTaxCheck = (By.XPATH, "// input[ @ id = 'IsTaxExempt']")
    Newsletter = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card["
                            "1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]")
    NewsletterValue = (By.XPATH, "//li[normalize-space()='Test store 2']")
    CustomerRoleEnter = (By.XPATH, "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-focused "
                                   "k-state-hover k-state-border-down']//div[@role='listbox']")
    DeselectRegistered = (By.XPATH, "//span[@title='delete']")

    GuestClick = (By.XPATH, "//li[@id='4759d749-2c57-4e80-b0e8-a664502e270c']")

    VendorSelect = (By.XPATH, "//select[@id='VendorId']")

    ActiveCheck = (By.XPATH, "//input[@id='Active']//input[@id='SearchRegistrationDateFrom']")
    AdminComment = (By.XPATH, "//textarea[@id='AdminComment']")
    SaveButton = (By.XPATH, "//button[@name='save']//i[@class='far fa-save']")
    SuccessMage = (By.XPATH, "//div[@class='alert alert-success alert-dismissable']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def enter_Email(self, email):
        self.driver.find_element(*AddCustomer.EmailEnter).send_keys(email)

    def enter_Password(self, passwd):
        self.driver.find_element(*AddCustomer.PasswordEnter).send_keys(passwd)

    def click_on_login_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.LoginClick))
        self.driver.find_element(*AddCustomer.LoginClick).click()

    def click_on_Customers(self):
        self.driver.find_element(*AddCustomer.CustomerClick).click()

    def again_click_on_customers(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Customers_Click_Again))
        self.driver.find_element(*AddCustomer.Customers_Click_Again).click()

    def click_on_AddNew(self):
        self.driver.find_element(*AddCustomer.AddNewClick).click()

    def enter_email(self, email):
        self.driver.find_element(*AddCustomer.Email).send_keys(email)

    def enter_password(self, passwd):
        self.driver.find_element(*AddCustomer.Password).send_keys(passwd)

    def enter_First_Name(self, fname):
        self.driver.find_element(*AddCustomer.FirstName).send_keys(fname)

    def enter_Last_Name(self, lname):
        self.driver.find_element(*AddCustomer.LastName).send_keys(lname)

    def select_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(*AddCustomer.GenderCheckMale).click()
        elif gender == 'Female':
            self.driver.find_element(*AddCustomer.GenderCheckFemale).click()
        else:
            self.driver.find_element(*AddCustomer.GenderCheckMale).click()

    def enter_date_of_birth(self, dob):
        self.driver.find_element(*AddCustomer.DobEnter).send_keys(dob)

    def enter_company_name(self, cmpny):
        self.driver.find_element(*AddCustomer.CompanyName).send_keys(cmpny)

    def click_on_istax(self):
        self.driver.find_element(*AddCustomer.IsTaxCheck).click()

    def enter_news_letter(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Newsletter))
        self.driver.find_element(*AddCustomer.Newsletter).click()
        self.driver.find_element(*AddCustomer.NewsletterValue).click()

    def click_on_customer_Role(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.CustomerRoleEnter))
        # self.driver.find_element(*AddCustomer.CustomerRoleEnter).click()
        self.driver.find_element(*AddCustomer.GuestClick).click()
        # self.driver.find_element(*AddCustomer.DeselectRegistered).click()

    def select_vendor(self, vendor):
        # if vendor == 'Vendor 1':
        #     self.wait.until(expected_conditions.visibility_of_element_located(self.VendorSelect))
        #     Vendor = Select(self.driver.find_element(*AddCustomer.VendorSelect))
        #     Vendor.select_by_value('Vendor 1')
        # elif vendor == 'Vendor 2':
        #     self.wait.until(expected_conditions.visibility_of_element_located(self.VendorSelect))
        #     Vendor = Select(self.driver.find_element(*AddCustomer.VendorSelect))
        #     Vendor.select_by_value('Vendor 2')
        # else:

        self.wait.until(expected_conditions.visibility_of_element_located(self.VendorSelect))
        Vendor = Select(self.driver.find_element(*AddCustomer.VendorSelect))
        Vendor.select_by_index(vendor)

    def click_on_active(self):
        self.driver.find_element(*AddCustomer.ActiveCheck).click()

    def enter_admin_comment(self, comment):
        self.driver.find_element(*AddCustomer.AdminComment).send_keys(comment)

    def click_on_save_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.SaveButton))
        self.driver.find_element(*AddCustomer.SaveButton).click()

    def check_success_status(self):

        try:
            self.driver.find_element(*AddCustomer.SuccessMage)
            return 1
        except NoSuchElementException:
            return 0
