from time import sleep

from selenium import webdriver


class LoginPage:

    def login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://test.apollo.amberainsider.com/")
        self.driver.find_element_by_link_text("去登录").click()
        sleep(2)
        self.driver.find_element_by_id("input-id").send_keys("janeyzhou@qq.com")
        self.driver.find_element_by_id("mask-pwd").send_keys("janeyzhou333")
        self.driver.find_element_by_id("loginBtn").click()

