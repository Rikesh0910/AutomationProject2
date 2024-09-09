from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    access_cart = (By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    checkout_cart = (By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button ']")

    def go_to_cart(self):
        return self.driver.find_element(*CartPage.access_cart)

    def cart_checkout(self):
        return self.driver.find_element(*CartPage.checkout_cart)