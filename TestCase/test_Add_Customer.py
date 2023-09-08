import time

from PageObjects.AddCustomePage import AddCustomer
from Utilities.Logger import LogGenerator


class Test_Add_Customer:
    log = LogGenerator.loggen()

    def test_add_customer_004(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.AC = AddCustomer(self.driver)
        self.log.info('Hitting Admin Url')
        self.driver.get(AddCustomer.AdminUrl)
        # self.log.info('Enter Admin Username')
        # self.AC.enter_Email('admin@yourstore.com')
        # self.log.info('Enter Admin Password')
        # self.AC.enter_Email('admin123')
        self.AC.click_on_login_button()
        self.AC.click_on_Customers()
        self.AC.again_click_on_customers()
        self.AC.click_on_AddNew()

        self.log.info('Enter email')
        self.AC.enter_email('rajkasbe21@gmail.com')
        self.log.info('Enter password')
        self.AC.enter_password('Kasbe@1997')
        self.log.info('Enter First_Name')
        self.AC.enter_First_Name('Raj')
        self.log.info('Enter Last_Name')
        self.AC.enter_Last_Name('Kasbe')

        self.AC.select_gender('Male')
        self.AC.enter_date_of_birth('02-04-1997')
        self.AC.enter_company_name('Dazzling House')
        self.AC.click_on_istax()
        self.AC.enter_news_letter()
        # self.AC.click_on_customer_Role()
        self.AC.select_vendor(1)
        # self.AC.click_on_active()
        self.AC.enter_admin_comment('I am the boss')
        self.AC.click_on_save_button()

        if self.AC.check_success_status() == 1:
            self.driver.save_screenshot(
                "C:\\Users\\Raj\\PycharmProjects\\NOPCOM\\ScreenShots\\test_add_customer_004pass.png")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Raj\\PycharmProjects\\NOPCOM\\ScreenShots\\test_add_customer_004fail.png")
            assert False






