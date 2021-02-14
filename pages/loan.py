from time import sleep

from selenium.webdriver.common.by import By

from common.base import Base


class Loan(Base):
    loan_tab_locator = (By.XPATH, "//*[contains(text(),'借贷')]")

    #借贷数量
    borrow_amount_locator = (By.CSS_SELECTOR, "[class^='input-item']:nth-child(1) [role='spinbutton']")
    #借贷币种
    borrow_coin_locator = (By.CSS_SELECTOR,"[class^='input-item']:nth-child(1) .ant-select-selector")
    #借贷币种列表
    borrow_coin_list_locator = "[class^='input-item']:nth-child(1) .ant-select-item-option-content"
    #质押币种
    collateral_coin_locator = (By.CSS_SELECTOR,"[class^='input-item']:nth-child(2) .ant-select-selector")
    # 质押币种列表
    collateral_coin_list_locator = "[class^='input-item']:nth-child(2) .ant-select-item-option-content"
    #开始借币按钮
    start_borrow_button_locator = (By.CSS_SELECTOR,"[class*='loan-form-wrap'] .ant-btn.ant-btn-primary")
    #确认订单popup上按键
    test= (By.CSS_SELECTOR,'[class^="confirm-modal-wrap" ] [class^="title"]')
    #我已同意选框
    # agree_checkbox_locator= (By.CSS_SELECTOR,"[class^='agreement'] input:nth-of-type(1)")
    agree_checkbox_locator = (By.CSS_SELECTOR,'[class^="confirm-modal-wrap" ] label>span:nth-of-type(1)')
    #协议关闭按钮
    close_agreement_locator = (By.CSS_SELECTOR,'#MainContent>div:nth-of-type(4) .ant-modal-close')
    #确定按钮
    confirm_button_locator = (By.CSS_SELECTOR,".ant-modal-footer .submit_btn")
    #操作成功或失败title
    operation_success_locator = (By.CSS_SELECTOR,".ant-modal-confirm-title")
    #操作失败内容
    operation_fail_content_locator = (By.CSS_SELECTOR,".ant-modal-confirm-content")
    #操作成功知道了按钮
    known_button_locator = (By.CSS_SELECTOR,".ant-modal-confirm-btns>.ant-btn-primary")

    # 借贷详情入口
    positions_locator = (By.CSS_SELECTOR, '[class*="position-link"]')

    # 借贷历史入口
    history_locator = (By.CSS_SELECTOR, '[class^="history-link"]')
    # 借贷历史表格
    history_table_locator = (By.CSS_SELECTOR, '.ant-table-tbody')
    #第一列展开button
    first_expand_button_locator = (By.CSS_SELECTOR,'.ant-table-tbody button:nth-of-type(1)')
    #第一列展开的详细信息
    first_row_details_locator = 'tr.ant-table-expanded-row [class^="item"]'


    def switch_to_loan(self):
        self.wait_element(self.loan_tab_locator).click()

    def create_loan(self):
        self.wait_element(self.borrow_amount_locator).send_keys("20000")
        self.wait_element(self.borrow_coin_locator).click()
        borrow_coin_list = self.wait_elements(self.borrow_coin_list_locator)
        for i in borrow_coin_list:
            print(i.text)
            if i.text == 'USDT':
                i.click()
        self.wait_element(self.collateral_coin_locator).click()
        collateral_coin_list = self.wait_elements(self.collateral_coin_list_locator)
        for i in collateral_coin_list:
            print(i.text)
            if i.text == 'BTC':
                i.click()
        self.wait_element(self.start_borrow_button_locator).click()
        print(self.wait_element(self.test).text)
        self.wait_element(self.agree_checkbox_locator).click()
        self.wait_element(self.confirm_button_locator).click()
        # self.wait_element(self.close_agreement_locator).click()
        try:
            if self.wait_element(self.operation_success_locator).text =="操作成功":
                print("pass")
                self.wait_element(self.known_button_locator).click()
            elif (self.wait_element(self.operation_success_locator).text == "操作失败") and (self.wait_element(self.operation_fail_content_locator).text == "质押物价值已发生变化，请重新借贷"):
                self.refresh_page()
                self.create_loan()
        except:
            print("error")


    def check_loan_history(self):
        self.wait_element(self.history_locator).click()
        self.wait_element(self.first_expand_button_locator).click()
        first_row_details = self.wait_elements(self.first_row_details_locator)
        print(first_row_details[0].text.split("："))
        assert first_row_details[0].text.split("：")[0] == "借贷币种"
        assert first_row_details[0].text.split("：")[1] == "USDT"
        dict_details = {}
        for i in first_row_details:
            dict_details[i.text.split("：")[0]] = i.text.split("：")[1]
        print(dict_details)
