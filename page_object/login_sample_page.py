import allure

from base.base_page import BasePage


class LoginSamplePage(BasePage):
    # URL of login sample page
    url = '/login'

    # Elements locators of login sample page
    username = ('id', 'username')
    password = ('css selector', 'input#password')
    submit = ('xpath', '//button[contains(@type, "submit")]')
    logout = ('css selector', 'a[href*="logout"]')

    def __init__(self, driver):
        super().__init__(driver)

    # Core sub-workflow of sample page
    def login(self, username, password):
        with allure.step('1. Open sample page'):
            self.open(self.url)
        with allure.step('2. Enter username and password'):
            self.enter(self.username, username)
            self.enter(self.password, password)
        with allure.step('3. Click login button'):
            self.click(self.submit)
        with allure.step('4. Login successful'):
            self.wait_for(self.logout)
