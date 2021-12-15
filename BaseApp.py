from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс
    """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10):
        """
        Поиск элемента на странице
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Нет такого локатора: {locator}")

    def go_to_site(self):
        print('Переходим на сайт: ', self.base_url)
        return self.driver.get(self.base_url)

