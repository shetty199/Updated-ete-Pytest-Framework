import inspect
import logging

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjectModel.RulePage import RulePage


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_element_presence(self,text):
        checkbox = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,text)))
        if not checkbox.is_selected():
            checkbox.click()

    def hover(self,locator):
        element_to_hover = self.driver.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger