from time import sleep

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

i_known_button = (By.XPATH,"//*[@class='ant-modal-footer']/*[contains(@class,'ant-btn-primary')]")
personal_identify = (By.XPATH,'//span[contains(text(),"个人认证")]/..')

buy = (By.XPATH,"(//div[starts-with(@class,'dasboard-status')])[2]")

#添加交易对按钮
add_pair = (By.XPATH,"//div[@class='un-draggable']")
first_pair = (By.XPATH,"//div[@class='body']/div/div[1]")
delete_button_on_pop = (By.CLASS_NAME,"ant-modal-close-icon")

def wait_element(dr,locator):
    wait = WebDriverWait(dr,10)
    return wait.until(EC.visibility_of_element_located(locator))


print("aaa")
from selenium import webdriver

driver = webdriver.Chrome()
# js= 'window.localStorage.setItem("Authorization","Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhpQWFXS2Fmb1k2R3FZUFhJR3F0eGhKaktkbDVZZ3lUQ1U5UzFQLUVfQncifQ.eyJqdGkiOiJpQVN5cjlBRkhJfjBXRE9OaWMzVUgiLCJzdWIiOiIwMDAwMDAzNzA2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5hbWJlcmFpbnNpZGVyLmNvbSIsImlhdCI6MTYxMDY4MTg5MCwiZXhwIjoxNjEwNzY4MjkwLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIG9mZmxpbmVfYWNjZXNzIiwiYXVkIjoiQXBvbGxvIn0.YjinEn6iWa8exJXMxW06qaQURDXU_FSgTiusdUvV8DMGgWta6WGOmaZcmkZDg99vi7BY-Ns6bNdf2J2ReSJjb4ZdXa00n0zUK1qVnDaBkeKQBaWyf7PcRtmU5a9GaaOJgtk2HCSkOInXgK5JqkJjXiDakbDzpFvGiFWiBlJadKnlegueYdo0VuJ0f67XPw2dRHlger7d5UrYtdP2y--8YM-gjZLp7o2C51khLnEXNFX3P_icY9xRLgoD-aSm6SJQtmCr2WMx2ZYtK2N783f2A894oNwdbfRJPW2EHFk4fWPENer-aL8GJUjZxxbrZC8-_sJFCubmSatWwnalCqdqYQ")'
# driver.execute_script((js))
# driver.get("http://test.apollo.amberainsider.com/")
# url = "http://test.apollo.amberainsider.com/client/earn"
# driver.get(url)
# driver.implicitly_wait(20)
# driver.get("http://test.apollo.amberainsider.com/")

# headers = {
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhpQWFXS2Fmb1k2R3FZUFhJR3F0eGhKaktkbDVZZ3lUQ1U5UzFQLUVfQncifQ.eyJqdGkiOiJpQVN5cjlBRkhJfjBXRE9OaWMzVUgiLCJzdWIiOiIwMDAwMDAzNzA2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5hbWJlcmFpbnNpZGVyLmNvbSIsImlhdCI6MTYxMDY4MTg5MCwiZXhwIjoxNjEwNzY4MjkwLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIG9mZmxpbmVfYWNjZXNzIiwiYXVkIjoiQXBvbGxvIn0.YjinEn6iWa8exJXMxW06qaQURDXU_FSgTiusdUvV8DMGgWta6WGOmaZcmkZDg99vi7BY-Ns6bNdf2J2ReSJjb4ZdXa00n0zUK1qVnDaBkeKQBaWyf7PcRtmU5a9GaaOJgtk2HCSkOInXgK5JqkJjXiDakbDzpFvGiFWiBlJadKnlegueYdo0VuJ0f67XPw2dRHlger7d5UrYtdP2y--8YM-gjZLp7o2C51khLnEXNFX3P_icY9xRLgoD-aSm6SJQtmCr2WMx2ZYtK2N783f2A894oNwdbfRJPW2EHFk4fWPENer-aL8GJUjZxxbrZC8-_sJFCubmSatWwnalCqdqYQ',
#     'Connection': 'keep-alive',
#     'Host': 'services.test.apollo.amberainsider.com',
#     # 'machindCode': 'f4426c6ff662bdcf0fe4e7c90f369b3d',
#     'Origin': 'http://test.apollo.amberainsider.com',
#     'Referer': 'http://test.apollo.amberainsider.com/client/earn',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     'x-locale': 'zh-CN'
# }

# cap = DesiredCapabilities.CHROME.copy()
#
# for key,value in headers.items():
#     cap['chrome.page.customHeaders.{}'.format(key)] = value

