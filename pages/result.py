"""
Esse é o módulo que contém a DuckDuckGoResultPage,
a page object para o resultado de pesquisa do site DuckDuckGo.
"""

from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:
    
    # Localizadores
    
    LINKS_DO_RESULTADO = (By.CLASS_NAME, "eVNpHGjtxRBq_gLOfGDr")
    INPUT_DE_PESQUISA = (By.ID, "search_form_input")

    # Inicializador
    
    def __init__(self, browser):
        self.browser = browser
        
    # Métodos de interação
    
    def titulos_dos_links_do_resultado(self):
        links = self.browser.find_elements(*self.LINKS_DO_RESULTADO)
        titulos = [link.text for link in links]
        return titulos
        
    def  valor_do_input_de_pesquisa(self):
        input_de_pesquisa = self.browser.find_element(*self.INPUT_DE_PESQUISA)
        valor = input_de_pesquisa.get_attribute('value')
        return valor
        
    def titulo(self):
        return self.browser.title
        