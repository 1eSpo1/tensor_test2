from PageObject import PicturesHelper

"""
Файл для тестирования.
Определения функций в PageObject.py
"""

def test_yandex_pictures(browser):
    yandex_main_page = PicturesHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.images_exists()
    yandex_main_page.click_on_pictures_button()
    yandex_main_page.switch_link()
    yandex_main_page.current_url()
    name_of_category = yandex_main_page.get_category_name()
    yandex_main_page.click_on_category()
    search_result = yandex_main_page.get_search_result()
    yandex_main_page.category_is_right(name_of_category, search_result)
    yandex_main_page.click_on_picture()
    yandex_main_page.picture_is_open()
    src1 = yandex_main_page.get_attribute_of_picture()
    yandex_main_page.click_on_next_button()
    yandex_main_page.click_on_prev_button()
    src2 = yandex_main_page.get_attribute_of_picture()
    yandex_main_page.is_picture_equal(src1, src2)





