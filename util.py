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
        self.input = json.load(open('input.json'))

    def login(self):
        self.driver.get(config.baseURL)
        page_loc = self.locator['loginPage']
        self.driver.find_element(By.XPATH, value=page_loc['email']).send_keys(config.username + Keys.TAB)
        self.driver.find_element(By.XPATH, value=page_loc['password']).send_keys(config.password + Keys.TAB)
        self.driver.find_element(By.XPATH, value=page_loc['btnLogin']).click()

    def validateElement(self, locator):
        return self.driver.find_element(By.XPATH, value=locator)

    def openInventory(self):
        self.login()
        self.driver.find_element(By.XPATH, value=self.locator['landingPage']['inventory']).click()

    def createProduct(self):
        self.openInventory()
        self.driver.find_element(By.XPATH, value=self.locator['inventoryPage']['menuProducts']).click()
        self.driver.find_element(By.XPATH, value=self.locator['inventoryPage']['optProducts']).click()

        assert self.validateElement(self.locator['productsPage']['pageHeading'])
        self.driver.find_element(By.XPATH, value=self.locator['productsPage']['createProd']).click()
        self.driver.find_element(By.XPATH, value=self.locator['newProdPage']['newProdPage']). \
            send_keys(self.input['createProduct']['name'])
