import re, time
from selenium import webdriver
from selenium.webdriver.common.by import By

site = 'https://selenium1py.pythonanywhere.com/ru/catalogue/'
basket = 'https://selenium1py.pythonanywhere.com/ru/basket/'

def test_add_in_basket_on_list():
    driver = webdriver.Chrome()
    driver.get(site)
    time.sleep(3)

    button_add = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button').click()
    time.sleep(1)

    driver.get(basket)
    time.sleep(2)

    basket_item = driver.find_element(By.CLASS_NAME, 'basket-items')

    assert basket_item

    driver.quit()

def test_add_in_basket_in_card():
    driver = webdriver.Chrome()
    driver.get(site)
    time.sleep(3)

    card = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[3]/article/div[1]/a/img').click()
    time.sleep(2)
    add_basket = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button').click()
    time.sleep(1)

    driver.get(basket)
    time.sleep(2)

    basket_item = driver.find_element(By.CLASS_NAME, 'basket-items')

    assert basket_item

    driver.quit()

def test_correct_display_in_basket():
    driver = webdriver.Chrome()
    driver.get(site)
    time.sleep(3)

    button_add = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/section/div/ol/li[2]/article/div[2]/form/button').click()
    time.sleep(1)

    driver.get(basket)
    time.sleep(2)

    item = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/form/div/div/div[2]/h3').text

    area = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/form/div/div/div[3]/div[1]/div/input')
    area.clear()
    area.send_keys('0')

    update_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/form/div/div/div[3]/div[1]/div/span/button').click()

    driver.get(site)
    time.sleep(2)

    card = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[2]/article/div[1]/a/img').click()
    time.sleep(2)
    add_basket = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button').click()
    time.sleep(1)

    driver.get(basket)
    time.sleep(2)

    item2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/form/div/div/div[2]/h3').text

    assert item == item2

    driver.quit()

def test_summ_basket():
    driver = webdriver.Chrome()
    driver.get(site)
    time.sleep(3)

    button_add = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button').click()
    time.sleep(1)
    button_add2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[2]/article/div[2]/form/button').click()
    time.sleep(1)

    price1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/p[1]').text
    price2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[2]/article/div[2]/p[1]').text
    price1 = float(re.findall("\d+\.\d+", f'{price1}'.replace(',', '.'))[0])
    price2 = float(re.findall("\d+\.\d+", f'{price2}'.replace(',', '.'))[0])
    summ = str(price1 + price2).replace('.', ',')

    driver.get(basket)
    time.sleep(2)

    basket_text = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]').text

    assert basket_text == f'Всего в корзине {summ} £'

    driver.quit()

def test_auth_window():
    driver = webdriver.Chrome()
    driver.get(site)
    time.sleep(3)

    button_add = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button').click()
    time.sleep(2)

    driver.get(basket)
    time.sleep(2)

    button_make_order = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div/a').click()
    time.sleep(2)

    auth_window = driver.find_element(By.CLASS_NAME, 'default')

    email_area = driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div[1]/div/input')
    password_area = driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div[3]/div/div/div/input')

    text = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/h1').text

    assert text == 'Кто Вы?' and email_area and password_area

    driver.quit()

def test_logo_basket():
    driver = webdriver.Chrome()
    driver.get(site)
    time.sleep(3)

    button_add = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button').click()
    time.sleep(1)
    button_add2= driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[2]/article/div[2]/form/button').click()
    time.sleep(1)

    price1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/p[1]').text
    price2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/section/div/ol/li[2]/article/div[2]/p[1]').text
    price1 = float(re.findall("\d+\.\d+", f'{price1}'.replace(',', '.'))[0])
    price2 = float(re.findall("\d+\.\d+", f'{price2}'.replace(',', '.'))[0])
    summ = str(price1 + price2).replace('.', ',')
    
    button_logo = driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[1]/a').click()
    time.sleep(1)

    basket = driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[2]').text

    button_basket = driver.find_element(By.CLASS_NAME, 'btn-group')

    assert basket == f'Всего в корзине: {summ} £\nПосмотреть корзину'

    driver.quit()
