import os
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from pages.seletores.resultados_seletores import ResultadosSeletores
from pages.base import Base


class Resultados(Base):
    def buscar_2_turno(self):
        """
        Esse método seleciona o segundo turno no menu principal
        :return: None
        """
        drop_down_eleicoes = Base.encontrar_elemento(self.drive, ResultadosSeletores.DROP_DOWN_ELEICOES)
        drop_down_eleicoes.click()
        btn_2_turno = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_2_TURNO)
        btn_2_turno.click()

    def escolher_local(self):
        """
        Esse método clica na escolha de um local de votação
        :return: None
        """
        Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_2_TURNO)
        btn_escolher_local = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_ESCOLHER_LOCAL)
        btn_escolher_local.click()

    def escolher_estado_municipio(self, estado, municipio):
        """
        Esse método escolhe o estado e municipio de votação
        :param estado: estado value
        :param municipio: municipio value
        :return: None
        """
        btn_estado = Base.encontrar_elemento(self.drive, ResultadosSeletores.DROP_DOWN_ESTADO)
        btn_estado.click()
        os.system('adb shell input swipe 500 1000 500 0')
        drop_seleciona_estado = Base.encontrar_elemento(self.drive, estado)
        drop_seleciona_estado.click()

        btn_confirma = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_CONFIRMAR_LOCAL)
        btn_confirma.click()

        drop_seleciona_municipio = Base.encontrar_elemento(self.drive, ResultadosSeletores.DROP_DOWN_MUNICIPIO)
        drop_seleciona_municipio.click()

        btn_municipio = Base.encontrar_elemento(self.drive, municipio)
        btn_municipio.click()

        btn_confirma.click()
        btn_confirma.click()

    def recife_pe_2_turno_validacao(self):
        """
        Esse método valida que o municipio escolhido foi exibido corretamente
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.HOME_TEXTO_RECIFE))
        except NoSuchElementException:
            return False
        return True

    def favoritar_candidato(self):
        """
        Esse método favorita um candidato
        :return: None
        """
        os.system('adb shell input swipe 500 1000 500 0')

        texto_marilia = Base.encontrar_elemento(self.drive, ResultadosSeletores.CANDIDATO_TEXTO_MARILIA)
        texto_marilia.click()

        btn_favoritar = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_FAVORITAR)
        btn_favoritar.click()


    def valida_favorito(self):
        """
        Esse método valida se o candidato foi favoritado corretamente na tela de detalhes do candidato
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.FAVORITO_TEXTO))
        except NoSuchElementException:
            return False
        return True

    def valida_favorito_tab(self):
        """
        Esse método valida se o candidato favoritado foi exibido na tab de favoritos
        :return: boolean
        """
        try:
            btn_fechar = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_FECHAR)
            btn_fechar.click()
            tab_favoritos = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_FAVORITOS_TAB)
            tab_favoritos.click()
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.CANDIDATO_TEXTO_MARILIA))
        except NoSuchElementException:
            return False
        return True

    def busca_1_turno(self):
        """
        Esse método realiza a busca de um candidato do primeiro turno
        :return: None
        """

        btn_resultados = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_RESUL)
        btn_resultados.click()

        btn_escolhe_turno = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_ESCOLHE_TURNO_TOP)
        btn_escolhe_turno.click()

        dialog_turno = Base.encontrar_elemento(self.drive, ResultadosSeletores.DIALOG_1_TURNO)
        dialog_turno.click()

        btn_confirma = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_CONFIRMAR_TURNO)
        btn_confirma.click()

        btn_pesquisar_candidato = Base.encontrar_elemento(self.drive, ResultadosSeletores.BTN_PESQUISAR_CANDIDATO)
        btn_pesquisar_candidato.click()

        barra_busca = Base.encontrar_elemento(self.drive, ResultadosSeletores.BARRA_BUSCA)
        barra_busca.send_keys("dani")

    def valida_busca(self):
        """
        Esse método valida se a busca de um candidato do primeiro turno foi feita corretamente
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.drive, 15)
            wait.until(EC.presence_of_element_located(ResultadosSeletores.RESULTADO_PESQUISA))
        except NoSuchElementException:
            return False
        return True

