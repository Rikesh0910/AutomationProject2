from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.NAME, "firstName")
    last_name = (By.NAME, "lastName")
    zip_code = (By.NAME, "postalCode")
    submit = (By.XPATH, "//input[@type='submit']")
    total = (By.XPATH, "//div[@class='summary_total_label']")
    finish = (By.XPATH, "//button[text()='Finish']")
    end_text = (By.CSS_SELECTOR, "div[class='complete-text']")
    return_home = (By.NAME, "back-to-products")

    def fill_checkout_form(self, firstname, lastname, zipcode):
        self.driver.find_element(*CheckoutPage.first_name).send_keys(firstname)
        self.driver.find_element(*CheckoutPage.last_name).send_keys(lastname)
        self.driver.find_element(*CheckoutPage.zip_code).send_keys(zipcode)
        return self.driver

    def submit_form(self):
        return self.driver.find_element(*CheckoutPage.submit)

    def get_total(self):
        return self.driver.find_element(*CheckoutPage.total)

    def complete_purchase(self):
        return self.driver.find_element(*CheckoutPage.finish)

    def final_text(self):
        return self.driver.find_element(*CheckoutPage.end_text)

    def return_to_homepage(self):
        return self.driver.find_element(*CheckoutPage.return_home)