# browser = webdriver.Chrome(desired_capabilities=cap)
# 进入浏览器设置
# options = webdriver.ChromeOptions()
# # 设置中文
# # options.add_argument('lang=zh_CN.UTF-8')
# # 更换头部
# options.add_argument('Authorization="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhpQWFXS2Fmb1k2R3FZUFhJR3F0eGhKaktkbDVZZ3lUQ1U5UzFQLUVfQncifQ.eyJqdGkiOiJpQVN5cjlBRkhJfjBXRE9OaWMzVUgiLCJzdWIiOiIwMDAwMDAzNzA2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5hbWJlcmFpbnNpZGVyLmNvbSIsImlhdCI6MTYxMDY4MTg5MCwiZXhwIjoxNjEwNzY4MjkwLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIG9mZmxpbmVfYWNjZXNzIiwiYXVkIjoiQXBvbGxvIn0.YjinEn6iWa8exJXMxW06qaQURDXU_FSgTiusdUvV8DMGgWta6WGOmaZcmkZDg99vi7BY-Ns6bNdf2J2ReSJjb4ZdXa00n0zUK1qVnDaBkeKQBaWyf7PcRtmU5a9GaaOJgtk2HCSkOInXgK5JqkJjXiDakbDzpFvGiFWiBlJadKnlegueYdo0VuJ0f67XPw2dRHlger7d5UrYtdP2y--8YM-gjZLp7o2C51khLnEXNFX3P_icY9xRLgoD-aSm6SJQtmCr2WMx2ZYtK2N783f2A894oNwdbfRJPW2EHFk4fWPENer-aL8GJUjZxxbrZC8-_sJFCubmSatWwnalCqdqYQ"')
# browser = webdriver.Chrome(chrome_options=options)
# url = "http://test.apollo.amberainsider.com/client/earn"
# driver.get(url)随着功能越来越多，回归的压力越来越大，
# driver.get("http://test.apollo.amberainsider.com/")
driver.get("http://beta.apollo.amberainsider.com/")
# driver.get("http://alpha.pro.ambergroup.io/client/eaas")
# driver.get("http://amberotc.com")
# print(driver.title)
# driver.delete_all_cookies()
# sleep(5)
# driver.find_element_by_link_text("去登录").click()
# sleep(2)
# driver.find_element_by_id("input-id").send_keys("janeyzhou@qq.com")
# driver.find_element_by_id("mask-pwd").send_keys("janeyzhou333")
# driver.find_element_by_id("loginBtn").click()
# #
# sleep(5)
# driver.find_element_by_css_selector("#root > section > header > ul > li.ant-menu-item.ant-menu-item-selected > span").click()
# print(driver.get_cookies())
# print("...............")
# print(driver.get_log)


# for entry in driver.get_log('performance'):
#     print(entry)
# wait_element(driver,personal_identify).click()
# driver.find_element_by_id("username").send_keys("zhenni")
# driver.find_element_by_id("IDNumber").send_keys("123234234543234565")
# driver.find_element_by_xpath("//*[contains(@class,'ant-btn-primary')]").click()

# driver.find_element_by_xpath("//*[@class='ant-modal-footer']/*[contains(@class,'ant-btn-primary')]").click()

#打开添加交易对，再关闭
# driver.find_element_by_xpath("//div[@class='un-draggable']").click()
# driver.find_element_by_xpath("//div[@class='body']/div/div[1]/img").click()
# driver.find_element_by_class_name("ant-modal-close-x").click()


# wait_element(driver,buy).click()
# radio = (By.XPATH,"//*[contains(text(),'市价')]")
# confirm_button = (By.XPATH,'//*[contains(text(),"确 认")]/..')
# count = (By.XPATH,"//*[contains(@class,'ant-input-number-lg')]/*[contains(@class,'ant-input-number-input-wrap')]/input")
# wait_element(driver,radio).click()
# wait_element(driver,count).clear()
# wait_element(driver,count).send_keys("2")
# wait_element(driver,confirm_button).click()

# waiting_list_locator = (By.XPATH,"//ul[@class='order-list']")
# waiting_list = wait_element(driver,waiting_list_locator)
# print(type(waiting_list))
# print(waiting_list.text)
# # context = waiting_list.find_element_by_xpath("//*[starts-with(@class,'order-status-desc')]").text
# context_locator = (By.XPATH,"//*[starts-with(@class,'order-status-desc')]")
# context = wait_element(waiting_list,context_locator).text
# kind = waiting_list.find_element_by_xpath("//*[starts-with(@class,'currency')]").text
# count_list = waiting_list.find_element_by_xpath("//*[starts-with(@class,'item-value')]").text
# method = waiting_list.find_element_by_xpath("//*[starts-with(@class,'item-label')]").text
# print(context)
# print(kind)
# print(count_list)
# print(method)
#买入

# driver.find_element_by_xpath("(//div[@class='radio-item___HauBo'])[2]").click()
