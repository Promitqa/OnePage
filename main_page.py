import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage
from selenium.webdriver.common.by import By

import re


class MainPage(BasePage):
    def login_popup(self):
        time.sleep(20)

        button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, "login")))  # кликаем по иконке в красном меню
        button.click()

        assert self.browser.find_element(By.CLASS_NAME, "login")  # находим попап входа
        # в инпуты вводим логин и пароль
        input1 = self.browser.find_element(By.NAME, "login")
        input1.send_keys("YOUR LOGIN")  # здесь укажи свой логин
        input2 = self.browser.find_element(By.NAME, "password")
        input2.send_keys("YOUR PASSWORD")  # здесь укажи свой пароль
        button2 = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div/form/label[3]/button")
        button2.click()

        time.sleep(15)
        #
        # self.browser.refresh()  # если не отрабатывает, расскоменти и будет обновление страницы
        #
        # time.sleep(10)  # можно добавить еще время ожидания

        WebDriverWait(self.browser, 40).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/header/div[1]/div[1]/div/div/div[2]/div[6]"))).click()  # кликаем по иконке в шапке

        assert self.browser.find_element(
            By.XPATH, "/html/body/div[2]/header/div[1]/div[1]/div/div/div[2]/div[6]/ul/li[1]/a").click()  # проверяем наличие выпадашки и кликаем на 1 строку в ней

    def login_vk(self):
        time.sleep(20)

        button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, "login")))  # кликаем по иконке в шапке
        time.sleep(3)
        button.click()

        self.browser.find_element(By.CLASS_NAME, "popup--login")  # находим попап входа
        button1 = self.browser.find_element(By.CLASS_NAME, "js-vk-login")  # кликаем на лого вк
        button1.click()
        # в инпуты вводим логин и пароль
        input1 = self.browser.find_element(By.NAME, "email")
        input1.send_keys("login")  # здесь укажи свой логин
        input2 = self.browser.find_element(By.NAME, "pass")
        input2.send_keys("password")  # здесь укажи свой пароль
        button = self.browser.find_element(By.ID, "install_allow")
        button.click()

        time.sleep(10)

        WebDriverWait(self.browser, 40).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/header/div[1]/div[1]/div/div/div[2]/div[6]"))).click()

        self.browser.find_element(
            By.XPATH, "/html/body/div[2]/header/div[1]/div[1]/div/div/div[2]/div[6]/ul/li[1]/a").click()

    def item_region(self):
        time.sleep(20)

        button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/header/div[2]/div/ul[2]/li/span")))  # кликаем по региону под шапкой
        button.click()

        elem = self.browser.find_element(By.XPATH, "/html/body/div[2]/noindex/div/div/div[1]/div[1]/a[2]")  # выбираем новый регион
        elem.click()

        time.sleep(5)
        # сравниваем его
        get_title = self.browser.title  # возвращает заголовок в строковом формате
        if "Подмосковье" in get_title:
            pass
        else:
            print("error region")

    def banner_place(self):
        # определяет наличие баннерного места, при отсутсвии = вывод ошибки
        assert self.browser.find_element(By.ID, "rbnr_brandingnewtop"), "Banner place is not presented"

    def search_form(self):
        # проверяем работу формы на страницку
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[1]/div/div/button"))).click()
        elem1 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[1]/div/div/div/ul/li[2]/label/span")
        elem1.click()

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[2]/div/div/button"))).click()
        elem2 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[2]/div/div/div/ul/li[1]/label")
        elem2.click()

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[2]/div[1]/div/div/button"))).click()
        elem3 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[2]/div[1]/div/div/div/ul/li[3]/label")
        elem3.click()

        self.browser.find_element(
             By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[3]/div[2]/div/input[1]")

        input1 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[3]/div/input[2]")
        input1.send_keys("Алтуфьево")

        input2 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[3]/div[2]/div/input[1]")
        input2.send_keys("30")
        input3 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[3]/div[2]/div/input[2]")
        input3.send_keys("60")

        self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[3]/div[4]/button").click()

        time.sleep(5)

        get_title = self.browser.title
        if "Арендовать" and "1 комн" and "Москве" in get_title:
            pass
        else:
            print('error1 title')
            if input2 != 30 and input3 != 60:
                pass
            else:
                print('error2 inputs')

    def search_form_podbor(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[1]/div/div/button"))).click()
        elem1 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[1]/div/div/div/ul/li[2]/label/span")
        elem1.click()

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[2]/div/div/button"))).click()
        elem2 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[2]/div/div/div/ul/li[2]/label")
        elem2.click()

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[2]/div[1]/div/div/button"))).click()
        elem3 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[2]/div[1]/div/div/div/ul/li[7]/label/span")
        elem3.click()

        self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[3]/div[2]/div/input[1]")

        input1 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[3]/div/input[2]")
        input1.send_keys("Алтуфьево")
        elem4 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[1]/div[3]/div/div/div[1]/div")
        elem4.click()

        input3 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[3]/div[2]/div/input[1]")
        input3.send_keys("30")
        input4 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[3]/div[2]/div/input[2]")
        input4.send_keys("60")

        self.browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/form/div[3]/div[3]/a").click()
        # сделан до перехода на расширенную форму - нужна проверка по урлу

    def max_price(self):
        # проверяем соответствие макс цены по отсортированному списку
        assert self.browser.execute_script("window.scrollBy(50, 50);")
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/main/div/div[3]/div[2]/div/div/button"))).click()
        assert self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[3]/div[2]/div/div/div/ul/li[3]/label/span").click()
        assert self.browser.execute_script("window.scrollBy(100, 100);")

        time.sleep(5)

        object1 = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[3]/div[3]/div[1]/div/div[2]/a")
        object1.click()

        assert self.browser.switch_to.window(window_name=self.browser.window_handles[1])

        get_title = self.browser.title
        if "6 000 000" in get_title:
            pass
        else:
            print("error max price")

    def find_spec_add(self):
        # наличие спецов
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/div[3]/span[1]/div/div[1]/div/noindex/div/p')
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/div[3]/span[1]/div/div[2]/div/noindex/div/p"]')
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/div[3]/span[1]/div/div[3]/div/noindex/div/p"]')
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/div[3]/span[2]/div/div[1]/div/noindex/div/p')
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/div[3]/span[2]/div/div[2]/div/noindex/div/p')
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/div[3]/span[2]/div/div[3]/div/noindex/div/p')
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/span/div[1]/div[1]/div/noindex/div/p')
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/span/div[1]/div[2]/div/noindex/div/p')
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/span/div[1]/div[3]/div/noindex/div/p')
        assert self.browser.find_element(
            By.XPATH, '/html/body/div[2]/main/div/div[3]/span/div[1]/div[4]/div/noindex/div/p')

    def find_ipoteka_link(self):
        # работа ссылки на ипотеку
        assert self.browser.execute_script("window.scrollBy(300, 300);")
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(
            (By.ID, "buy_with_a_mortgage_from_lists"))).click()

        assert self.browser.switch_to.window(window_name=self.browser.window_handles[1])

        time.sleep(5)

        get_title = self.browser.title
        assert self.browser.title
        if "вторичка" and "6 000 000" and "Санкт-Петербурге" and "50%" and "20 лет" in get_title:
            pass
        else:
            print("error ipoteks choice")

    def find_element_button(self):
        # обратный звонок
        button = self.browser.find_element(By.CLASS_NAME, "cpopup-btn__label")
        button.click()

        assert self.browser.find_element(By.CLASS_NAME, "cpopup__win")

        input1 = self.browser.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/form/div[1]/input")
        input1.send_keys("111 111 11 11")

    def find_checkbox(self):
        # чекбокс с Даниилом
        time.sleep(10)

        button = self.browser.find_element(By.CLASS_NAME, "trigger-image")
        button.click()
        assert self.browser.find_element(
            By.CLASS_NAME, "relative")

    def find_complecks_place(self):
        # наличие места под комплексы рядом
        element = self.browser.find_element(By.CLASS_NAME, "houses-preview")
        assert self.browser.execute_script("arguments[0].scrollIntoView()", element)

        time.sleep(10)

        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[2]/main/div/div[3]/div[11]/div[2]/div/div[1]/div[6]/a[1]/img"))).click()

    def find_map_place(self):
        # наличие графика
        assert self.browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div[3]/div[16]")

    def number_phone(self):
        # релевантность телефона на объявлениях
        assert self.browser.execute_script("window.scrollBy(200, 200);")

        time.sleep(5)

        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="opened_the_phone_base"]'))).click()

        time.sleep(3)

        num = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((By.ID, 'opened_the_phone_base'))).get_attribute("innerHTML")
        # oриентировано на российские мобильные + городские с кодом из 3 цифр
        r = re.fullmatch('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
                         num)  # вызов функции fullmatch путем передачи шаблона и num
        if r is not None:  # проверяем, нет это или нет
            pass
        else:
            print('Недопустимый номер')

    def check_subscription_popup(self):
        # всплывающая подписка
        time.sleep(60)

        assert self.browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div[3]/div[8]/div")
        input1 = self.browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div[3]/div[8]/div/form/div/input[7]")
        input1.send_keys("velikayaaleksa@yandex.ru")
        button = self.browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div[3]/div[8]/div/form/button")
        button.click()
        message = self.browser.find_element(By. XPATH, "/html/body/div[2]/main/div/div[3]/div[8]/div/p[2]")
        assert "Подписка успешно активирована!" or "Вы уже подписаны на эту страницу" in message.text

    def check_subscription_hand_popup(self):
        # подписка внизу страницы
        assert self.browser.execute_script("window.scrollBy(1200, 1200);")  # РАССЧИТАТЬ ПИКСЕЛЬНЫЙ СКРОЛЛ
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="spiski-link-subscribe"]'))).click()

        assert self.browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div[3]/div[8]/div")
        input1 = self.browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div[3]/div[8]/div/form/div/input[7]")
        input1.send_keys("velikayaaleksa@yandex.ru")
        button = self.browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div[3]/div[8]/div/form/button")
        button.click()
        message = self.browser.find_element(By. XPATH, "/html/body/div[2]/main/div/div[3]/div[8]/div/p[2]")
        assert "Подписка успешно активирована!" or "Вы уже подписаны на эту страницу" in message.text

    def check_noindex_num(self):
        # колличество объявлений в выбранном списке
        text = self.browser.find_element(
            By.XPATH, "/html/body/div[2]/header/div[1]/div[1]/div/div/div[1]/p").get_attribute(
            "innerText")
        s1 = "".join(c for c in text if c.isdecimal())
        num1 = int(s1)
        num2 = 100000
        try:
            if num1 <= num2:
                print('noindex number < 100 000')
        finally:
            pass

    def check_header_count(self):
        # колличество объявлений в ноиндексе в шапке
        text = self.browser.find_element(By.CLASS_NAME, "search-result-header__count").get_attribute("innerText")
        s1 = "".join(c for c in text if c.isdecimal())
        num1 = int(s1)
        num2 = 900
        try:
            if num1 <= num2:
                print('noindex number < 900')
        finally:
            pass
