from time import sleep

from selenium.webdriver.common.by import By

from common.base import Base


class Earn(Base):
    earn_tab_locator = (By.XPATH,"//*[contains(text(),'理财')]")
    #活期tab
    flexible_deposits_locator = (By.CSS_SELECTOR,'.fixed-container .ant-menu-item:nth-child(2)')
    #定期tab
    fixed_deposits_locator = (By.CSS_SELECTOR, '.fixed-container .ant-menu-item:nth-child(4)')
    #结构化tab
    strutured_deposits_locator = (By.CSS_SELECTOR, '.fixed-container .ant-menu-item:nth-child(6)')
    #申购按钮列表
    subscribe_button = (By.CSS_SELECTOR,'.ant-btn')
    #理财名称
    # describe_title_locator = (By.CSS_SELECTOR,'div[class^="title-text"]')
    describe_title_locator = (By.CSS_SELECTOR, "[class^='product-name']")
    available_amount_locator = (By.CSS_SELECTOR,'[class*="balance-warp"]>span:nth-child(2)')
    #申购金额
    describe_mount_locator = (By.CSS_SELECTOR,'input[role="spinbutton"]')
    #确认申购OK按钮
    OK_button_locator = (By.CSS_SELECTOR,'.ant-btn.submit_btn.ant-btn-primary')
    #申购成功OK按钮
    success_OK_button_locator = (By.CSS_SELECTOR,'.ant-modal-body .ant-btn.ant-btn-primary')
    #申购成功信息
    success_describe_msg_locator = (By.CSS_SELECTOR,'.ant-modal-confirm-title')

    #持仓入口
    positions_locator = (By.CSS_SELECTOR,'[class*="position-link"]')

    #理财历史入口
    history_locator = (By.CSS_SELECTOR,'[class*="history-link"]')
    #理财历史表格
    history_table_locator= (By.CSS_SELECTOR,'.ant-table-tbody')
    #理财历史第一行申购记录
    product_title_locator = (By.CSS_SELECTOR,'.ant-table-tbody tr:nth-child(1) td:nth-child(1)')
    product_amount_locator = (By.CSS_SELECTOR,'.ant-table-tbody tr:nth-child(1) td:nth-child(2)')
    operation_locator = (By.CSS_SELECTOR, '.ant-table-tbody tr:nth-child(1) td:nth-child(3)')
    status_locator = (By.CSS_SELECTOR, '.ant-table-tbody tr:nth-child(1) td:nth-child(4)')
    time_locator = (By.CSS_SELECTOR, '.ant-table-tbody tr:nth-child(1) td:nth-child(5)')

    def switch_to_earn(self):
        self.wait_element(self.earn_tab_locator).click()

    def create_flexible_deposits(self):
        #点击活期tab
        self.wait_element(self.flexible_deposits_locator).click()
        sleep(3)
        self.wait_element(self.subscribe_button).click()
        #点击申购按钮
        # for i in self.wait_element(self.subscribe_button):
        #     if i.text =="申购":
        #         i.click()
        #提取理财名称
        self.describe_title = self.wait_element(self.describe_title_locator).text
        print(self.describe_title)
        #输入申购金额
        self.wait_element(self.describe_mount_locator).send_keys("100")
        # subscribe_button = self.wait_element(self.subscribe_button)
        # if subscribe_button.text == "申购":
        #     subscribe_button.click()

        #点击确认申购OK按钮
        self.wait_element(self.OK_button_locator).click()

        #获取申购成功信息
        success_describe_msg = self.wait_element(self.success_describe_msg_locator).text
        assert success_describe_msg == "申购成功"
        #点击申购成功弹出框得OK按钮
        self.wait_element(self.success_OK_button_locator).click()


    def check_positions(self):
        self.wait_element(self.positions_locator).click()
    def check_investment_history(self):
        self.wait_element(self.history_locator).click()
        print(self.wait_element(self.product_title_locator).text)
        assert self.wait_element(self.product_title_locator).text == self.describe_title
        assert "100." in self.wait_element(self.product_amount_locator).text
        assert self.wait_element(self.operation_locator).text == "申购"
        assert self.wait_element(self.status_locator).text == "确认中"