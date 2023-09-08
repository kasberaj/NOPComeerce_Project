from PageObjects.SearchCustomerPage import Search_Customer


class Test_Search_Customer:

    def test_search_customer_005(self, setup):
        self.driver = setup
        self.SC = Search_Customer(self.driver)