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
        self.options = uc.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
        self.driver = uc.Chrome(options=self.options)
        self.driver.get("https://donald.bet/")


                   
    def main(self):
        try:
            self.carregar_dados()
            self.iniciar_telas()
            sleep(5)
            while True:
                mensagem = self.telegram.buscar_ultima_mensagem()
                if mensagem:
                    self.ultimos = self.pegar_ultimos_resultados()
                    self.apostar(mensagem)
                
                sleep(1)
        except:
            self.driver.quit()
            self.telegram.driver.quit()
            exit()

if __name__ == '__main__':
    main = Main()
    main.main()