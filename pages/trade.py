from selenium.webdriver.common.by import By

from common.base import Base


class Trade(Base):
    #添加交易对
    add_symbol_locator = (By.XPATH,"//div[@class='un-draggable']")
    first_symbol_locator = (By.XPATH,"//div[@class='body']/div/div[1]/img")
    # first_symbol_locator = (By.XPATH, "(//*[starts-with(@class,'currency')])[1]")
    close_symbol_locator = (By.CLASS_NAME,"ant-modal-close-x")


    #添加订单
    #第一对币种的买
    first_buy = (By.XPATH, "(//div[starts-with(@class,'dasboard-status')])[2]")
    #市价选项
    market_price_option = (By.XPATH,"//*[contains(text(),'市价')]")
    #确认按钮
    # confirm_button = (By.XPATH, '//*[contains(text(),"确 认")]/..')
    confirm_button = (By.CSS_SELECTOR, ".justify-end button:nth-child(2)")
    #买入数量
    count = (By.XPATH,"(//*[contains(@class,'ant-input-number-lg')]/*[contains(@class,'ant-input-number-input-wrap')]/input)[1]")

    #活跃订单
    waiting_list_locator = (By.XPATH, "//ul[@class='order-list']")
    #活跃订单中的限价委托字样
    limit_context = (By.XPATH,"//*[starts-with(@class,'order-status-desc')]")
    #活跃订单中的币对
    wait_currency=(By.XPATH,"//*[starts-with(@class,'currency')]")
    #活跃订单中的买卖方向
    wait_direction = (By.XPATH,"//*[starts-with(@class,'item-label')]")
    #活跃订单中的数量
    wait_count = (By.XPATH,"//*[starts-with(@class,'item-value')]")

    #平仓按钮
    close_position_button = (By.XPATH,"//*[contains(@class,'ant-btn mr-2 ant-btn-sm')]")
    #取消平仓
    close_cancell = (By.XPATH,"//*[contains(text(),'取')]")
    #确认平仓
    # close_confirm = (By.XPATH, "//*[contains(text(),'确')]")
    close_confirm = (By.XPATH,"//*[contains(@class,'ant-btn w-24 ant-btn-primary ant-btn-sm')]")


    #当前仓位列表
    current_position_list = (By.XPATH,"//*[@class='ant-table-tbody']")
    current_directon = (By.XPATH,"//*[@class='ant-table-tbody']/tr/td[3]")
    def add_currency(self):
        self.wait_element(self.add_symbol_locator).click()
        self.wait_element(self.first_symbol_locator).click()
        self.wait_element(self.close_symbol_locator).click()
    #创建市价单
    def create_market_order(self):
        self.wait_special_element("(//div[starts-with(@class,'dasboard-status')])[2]")
        # self.wait_element(self.first_buy).click()
        self.wait_element(self.market_price_option).click()
        self.wait_element(self.confirm_button).click()
    #验证
    def verify_market_order(self):
        assert self.wait_element(self.current_directon).text == '买'
    #平仓
    def close_position(self):
        self.wait_element(self.close_position_button).click()
        # self.wait_element(self.close_cancell).click()
        self.wait_element(self.close_confirm).click()



