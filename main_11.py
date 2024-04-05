from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os

PROMISE_DOWN = 150
PROMISE_UP = 30
TWITTER_EMAIL = 'CRYPTOBLUEWOLF@GMAIL.COM'
TWITTER_PASSWORD = os.environ.get('PASSWORD_CRYPTO')
USERNAME = 'CryptoWolf29'


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)  # keeps chrome open


class InternetSpeedTwitterBot:
    def __init__ (self, ):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver= webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0
        
    def get_internet_speed(self):
        self.driver.get('https://fast.com/es/')      
        
        # time.sleep(5)

        # go_test = self.driver.find_element(By.XPATH, value='//*[@id="main-content"]/div[1]/div/button/span')
        # go_test.click()
        
        time.sleep(35)
        
        more_info = self.driver.find_element(By.XPATH, value='//*[@id="show-more-details-link"]')
        more_info.click()
        
        time.sleep(10)
                    
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="upload-value"]').text
        
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="speed-value"]').text
        
        print(self.up)
        print(self.down)
        pass
    
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/home?lang=es')
        
        time.sleep(2)
        continue_google = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        continue_google.click()
        
        time.sleep(2)
        email = self.driver.find_element(By.NAME, value='text')
        email.click()
        email.send_keys(TWITTER_EMAIL)    
        next = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next.click()
        
        # time.sleep(2)
        # username = self.driver.find_element(By.NAME, value='text')
        # username.click()
        # username.send_keys(USERNAME)        
        # next = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        # next.click()
        
        time.sleep(2)
        password = self.driver.find_element(By.NAME, value='password')
        password.click()
        password.send_keys(TWITTER_PASSWORD)        
        next = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        next.click()
        
        # x = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg/g/path')
        # x.click()
        
        body = f'Hey internet provider, why is my internet speed {self.up}up/{self.down}down when I pay for 50up/150down?'
        
        time.sleep(3)
        tweet = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(body)
        
        post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
        post.click()
        pass
    
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

