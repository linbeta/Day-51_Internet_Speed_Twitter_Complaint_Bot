from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

PROMISED_DOWN = 60
PROMISED_UP = 24
PATH = "D:\OneDrive\Development\Tools\chromedriver.exe"
TWITTER_ID = os.environ['T_ID']
TWITTER_PW = os.environ['T_PW']

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        sleep(5)
        go_btn = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()
        sleep(60)
        download = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = float(download.text)
        upload = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = float(upload.text)
        sleep(5)
        self.driver.quit()

    def tweet_auto_bot(self):
        internet_speed = f"DOWN: {self.down} Mbps / UP: {self.up} Mbps."
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            return f"Complain bot: {internet_speed} It should be {PROMISED_DOWN}/{PROMISED_UP} Mbps!"
        else:
            return f"Auto internet speed test bot: {internet_speed}"


# Create a bot object called bot_test from the class InternetSpeedTwitterBot
bot_test = InternetSpeedTwitterBot()
bot_test.get_internet_speed()
tweet_content = bot_test.tweet_auto_bot()

###LOGIN TWITTER ####
driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/home")
sleep(2)
# Log in twitter account:
twitter_id = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
twitter_id.send_keys(TWITTER_ID)
twitter_pw = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
twitter_pw.send_keys(TWITTER_PW)
twitter_pw.send_keys(Keys.ENTER)
sleep(2)

# Post content and tweet it!
input_box = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
input_box.send_keys(f"@{TWITTER_ID} {tweet_content}")
tweet_btn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
tweet_btn.click()
