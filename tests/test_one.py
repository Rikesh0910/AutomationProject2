

from PageObjects.CartPage import CartPage
from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.LogInPage import LogInPage
from PageObjects.ProductPage import ProductPage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_login(self):
        #Login Page
        log = self.get_logger()
        log.info("starting test on the initial login")
        login = LogInPage(self.driver)
        login.get_name().send_keys("standard_user")
        login.get_pass().send_keys("secret_sauce")
        login.sel_login().click()
        log.info("logged in")

        #Product Page
        log.info("now filtering products based on low to high(price)")
        product = ProductPage(self.driver)
        self.select_dropdown(product.filt_products(),"lohi")
        log.info("adding product 1")
        product.add_product1().click()
        log.info("adding product 2")
        self.actionsOnElement(self.driver, product.add_product2())

        #Cart Page
        cart = CartPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 0)")
        log.info("now accessing cart!")
        cart.go_to_cart().click()
        self.actionsOnElement(self.driver, cart.cart_checkout())

        #Checkout Page
        checkout = CheckoutPage(self.driver)
        log.info("now filling out form to checkout")
        checkout.fill_checkout_form("Rikesh","Krishna","600093")
        self.actionsOnElement(self.driver, checkout.submit_form())
        total_amt = checkout.get_total().text
        log.info("printing"+ total_amt)
        checkout.complete_purchase().click()
        text_final = checkout.final_text().text
        log.info(text_final)
        assert "Your order has been dispatched" in text_final
        checkout.return_to_homepage().click()