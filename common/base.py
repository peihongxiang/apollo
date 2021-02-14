from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:

    def __init__(self,driver):
        self.driver = driver

    def refresh_page(self):
        self.driver.refresh()

    def wait_element(self,locator):
        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_elements(self,locator):
        while True:
            alist = self.driver.find_elements_by_css_selector(locator)
            if alist:
                break
        return alist

    def wait_special_element(self,locator):
        flag = False
        lasting_time = 0
        while flag==False and lasting_time < 5:
            try:
                a = self.driver.find_element_by_xpath(locator)
                print("已定位到元素")
                a.click()
                print("已点击元素")
                flag = True
            except:
                print("没定位到元素")
                lasting_time += 0.2
                sleep(1)
