from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base import Base


class Login(Base):
    # login_link = (By.XPATH,"//*[starts-with(@class,'login-tips')]/a")
    # username = (By.ID, "basic_email")
    # password = (By.ID, "basic_password")
    # login_button = (By.CSS_SELECTOR,".ant-btn.ant-btn-primary")
    login_link = (By.LINK_TEXT, "登录")

    username = (By.ID, "input-id")
    password = (By.ID, "mask-pwd")
    login_button = (By.ID, "loginBtn")


    def login(self):
        # 登录
        self.wait_element(self.login_link).click()
        sleep(2)
        self.wait_element(self.username).send_keys("janeyzhou@qq.com")
        self.wait_element(self.password).send_keys("123456")
        self.wait_element(self.login_button).click()
        # driver.find_element_by_id("input-id").send_keys("janeyzhou@qq.com")
        # driver.find_element_by_id("mask-pwd").send_keys("janeyzhou333")
        # driver.find_element_by_id("loginBtn").click()




