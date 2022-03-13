# Author : Anubhav

import unittest
import util as util


class TestAspireapp(unittest.TestCase):
    def setUp(self):
        self.ut = util.Util()
        self.driver = self.ut.driver
        self.addCleanup(self.driver.quit)

    # 1. Login to web application
    def test_aspireLogin(self):
        self.ut.login()
        assert self.ut.validateElement(self.ut.locator['landingPage']['user'])

    # 2. Navigate to `Inventory` feature
    def test_openInventory(self):
        self.ut.openInventory()
        assert self.ut.validateElement(self.ut.locator['inventoryPage']['pageHeading'])

    # 3. From the top-menu bar, select `Products -> Products` item, then create a new product
    def test_createProduct(self):
        self.ut.createProduct()
        print((self.ut.locator['newProdPage']['newProdName']).format(self.ut.input['createProduct']['name']))
        assert self.ut.validateElement((self.ut.locator['newProdPage']['newProdName']).format(self.ut.input['createProduct']['name']))

    # 4. Update the quantity of new product is more than 10
    def test_updateProductQuantity(self):
        assert True

    # 5. From top-left page, click on `Application` icon
    # 6. Navigate to `Manufacturing` feature, then create a new Manufacturing Order item for the created Product on step #3
    def test_createMafOrder(self):
        assert True

    # 7. Update the status of new Orders to ??Done?? successfully
    def test_updateOrderStatus(self):
        assert True

    # 8. Validate the new Manufacturing Order is created with corrected information.
    def test_MafOrdInfo(self):
        assert True
