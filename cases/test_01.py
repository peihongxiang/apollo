from time import sleep

import pytest

from pages import login
from selenium import webdriver

from pages.earn import Earn
from pages.loan import Loan
from pages.login import Login
from pages.trade import Trade
from pages.earn import Earn

driver = webdriver.Chrome()
@pytest.fixture()
def setup():
    driver.implicitly_wait(20)
    driver.get("http://test.apollo.amberainsider.com/")
    driver.maximize_window()
    login_page = Login(driver)
    trade_page = Trade(driver)
    earn_page = Earn(driver)
    loan_page = Loan(driver)
    yield login_page,trade_page,earn_page,loan_page
    # driver.quit()

class TestLogin():
    # self.driver = webdriver.Chrome()
    #
    # @pytest.fixture()
    # def setup():
    #     driver.implicitly_wait(20)
    #     driver.get("http://test.apollo.amberainsider.com/")
    #     driver.maximize_window()
    #     login_page = Login(driver)
    #     trade_page = Trade(driver)
    #     earn_page = Earn(driver)
    #     yield login_page, trade_page, earn_page
    #     # driver.quit()
    # def test_login(self,setup):
        # login_page,trade_page,earn_page = setup
        # login_page.login()
        # sleep(10)
        # trade_page.add_currency()
        # trade_page.create_market_order()
        # trade_page.verify_market_order()
        # trade_page.close_position()

    # def test_earn(self,setup):
    #     login_page, trade_page, earn_page = setup
    #     login_page.login()
    #     sleep(10)
    #     earn_page.switch_to_earn()
    #     earn_page.create_flexible_deposits()
    #     # earn_page.check_positions()
    #     earn_page.check_investment_history()

    def test_loan(self,setup):
        login_page, trade_page, earn_page, loan_page = setup
        login_page.login()
        sleep(10)
        loan_page.switch_to_loan()
        # loan_page.create_loan()
        # earn_page.check_positions()
        loan_page.check_loan_history()



#
# if __name__ == "__main__":
#
#     a = TestLogin()
#     a.test_login()




