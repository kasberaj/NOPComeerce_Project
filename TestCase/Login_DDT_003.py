import time

from PageObjects.LogInPage import Login
from Utilities import xlutils
from Utilities.ReadConfig import ReadConfig


class Test_LogIn_DDT_003:
    Username = ReadConfig.get_username()
    Password = ReadConfig.get_password()
    path = "C:\\Users\\Raj\\PycharmProjects\\NOPCOM\\TestData\\Nop_Login_Data.xlsx"

    def test_log_in_DDT_003(self, setup):  # get_data_for_login
        self.driver = setup
        self.LP = Login(self.driver)

        self.row = xlutils.rowCount(self.path, 'Sheet1')

        for r in range(2, self.row + 1):
            self.username = xlutils.readData(self.path, 'Sheet1', 'r', 1)
            self.password = xlutils.readData(self.path, 'Sheet1', 'r', 2)
            self.exp_result = xlutils.readData(self.path, 'Sheet1', 'r', 3)

            self.LP.enter_emai_id(self.username)
            self.LP.enter_password(self.password)

            self.LP.click_on_login_button()
            time.sleep(10)
            if self.driver.title == "nopCommerce demo store. Password Recovery":


                self.driver.save_screenshot(
                    "C:\\Users\\Raj\\PycharmProjects\\NOPCOM\\ScreenShots\\test_log_in_002passed"
                    ".png")
                self.LP.click_on_logout_button()


                assert True
            else:
                self.driver.save_screenshot(
                    "C:\\Users\\Raj\\PycharmProjects\\NOPCOM\\ScreenShots\\test_log_in_002failed"
                    ".png")
                assert False
