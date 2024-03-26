import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_products():
    index = 0
    product_elements = []

    while True:
        try:
            things = driver.find_element(by=By.CSS_SELECTOR, value=f"#products #product{index}")
            if "product unlocked enabled" in things.get_attribute("class"):
                product_elements.append(things)

            index += 1
        except:
            return product_elements


URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

driver.get(URL)

english_button = driver.find_element(By.ID, value="langSelect-EN")
english_button.click()

time.sleep(3)

cookie_image = driver.find_element(by=By.ID, value="bigCookie")

start_time = datetime.now()

while True:
    cookie_image.click()

    current_time = datetime.now()
    elapsed_time = current_time - start_time

    if elapsed_time >= timedelta(minutes=.5):
        product_list = get_products()
        for product in product_list[::-1]:
            product.click()

        start_time = datetime.now()
