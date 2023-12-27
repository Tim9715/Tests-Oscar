import re, time
from selenium import webdriver
from selenium.webdriver.common.by import By


class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://selenium1py.pythonanywhere.com/ru/catalogue/'

    def add_item_to_basket_on_list(self, item_index):
        self.driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/section/div/ol/li[{item_index}]/article/div[2]/form/button').click()

    def click_card(self, item_index):
        self.driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/section/div/ol/li[{item_index}]/article/div[1]/a/img').click()

    def click_logo(self):
        self.driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[1]/a').click()

    def check_price_in_list(self, item_index):
        price = self.driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/section/div/ol/li[{item_index}]/article/div[2]/p[1]').text
        price = float(re.findall("\d+\.\d+", f'{price}'.replace(',', '.'))[0])
        return price


class CardPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_to_basket(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button').click()


class BasketPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://selenium1py.pythonanywhere.com/ru/basket/'

    def check_item_in_basket(self):
        return self.driver.find_element(By.CLASS_NAME, 'basket-items')


    def check_price_in_basket(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]').text

    def item_in_basket(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/form/div/div/div[2]/h3').text

    def clear_area_in_basket(self):
        area = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/form/div/div/div[3]/div[1]/div/input')
        area.clear()
        area.send_keys('0')

    def click_update_button(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/form/div/div/div[3]/div[1]/div/span/button').click()

    def click_button_make_order(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div/a').click()


class AuthPage:
    def __init__(self, driver):
        self.driver = driver

    def check_auth_window(self):
        email_area = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div[1]/div/input')
        password_area = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div[3]/div/div/div/input')
        text = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/h1').text
        if email_area and password_area and text: return True


class LogoPage:
    def __init__(self, driver):
        self.driver = driver

    def check_summ_basket(self):
        return self.driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[2]').text

    def check_basket_button(self):
        return self.driver.find_element(By.CLASS_NAME, 'btn-group')


class Tests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.catalog_page = CatalogPage(self.driver)
        self.card_page = CardPage(self.driver)
        self.basket_page = BasketPage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.logo_page = LogoPage(self.driver)

    def test_add_in_basket_on_list(self):
        self.driver.get(self.catalog_page.url)
        time.sleep(3)

        self.catalog_page.add_item_to_basket_on_list(1)
        time.sleep(1)

        self.driver.get(self.basket_page.url)
        time.sleep(2)

        assert self.basket_page.check_item_in_basket()
        
        self.driver.quit()
        
    def test_add_in_basket_in_card(self):
        self.driver.get(self.catalog_page.url)
        time.sleep(3)

        self.catalog_page.click_card(3)
        time.sleep(2)

        self.card_page.click_add_to_basket()
        time.sleep(1)

        self.driver.get(self.basket_page.url)
        time.sleep(2)

        assert self.basket_page.check_item_in_basket()
        
        self.driver.quit()

    def test_correct_display_in_basket(self):
        self.driver.get(self.catalog_page.url)
        time.sleep(3)

        self.catalog_page.add_item_to_basket_on_list(2)
        time.sleep(1)

        self.driver.get(self.basket_page.url)
        time.sleep(2)

        item = self.basket_page.check_item_in_basket()

        self.basket_page.clear_area_in_basket()

        self.basket_page.click_update_button()

        self.driver.get(self.catalog_page.url)
        time.sleep(3)

        self.catalog_page.click_card(2)
        time.sleep(2)

        self.card_page.click_add_to_basket()
        time.sleep(1)

        self.driver.get(self.basket_page.url)
        time.sleep(2)

        item2 = self.basket_page.check_item_in_basket()

        assert item == item2
        
        self.driver.quit()

    def test_summ_basket(self):
        self.driver.get(self.catalog_page.url)
        time.sleep(3)

        self.catalog_page.add_item_to_basket_on_list(1)
        time.sleep(1)

        self.catalog_page.add_item_to_basket_on_list(2)
        time.sleep(1)

        price1 = self.catalog_page.check_price_in_list(1)
        price2 = self.catalog_page.check_price_in_list(2)
        summ = str(price1 + price2).replace('.', ',')

        self.driver.get(self.basket_page.url)
        time.sleep(2)

        basket_text = self.basket_page.check_price_in_basket()

        assert basket_text == f'Всего в корзине {summ} £'

        self.driver.quit()

    def test_auth_window(self):
        self.driver.get(self.catalog_page.url)
        time.sleep(3)

        self.catalog_page.add_item_to_basket_on_list(1)
        time.sleep(1)

        self.driver.get(self.basket_page.url)
        time.sleep(2)

        self.basket_page.click_button_make_order()
        time.sleep(2)

        assert self.auth_page.check_auth_window() == True
        
        self.driver.quit()

    def test_logo_basket(self):
        self.driver.get(self.catalog_page.url)
        time.sleep(3)

        self.catalog_page.add_item_to_basket_on_list(1)
        time.sleep(1)

        self.catalog_page.add_item_to_basket_on_list(2)
        time.sleep(1)

        price1 = self.catalog_page.check_price_in_list(1)
        price2 = self.catalog_page.check_price_in_list(2)
        summ = str(price1 + price2).replace('.', ',')

        self.catalog_page.click_logo()
        time.sleep(1)

        basket_text = self.logo_page.check_summ_basket()

        button_basket = self.logo_page.check_basket_button()

        assert basket_text == f'Всего в корзине: {summ} £\nПосмотреть корзину' and button_basket
        
        self.driver.quit()

tests = Tests()
tests.test_add_in_basket_on_list()
tests.test_add_in_basket_in_card()
tests.test_correct_display_in_basket()
tests.test_summ_basket()
tests.test_auth_window()
tests.test_logo_basket()

