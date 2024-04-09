import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

PROMISED_DOWN = 1000
PROMISED_UP = 1000
CHROME_DRIVER_PATH = "chromedriver/chromedriver.exe"

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(by=By.CLASS_NAME, value="start-button")
        go_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text)
        self.up = float(self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            message = f"Hey Frontier, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

            self.driver.get("https://twitter.com/")
            time.sleep(5)

            login_button = self.driver.find_element(by=By.LINK_TEXT, value="Sign in")
            login_button.click()
            time.sleep(5)

            username = self.driver.find_element(by=By.CSS_SELECTOR, value="[autocomplete='username']")
            username.send_keys(f"{TWITTER_EMAIL}")
            next_button = self.driver.find_element(by=By.LINK_TEXT, value='div[data-testid="LoginForm_Login_Button"]')
            next_button.click()
            time.sleep(5)

            password = self.driver.find_element(by=By.CSS_SELECTOR, value="[autocomplete='password']")
            password.send_keys(Keys.ENTER)
            time.sleep(5)

            tweet = self.driver.find_element(by=By.CLASS_NAME, value="public-DraftStyleDefault-block")
            tweet.send_keys(message)
            tweet_button = self.driver.find_element(by=By.CSS_SELECTOR, value='div[data-testid="tweetButtonInline"]')
            tweet_button.click()
        else:
            print("Internet speed is fine.")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
