import pytest
from pages.pagina_principal import Initial
from pages.resultados import Resultados
from pages.seletores.resultados_seletores import ResultadosSeletores


@pytest.mark.usefixtures('test_setup')
class TestResultados(object):
    def test_fluxo_inicial(self, test_setup):
        """
        Esse método testa se é possível alcançar a tela inicial do app sem erros
        :param test_setup: Conexão entre o DUT  e o Appium
        :return: boolean
        """
        initial = Initial(test_setup)
        initial.realizar_fluxo_inicial()
        is_in_home = initial.verificar_tela_home()
        assert is_in_home, 'Não alcançou home'

    def test_estado_municipio_2_turno(self, test_setup):
        """
        Esse método testa se é possível verificar o resultado da eleição do 2 turno escolhendo um estado e municipio, sem erros
        :param test_setup: Conexão entre o DUT  e o Appium
        :return: boolean
        """
        initial_resultados = Resultados(test_setup)
        initial_resultados.buscar_2_turno()
        initial_resultados.escolher_local()
        initial_resultados.escolher_estado_municipio(ResultadosSeletores.BTN_ESTADO_PERNAMBUCO,
                                                     ResultadosSeletores.BTN_MUNICIPIO_RECIFE)
        retorna_recife_pe = initial_resultados.recife_pe_2_turno_validacao()
        assert retorna_recife_pe, 'Resultado Errado'

    def test_favorita_candidato(self, test_setup):
        """
        Esse método testa se ao favoritar um candidato o mesmo aparece corretamente favoritado e na tab de favoritos
        :param test_setup: Conexão entre o DUT  e o Appium
        :return: boolean
        """
        initial_resultados = Resultados(test_setup)
        initial_resultados.favoritar_candidato()
        valida_favorito = initial_resultados.valida_favorito()
        valida_favoritos_tab = initial_resultados.valida_favorito_tab()
        assert (valida_favorito) and (valida_favoritos_tab), 'Candidato não foi favoritado'

    def test_busca_candidato(self, test_setup):
        """
        Esse método testa se ao pesquisar um candidato o mesmo aparece no resultado da busca
        :param test_setup: Conexão entre o DUT e o Appium
        :return: boolean
        """
        initial_resultados = Resultados(test_setup)
        initial_resultados.busca_1_turno()
        valida_busca = initial_resultados.valida_busca()
        assert valida_busca, 'Candidato não foi encontrado'
