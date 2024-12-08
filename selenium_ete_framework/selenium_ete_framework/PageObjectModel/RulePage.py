from selenium.webdriver.common.by import By

class RulePage:
    def __init__(self,driver):
        self.driver=driver

    create_rule=(By.XPATH, '//*[@id="addnew"]/span/em')
    rule_name=(By.ID, "rulestp_name")
    rule_desc=(By.ID, "rulestp_desc")
    #hover_on_rule=(By.XPATH,"//*[@id='print__screen']/kl-pages/kl-left-side-bar/div/ul/div[2]/li[10]/div/div[1]/img")
    condition=(By.XPATH,"//*[@id='code-editor']/div/div/div[1]/div[2]/div[1]/div[4]")
    save_proc=(By.XPATH,"//*[@id='print__screen']/kl-pages/kl-settings/kl-rule-conf/kl-rule-engine-config/div/div/div/div[2]/button[2]")
    expand_condition=(By.XPATH,"//*[@id='rule_header10']/span")

    def create_rules(self):
        return self.driver.find_element(*RulePage.create_rule)

    def rule_name_textfield(self):
        return self.driver.find_element(*RulePage.rule_name)

    def rule_descscription(self):
        return self.driver.find_element(*RulePage.rule_desc)
    # def hover_on_rules(self):
    #     return self.driver.find_element(*RulePage.hover_on_rule)

    def condition_field(self):
        return self.driver.find_element(*RulePage.condition)

    def expand_cond(self):
        return self.driver.find_element(*RulePage.expand_condition)