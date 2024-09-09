from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    filter = (By.XPATH, "//select[@class='product_sort_container']")
    prod1 = (By.NAME, "add-to-cart-sauce-labs-onesie")
    prod2 = (By.NAME, "add-to-cart-sauce-labs-fleece-jacket")


    def filt_products(self):
        return self.driver.find_element(*ProductPage.filter)

    def add_product1(self):
        return self.driver.find_element(*ProductPage.prod1)

    def add_product2(self):
        return self.driver.find_element(*ProductPage.prod2)