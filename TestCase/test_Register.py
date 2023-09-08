import time

from PageObjects.RegisterPage import Register
from Utilities.Logger import LogGenerator


class Test_Register:
    log = LogGenerator.loggen()

    def test_register_001(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

        self.R = Register(self.driver)

        self.log.info("select Gender")
        self.R.click_on_gender()

        self.log.info("Enter first name")
        self.R.enter_first_name('Raj')
        self.log.info("Enter last name")
        self.R.enter_last_name('Kasbe')
        self.log.info("select DOB day")
        self.R.select_dob_day(2)
        self.log.info("select DOB month")
        self.R.select_dob_month(4)
        self.log.info("select DOB year")
        self.R.select_dob_day('12')
        self.log.info("enter Email")
        self.R.enter_email('therajkasbe@gmail.com')

        self.log.info("Enter Company Name ")
        self.R.enter_company_name('Dazzling House Detailing')
        self.log.info("Enter Pasword ")
        self.R.enter_password('Kasbe@1997')
        self.log.info("Enter Password to Confirm ")
        self.R.enter_confirmed_password('Kasbe@1997')

        self.log.info("Click on Register button")
        self.R.click_on_register()
        # time.sleep(5)
        if self.R.check_status() == 1:

            assert True
        else:
            self.log.info("Taking SS if tCase Failed")

            self.driver.save_screenshot("C:\\Users\\Raj\\PycharmProjects\\NOPCOM\\ScreenShots\\test_register_001_failed.png")
            assert False
