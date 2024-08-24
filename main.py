from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import subprocess
import platform
import logging
import json
import os

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

class Main:
        
    def start(self):
        system = platform.system()
        
        if system == "Windows":
            subprocess.Popen(
                f'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --log-level=3 --remote-debugging-port=9222 --disable-popup-blocking', shell=True)
        elif system == "Linux":
            subprocess.Popen(
                f'/usr/bin/google-chrome --log-level=3 --remote-debugging-port=9222', shell=True)
        
        sleep(1)
        service = Service()
        self.options = webdriver.ChromeOptions()

        self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.options.add_argument("--start-maximized")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument(" ")
        
        if system == "Windows":
            self.driver = webdriver.Chrome(service=service, options=self.options)
        elif system == "Linux":
            self.driver = webdriver.Chrome(service=service, options=self.options)
        self.config = json.load(open('config.json'))
        self.driver.get('https://br.parimatch.com/')

    def entrando_jogo(self):

        sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, '[data-id="header-instant-games"]').click()
        sleep(5)
        self.elements = self.driver.find_elements(By.CSS_SELECTOR, 'li.NavigationBlock__item_ig--ig-r4zue')
        self.elements[4].click()
        sleep(5)
        self.input = self.driver.find_element(By.CSS_SELECTOR, 'input.Input__input_ig--ig-by18T.SearchInput__field_ig--ig-EyWJ_')
        self.input.click()
        self.input.send_keys('Aviator')
        sleep(1)
        self.input.send_keys(Keys.ENTER)
        sleep(3)
        self.driver.find_elements(By.CSS_SELECTOR, 'a.GameCard__title_ig--ig-oEqAU')[0].click()
        sleep(10)

    def pegando_ultimos(self):
        sleep(1)
#        iframe = self.driver.find_elements(By.CSS_SELECTOR, 'iframe')[]
#        self.driver.get(iframe.get_attribute('src'))
#        sleep(2)


    def main(self):
        try:
            self.start()
            self.entrando_jogo()
            self.pegando_ultimos()
        except Exception as e:
            logging.error(f"Erro: {e}", exc_info=True)
            if self.driver:
                self.driver.quit()
            exit()

if __name__ == '__main__':
    main = Main()
    main.main()