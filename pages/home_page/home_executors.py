from ..common_page.common_executors import CommonPage
from .home_locators import HomePageLocators

class HomePage(CommonPage, HomePageLocators):
    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def get_header(self):
        login_form = self.driver.find_element(*self.HEADER)
        return login_form.text