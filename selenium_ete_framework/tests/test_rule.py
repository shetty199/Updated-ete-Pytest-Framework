import time
import pytest

from TestData.LoginTestData import LoginTestData
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from PageObjectModel.RulePage import RulePage
from PageObjectModel.LoginPage import LoginPage


class TestRule(BaseClass):
    pass
    # def test_rule(self,getdata):
    #     log=self.getLogger()
    #     time.sleep(4)
    #     # Login
    #     login=LoginPage(self.driver)
    #     log.info("entering the user name")
    #     login.username().send_keys(getdata["User_name"])
    #     login.password1().send_keys(getdata["Password"])
    #     login.log_click().click()
    #     time.sleep(3)
    #     # self.driver.set_window_size(100, 100)
    #     # self.driver.save_screenshot("C://Users//shettappa.chalawadi//PycharmProjects//selenium_ete_framework//screenshots//screenshot.png")
    #     # log.info("screenshot is captured")
    #
    #     #hover.hover_on_rules(self.driver)
    #     element_to_hover = self.driver.find_element(By.XPATH,"//*[@id='print__screen']/kl-pages/kl-left-side-bar/div/ul/div[2]/li[10]/div/div[1]/img")
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element_to_hover).perform()
    #     time.sleep(4)
    #
    #     # Click on the hidden option
    #     element = self.driver.find_element(By.XPATH, "//div[@class='left-side-bar overlay-menu-mobile']/ul/div[2]/li[9]/div/ul/li[10]")
    #     self.driver.execute_script("arguments[0].click();", element)
    #
    #
    #     print(self.driver.title)
    #     log.info("title should be displayed")
    #     time.sleep(3)
    #
    #     # Add new rule
    #     rulepage=RulePage(self.driver)
    #     rulepage.create_rules().click()
    #     time.sleep(3)
    #     rulepage.rule_name_textfield().send_keys("Rule1")
    #     rulepage.rule_descscription().send_keys("desc")
    #     # Wait for the multi-custom-search input
    #     self.wait = WebDriverWait(self.driver, 10)
    #     self.driver.find_element(By.XPATH, '//*[@id="multi_custom_search"]').send_keys(
    #         "Site Rule test>Plant Rule test>Line Rule test>Eq_rule_block_check1")
    #     time.sleep(3)
    #     # Check and select checkbox if not already selected
    #     self.verify_element_presence("#print__screen > kl-pages > kl-settings > kl-rule-conf > kl-rule-engine-config > div > div > div > div.scrollDivContent > div > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > div > kl-custom-multiselect > div > div.col-12.p-0.checkbox-list > div > label > span")
    #     # checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#print__screen > kl-pages > kl-settings > kl-rule-conf > kl-rule-engine-config > div > div > div > div.scrollDivContent > div > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > div > kl-custom-multiselect > div > div.col-12.p-0.checkbox-list > div > label > span")))
    #     # save and proceed
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH,'//*[@id="print__screen"]/kl-pages/kl-settings/kl-rule-conf/kl-rule-engine-config/div/div/div/div[2]/button[2]').click()
    #     time.sleep(5)
    #     rulepage.expand_cond().click()
    #     time.sleep(3)
    #     log.info("expanded")
    #     time.sleep(15)
    #
    #     # Using JavaScript to set the value
    #     # actions = ActionChains(self.driver)
    #     element = self.driver.find_element(By.XPATH, "//div[@class='view-lines']")
    #     self.driver.execute_script("arguments[0].send_keys('concat([Site Rule test>Plant Rule test>Line Rule test>Eq_rule_block_check1:Test_Parameter(Raw)_05],10)');", element)
    #
    #     #self.driver.find_element(By.XPATH,"//div[@class='view-lines']").send_keys("concat([Site Rule test>Plant Rule test>Line Rule test>Eq_rule_block_check1:Test_Parameter(Raw)_05],10)")
    #
    #     # rulepage.condition_field().send_keys("concat([Site Rule test>Plant Rule test>Line Rule test>Eq_rule_block_check1:Test_Parameter(Raw)_05],10)")
    #     time.sleep(20)
    #     log.info("condition is entered in the condition field")
    #
    #
    # @pytest.fixture(params=LoginTestData.test_logdata)
    # def getdata(self,request):
    #     return request.param


import pytest
@pytest.mark.parametrize("input,Expected",[(1,2),(3,4)])
def test_inc(input,Expected):
    assert input+1 == Expected