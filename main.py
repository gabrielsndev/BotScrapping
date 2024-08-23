from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import logging
import json

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

class Main:
        
    def start(self):

        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        

        self.driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get('https://br.parimatch.com/')
        sleep(10)

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, 'span.modulor_button__text-wrap__1_49_1').click()
        sleep(200)

    def main(self):
        try:
            self.start()
            self.login()
        except Exception as e:
            # Log do erro
            logging.error(f"Erro: {e}")
            if self.driver:
                self.driver.quit()
            exit()

if __name__ == '__main__':
    main = Main()
    main.main()