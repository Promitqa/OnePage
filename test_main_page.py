from main_page import MainPage

import random

string = 'https://spb.restate.ru/choice/petersburg/owners_flats_sale?x'
random_number = random.randint(1, 9)
result = string.replace("x", str(random_number))
print(result)


def test_guest_can_go_to_login_page(browser):  # НУЖНЫЕ ТЕСТОВЫЕ ДАННЫЕ
    page = MainPage(browser, result)
    page.open()
    page.login_popup()


def test_guest_can_go_to_login_page_vk(browser):   # НУЖНЫЕ ТЕСТОВЫЕ ДАННЫЕ В ВК
    page = MainPage(browser, result)
    page.open()
    page.login_vk()


def test_guest_region_page(browser):
    page = MainPage(browser, result)
    page.open()
    page.item_region()


def test_banner_place(browser):  # проверяет наличие места под баннер
    page = MainPage(browser, result)
    page.open()
    page.banner_place()


def test_search_form(browser):
    page = MainPage(browser, result)
    page.open()
    page.search_form()


def test_form_podbor(browser):  # сделан до перехода на расширенную форму - нужна проверка по урлу
    page = MainPage(browser, result)
    page.open()
    page.search_form()


def test_max_price(browser):
    page = MainPage(browser, result)
    page.open()
    page.max_price()


def test_find_spec_add(browser):
    page = MainPage(browser, result)
    page.open()
    page.find_spec_add()


def test_find_ipoteka_link(browser):
    page = MainPage(browser, result)
    page.open()
    page.find_ipoteka_link()


def test_find_button(browser):
    page = MainPage(browser, result)
    page.open()
    page.find_element_button()


def test_find_checkbox(browser):
    page = MainPage(browser, result)
    page.open()
    page.find_checkbox()


def test_find_complecks_place(browser):  # проверяет наличие место под комплексы и кликает на 1
    page = MainPage(browser, result)
    page.open()
    page.find_complecks_place()


def test_find_map_place(browser):  # проверяет наличие места
    page = MainPage(browser, result)
    page.open()
    page.find_map_place()


def test_number_phone(browser):  # проверяет маску телефона и кликабельность
    page = MainPage(browser, result)
    page.open()
    page.number_phone()


def test_check_subscription_popup(browser):  # чек подписки в попапе
    page = MainPage(browser, result)
    page.open()
    page.check_subscription_popup()


def test_check_subscription_hand_popup(browser):
    page = MainPage(browser, result)
    page.open()
    page.check_subscription_hand_popup()


def test_check_noindex_num(browser):  # число объявлений в шапке профиля
    page = MainPage(browser, result)
    page.open()
    page.check_noindex_num()


def test_check_header_count(browser):  # число объявлений на подборке
    page = MainPage(browser, result)
    page.open()
    page.check_noindex_num()
