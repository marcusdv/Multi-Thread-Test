"""
This module contains shared fixtures.
"""

import json
import selenium.webdriver
import pytest

# para limpar temos fixture functions, são funções ques possuem as fases de inicio e termino em um corpo.
# ELes ficam no file chamado "conftest.py". O nome do file é importante. Pytest irá identificar pelo nome em procura de fixtures e plugins.

@pytest.fixture
def config(scope='session'):
    # Lê o arquivo
    # E transforma em um dicionario python
    with open('config.json') as config_file:
        config = json.load(config_file)
        
    # Afirma se os valores são aceitaveis
    # verifica se o browser está correto
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    # e se o implicit_wait é inteiro
    assert isinstance(config['implicit_wait'], int)
    # e se é um valor
    assert config['implicit_wait'] > 0

    # Retorna a configuração para que possa ser utilizada
    return config

@pytest.fixture
def browser(config):

    # Iniciar a instância
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Chamada por espera para dar tempo dos elementos aparecerem na tela, antes de desistir
    b.implicitly_wait(config['implicit_wait'])

    # Retorna (return mesmo) a instância do WebDriver para setup
    yield b

    # Sai da instância WebDriver para limpar
    b.quit()