import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Раздел «Лента заказов»")
class TestOrderFeed:

    @allure.title("Счётчик Выполнено за всё время увеличивается после создания заказа")
    def test_total_orders_counter_increases_after_creating_order(self, login_user):
        main_page = MainPage(login_user)
        order_page = OrderPage(login_user)

        main_page.wait_for_page_to_load()

        main_page.click_on_feed_button()
        order_page.wait_for_order_page_to_load()
        original_total = order_page.get_total_orders_count()

        main_page.click_on_constructor_button()
        main_page.wait_for_page_to_load()

        main_page.drag_ingredient_bun_to_basket()
        main_page.place_order()

        main_page.close_order_success_modal()

        main_page.click_on_feed_button()
        final_total = order_page.get_total_orders_count()

        assert final_total > original_total

    @allure.title("Счётчик Выполнено за сегодня увеличивается после создания заказа")
    def test_today_orders_counter_increases_after_creating_order(self, login_user):
        main_page = MainPage(login_user)
        order_page = OrderPage(login_user)

        main_page.wait_for_page_to_load()

        main_page.click_on_feed_button()
        order_page.wait_for_order_page_to_load()
        original_today = order_page.get_today_orders_count()

        main_page.click_on_constructor_button()
        main_page.wait_for_page_to_load()

        main_page.drag_ingredient_bun_to_basket()
        main_page.place_order()

        main_page.close_order_success_modal()

        main_page.click_on_feed_button()
        final_today = order_page.get_today_orders_count()

        assert final_today > original_today

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_number_appears_in_in_progress_section(self, login_user):
        main_page = MainPage(login_user)
        order_page = OrderPage(login_user)

        main_page.wait_for_page_to_load()

        main_page.drag_ingredient_bun_to_basket()
        main_page.place_order()

        order_number = main_page.get_order_number()
        main_page.close_order_success_modal()

        main_page.click_on_feed_button()
        order_page.wait_for_order_page_to_load()

        order_page.wait_for_orders_in_progress()
        in_progress_number = order_page.get_order_number_in_progress_orders()

        assert order_number == in_progress_number