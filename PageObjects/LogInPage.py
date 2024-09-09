from selenium.webdriver.common.by import By


class LogInPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "input[class='submit-button btn_action']")

    def get_name(self):
        return self.driver.find_element(*LogInPage.username)

    def get_pass(self):
        return self.driver.find_element(*LogInPage.password)

    def sel_login(self):
        return self.driver.find_element(*LogInPage.login_button)