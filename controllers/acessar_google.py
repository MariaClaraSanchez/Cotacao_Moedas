from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SiteGoogle:
    def __init__(self, caminho_driver: str) -> None:
        """Instancia a classe com as configurações iniciais
        Args: 
            caminho_driver (str): caminho do executavel do chromedriver 
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--log-level=3')

        self.driver = webdriver.Chrome(caminho_driver,
                                       options=chrome_options)

    def acessar_google(self) -> dict:
        """Acessa o site do google
        """
        self.driver.get('https://google.com.br')
        xpath_google = '//*[@class="gLFyf gsfi" and @name="q"]'
        xpath_valor = '//*[@class="DFlfde SwHCTb"]'
        
        #moedas = ['Dolar','Euro']
        #print(type(moedas))

        moedas = ['Dolar','Euro', 'Libra Esterlina', 'Iene', 'Dólar Australiano',
                    'Franco Suíço', 'Dólar Canadense', 'Renminbi (Yuan)', 
                    'Peso Argentino', 'Lira Turca']    

        moeda_valor = []
        #print(type(moeda_valor))
        time.sleep(4)
        for nome in moedas:
            self.driver.find_element(By.XPATH, xpath_google).send_keys(f'Cotação {nome}')
            self.driver.find_element(By.XPATH, xpath_google).send_keys(Keys.RETURN)
            valor = self.driver.find_element(By.XPATH,xpath_valor).text
            valor = valor.replace(',','.')
            self.driver.find_element(By.XPATH, xpath_google).clear()
            moeda_valor.insert(0,(nome, float(valor)))
 
        return moeda_valor