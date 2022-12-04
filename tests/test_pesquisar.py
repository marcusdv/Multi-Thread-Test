# 
# Testes do site DuckDuckGo.
# 

# importando classes dos page objects
import pytest
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

# pytest, quando ve um test case com um argumento, ele checa o nome desse argumento com todos os fixtures disponíveis do projeto, que irão vir de "conftest.py"
# @pytest.mark.parametrize python vai rodar a função para cada item na lista
@pytest.mark.parametrize('frase', ['panda', 'python', 'polar bear'])
def test_pesquisas_basicas_duckduckgo(browser, frase):
    
    pagina_pesquisa = DuckDuckGoSearchPage(browser)
    pagina_resultado = DuckDuckGoResultPage(browser)
    
    # Faz com que a página inicial duckduckgo seja exibida
    pagina_pesquisa.carregar()

    # Depois faz uma pesquisa por "frase"
    pagina_pesquisa.pesquisar(frase)

    # E se o query de pesquisa de resultado é "frase"
    assert frase == pagina_resultado.valor_do_input_de_pesquisa()

    # E se o link dos resultados contém "frase"
    titulos = pagina_resultado.titulos_dos_links_do_resultado()
    resultados = [t for t in titulos if frase.lower() in t.lower()]
    assert len(resultados) > 0
        
    # Depois verifica se o título da página de pesquisa possuí a pesquisa "frase"
    assert frase in pagina_resultado.titulo()