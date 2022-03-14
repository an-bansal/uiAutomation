# Author: Anubhav
import json
import logging
# import os
import time

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

    def getElement(self, loc):
        return self.driver.find_element(By.XPATH, value=loc)

    def login(self):
        self.driver.get(config.baseURL)
        self.getElement(self.locator['loginPage']['email']).send_keys(config.username + Keys.TAB)
        self.getElement(self.locator['loginPage']['password']).send_keys(config.password + Keys.TAB)
        self.getElement(self.locator['loginPage']['btnLogin']).click()
        logging.info('Login successful')

    def openInventory(self):
        self.login()
        self.getElement(self.locator['landingPage']['inventory']).click()

    def createProduct(self):
        self.openInventory()
        self.getElement(self.locator['inventoryPage']['menuProducts']).click()
        self.getElement(self.locator['inventoryPage']['optProducts']).click()

        assert self.validateElement(self.locator['productsPage']['pageHeading'])
        self.getElement(self.locator['productsPage']['createProd']).click()
        self.input['createProduct']['name'] += str(int(time.time()))
        self.getElement(self.locator['prodInfoPage']['pageHeading']). \
            send_keys(self.input['createProduct']['name'])
        self.getElement(self.locator['prodInfoPage']['btnSave']).click()
        logging.info('Created Product : ' + self.input['createProduct']['name'])

    def updateQty(self):
        self.createProduct()
        self.getElement(self.locator['inventoryPage']['menuProducts']).click()
        self.getElement(self.locator['inventoryPage']['optProducts']).click()
        self.getElement(self.locator['productsPage']['searchBox']). \
            send_keys(self.input['createProduct']['name'] + Keys.RETURN)
        time.sleep(1)  # to handle late loading
        self.getElement(self.locator['productsPage']['firstRes']).click()
        self.getElement(self.locator['prodInfoPage']['updateQty']).click()
        time.sleep(1)
        self.getElement(self.locator['prodInfoPage']['createQty']).click()
        self.getElement(self.locator['prodInfoPage']['countedQty']).send_keys(Keys.BACKSPACE * 5)
        self.getElement(self.locator['prodInfoPage']['countedQty']).send_keys(self.input['updateQty']['qty'])
        self.getElement(self.locator['prodInfoPage']['saveQty']).click()

    def createMafOrd(self):
        self.updateQty()
        self.getElement(self.locator['landingPage']['appList']).click()
        self.getElement(self.locator['landingPage']['manufacturing']).click()
        assert self.validateElement(self.locator['mafOrdPage']['pageHeading'])

        self.getElement(self.locator['mafOrdPage']['crtMfaOrd']).click()
        # self.getElement(self.locator['mafOrdPage']['prdName']).send_keys(self.input['createProduct']['name'])
        self.driver.find_element(By.CSS_SELECTOR, value=self.locator['mafOrdPage']['prdName']). \
            send_keys(self.input['createProduct']['name'] + "1647253955")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, value=self.locator['mafOrdPage']['prdName']).send_keys(Keys.TAB)
        self.getElement(self.locator['mafOrdPage']['prdQty']).send_keys(Keys.BACKSPACE)
        self.getElement(self.locator['mafOrdPage']['prdQty']).send_keys(self.input['updateQty']['qty'])
        self.getElement(self.locator['mafOrdPage']['btnConfirm']).click()

    def updateOrdStatus(self):
        # self.createMafOrd()
        self.openInventory()
        self.getElement(self.locator['landingPage']['appList']).click()
        self.getElement(self.locator['landingPage']['manufacturing']).click()
        assert self.validateElement(self.locator['mafOrdPage']['pageHeading'])

        self.getElement(self.locator['mafOrdPage']['btnMKD']).click()
        self.getElement(self.locator['mafOrdPage']['btnOk']).click()
        time.sleep(10)

    def validateElement(self, locator):
        return self.getElement(locator)

    def validateTextInElement(self, locator, text):
        capTxt = self.getElement(locator).text
        logging.info("Captured Text : " + capTxt + " & Comparison Text : " + text)
        return self.getElement(locator).text == text
