from selenium.webdriver.support.wait import WebDriverWait
import logging
import random
import string
import time
from datetime import datetime


from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def return_text(self, locator):
        exp_wait = WebDriverWait(self.driver, 20, 1)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        return web_ele.text

    def click_element(self, locator):
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        web_ele.click()

    def javascripit_click(self, locator):
        exp_wait = WebDriverWait(self.driver, 5, 1)
        web_ele = exp_wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", web_ele)

    def move_to_element(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.move_to_element(web_ele).perform()

    def right_click(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.context_click(web_ele).perform()

    def double_click(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.double_click(web_ele).perform()

    def click_and_hold(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.click_and_hold(web_ele).perform()
    def drag_and_drop(self,src,tar):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        src_ele= exp_wait.until(EC.presence_of_element_located(src))
        tar_ele = exp_wait.until(EC.presence_of_element_located(tar))
        mouse_act.drag_and_drop(src_ele,tar_ele).perform()
    def send_keys(self, locator, text):
        exp_wait = WebDriverWait(self.driver, 5, 1)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        web_ele.clear()
        web_ele.send_keys(Keys.CONTROL + 'a')
        web_ele.send_keys(Keys.DELETE)
        self.driver.execute_script("arguments[0].value ='';", web_ele)
        web_ele.send_keys(text)

    def send_keys_file(self,locator, text):
        exp_wait = WebDriverWait(self.driver, 5, 1)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        web_ele.send_keys(text)


    def move_by_offset(self,locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 5, 1)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        mouse_act.move_by_offset(80,0).click().perform()

    def get_webtable_rows(self, locator):
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        list = web_ele.find_elements(locator[0], locator[1])
        return len(list)