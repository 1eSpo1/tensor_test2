from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


class SearchLocators:
    LOCATOR_PICTURE_BUTTON = (By.LINK_TEXT, 'Картинки')
    LOCATOR_CATEGORY_NAME = (By.CLASS_NAME, "PopularRequestList-SearchText")
    LOCATOR_CATEGORY = (By.CSS_SELECTOR, '[class="PopularRequestList-Shadow"]')
    LOCATOR_SEARCH_RESULT = (By.CSS_SELECTOR, '[name="description"]')
    LOCATOR_FIRST_PICTURE = (By.CSS_SELECTOR, '[class="serp-item__link"]')
    LOCATOR_ATTRIBUTE_OF_PICTURE = (By.CSS_SELECTOR, '[class="MMImage-Origin"]')
    LOCATOR_FIELD_OF_PICTURE = (By.CSS_SELECTOR, '[class="MMImageWrapper"]')
    LOCATOR_NEXT_BUTTON = (By.CSS_SELECTOR, '[class="CircleButton CircleButton_type_next CircleButton_type MediaViewer-Button MediaViewer-Button_hovered MediaViewer_theme_fiji-Button MediaViewer-ButtonNext MediaViewer_theme_fiji-ButtonNext"]')
    LOCATOR_PREV_BUTTON = (By.CSS_SELECTOR, '[class="CircleButton CircleButton_type_prev CircleButton_type MediaViewer-Button MediaViewer_theme_fiji-Button MediaViewer-ButtonPrev MediaViewer_theme_fiji-ButtonPrev"]')

class PicturesHelper(BasePage):
    """
    Производный класс от базового класса BasePage
    Реализация функций для test.py
    """
    def images_exists(self):
        BasePage.find_element(self, SearchLocators.LOCATOR_PICTURE_BUTTON)
        print('Ссылка Картинки присутсвтует на странице')


    def current_url(self):
        """
        Проверка на верный URL
        """
        urlis = self.driver.current_url
        neededurl = "https://yandex.ru/images/"
        if neededurl in urlis:
            print('Перешли на верный URL')
        else:
            print('Не тот URL')

    def category_is_right(self, category_name, search_result):
        """
        :param category_name: название категории
        :param search_result: что отображается в поисковой строке
        Проверяет совпадение параметров
        """
        if category_name in search_result:
            print('В поиске верный текст')
        else:
            print('Текст поиска не совпадает с категорией')

    def picture_is_open(self):
        """
        Проверяет открытие каритнки
        """
        elem = self.driver.find_element(By.CSS_SELECTOR,
                                   '[class="Link Link_theme_normal MMOrganicSnippet-Title MMSidebar-SectionTitle"]').get_attribute(
            "textContent")
        if elem != 0:
            print('Картинка открылась.', '\nЗаголовок картинки:', elem)
        else:
            print('Картинка не открылась')

    def switch_link(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def click_on_pictures_button(self):
        time.sleep(5)
        return self.find_element(SearchLocators.LOCATOR_PICTURE_BUTTON).click()

    def get_category_name(self):
        self.category_name = self.find_element(SearchLocators.LOCATOR_CATEGORY_NAME).get_attribute("textContent")
        return self.category_name

    def click_on_category(self):
        time.sleep(5)
        return self.find_element(SearchLocators.LOCATOR_CATEGORY).click()

    def get_search_result(self):
        self.search_result = self.find_element(SearchLocators.LOCATOR_SEARCH_RESULT).get_attribute("content")
        return self.search_result

    def click_on_picture(self):
        time.sleep(5)
        return self.find_element(SearchLocators.LOCATOR_FIRST_PICTURE).click()

    def get_attribute_of_picture(self):
        time.sleep(5)
        return self.find_element((SearchLocators.LOCATOR_ATTRIBUTE_OF_PICTURE)).get_attribute("src")

    def click_on_next_button(self):
        """
        Наводит курсор на поле картинки для появлнеия кликабельного элемента.
        :return: производит клик по элементу
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(SearchLocators.LOCATOR_FIELD_OF_PICTURE))
        actions.perform()
        time.sleep(5)
        return self.find_element(SearchLocators.LOCATOR_NEXT_BUTTON).click()

    def click_on_prev_button(self):
        time.sleep(5)
        return self.find_element(SearchLocators.LOCATOR_PREV_BUTTON).click()

    def is_picture_equal(self, src1, src2):
        assert src1 == src2, 'Это разные картинки'
        return print('Это то же изображение')



