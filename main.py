from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import subprocess
import logging
import json
import os

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

class Main:
        
    def start(self):

        os.system('taskkill /IM chrome.exe /F')
        subprocess.Popen(
       '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --log-level=3 --remote-debugging-port=9222', shell=True)
        self.options = uc.ChromeOptions()
        self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.options.add_argument("--start-maximized")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--no-sandbox")
        self.driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.options)
        self.driver.maximize_window()
        self.config = json.load(open('config.json'))

    def login(self):

        self.driver.get('https://br.parimatch.com/')
        sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, 'div.modulor_ripple__wrapper__1_49_1').click()
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="phone-field-input"]').click()
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="phone-field-input"]').send_keys(self.config['phone'])
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="password-field-input"]').click()
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="password-field-input"]').send_keys(self.config['password'])
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-button"]').click()
        sleep(5)

        

    def main(self):
        try:
            self.start()
            self.login()
        except Exception as e:
            logging.error(f"Erro: {e}", exc_info=True)
            if self.driver:
                self.driver.quit()
            exit()

if __name__ == '__main__':
    main = Main()
    main.main()