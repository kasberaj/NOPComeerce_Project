import time

from PageObjects.LogInPage import Login
from Utilities.ReadConfig import ReadConfig


class Test_LogIn:
    Username = ReadConfig.get_username()
    Password = ReadConfig.get_password()

    def test_log_in_002(self, setup, get_data_for_login):  #
        self.driver = setup
        self.LP = Login(self.driver)

        # ===  For Login By Params ===
        self.LP.enter_emai_id(get_data_for_login[0])
        self.LP.enter_password(get_data_for_login[1])

        # ===  For Login By Config ===
        # self.LP.enter_emai_id(self.Username)
        # self.LP.enter_password(self.Password)

        self.LP.click_on_login_button()
        time.sleep(10)
        if self.LP.check_login_status() == 1:

            self.driver.save_screenshot("C:\\Users\\Raj\\PycharmProjects\\NOPCOM\\ScreenShots\\test_log_in_002passed"
                                        ".png")

            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Raj\\PycharmProjects\\NOPCOM\\ScreenShots\\test_log_in_002failed"
                                        ".png")
            assert False
