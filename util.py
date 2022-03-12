# Author: Anubhav
import json

# from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import config


class Util:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=config.gecodriverpath)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.locator = json.load(open('xpath.json'))

    def login(self):
        self.driver.get(config.baseURL)
        page_loc = self.locator['loginPage']
        self.driver.find_element(By.XPATH, value=page_loc['email']).send_keys(config.username + Keys.TAB)
        self.driver.find_element(By.XPATH, value=page_loc['password']).send_keys(config.password + Keys.TAB)
        self.driver.find_element(By.XPATH, value=page_loc['btnLogin']).click()

    def validateElement(self, locator):
        return self.driver.find_element(By.XPATH, value=locator)
