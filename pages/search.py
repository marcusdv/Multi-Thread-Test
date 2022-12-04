"""
Esse módulo possui a página DuckDuckGoSearchPage,
a page object para a página de pesquisa DuckDuckGo.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:
    
    # URL
    URL = "https://duckduckgo.com"

    # Localizadores 
    
    # input pesquisa é uma TUPLA de 2 elementos
    INPUT_PESQUISA = (By.ID, "search_form_input_homepage")
    
    #  Inicializador
    # define a váriavel local browser como a que for passada. É uma inicialização de instãncia de variável.
    def __init__(self, browser):
        self.browser = browser
        
    # Métodos de interação
    def carregar(self):
        self.browser.maximize_window()
        self.browser.get(self.URL)
    
    def pesquisar(self, frase):
        # esse asterístico pega a TUPLA que é INPUT_PESQUISA e separálos em argumentos em suas respectivas posições. O "find_elements" utiliza DOIS argumentos
        input_pesquisa = self.browser.find_element(*self.INPUT_PESQUISA)
        input_pesquisa.send_keys(frase + Keys.RETURN)