import allure
import pytest

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Основная функциональность")
class TestKeyFunctionality:

    @allure.title("Переход по клику на Конструктор")
    def test_click_on_constructor_button_redirects_to_constructor_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        order_page.open_order_page()
        main_page.wait_for_page_to_load()

        main_page.click_on_constructor_button()

        assert main_page.is_main_page_opened()

    @allure.title("Переход по клику на Лента заказов")
    def test_click_on_feed_button_redirects_to_feed_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.wait_for_page_to_load()

        main_page.click_on_feed_button()

        assert order_page.is_order_page_opened()

    @allure.title("Клик на ингредиент открывает модальное окно")
    def test_click_on_ingredient_opens_modal_window(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.wait_for_page_to_load()

        main_page.click_on_ingredient()

        assert main_page.is_modal_visible()

    @allure.title("Модальное окно закрывается по крестику")
    def test_close_modal_window_with_close_button(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.wait_for_page_to_load()

        main_page.click_on_ingredient()
        main_page.close_ingredient_modal()

        assert main_page.is_modal_closed()

    @allure.title("Счётчик ингредиента увеличивается при добавлении ингредиента в заказ")
    def test_ingredient_counter_increases_by_using_drag_and_drop(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.wait_for_page_to_load()

        original_count = main_page.get_ingredient_counter()

        main_page.click_on_ingredient()
        main_page.drag_ingredient_bun_to_basket()

        final_count = main_page.get_ingredient_counter()

        assert final_count > original_count