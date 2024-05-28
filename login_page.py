from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = 'username'
        self.password_locator = 'password'
        self.submitButton_locator = '//button[@type="submit"]'

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_locator).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.submitButton_locator).click()
