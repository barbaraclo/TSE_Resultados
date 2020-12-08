from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.seletores.pagina_principal_seletor import PrincipalSeletores


class Base(object):
    def __init__(self, drive):
        self.drive = drive

    def encontrar_elemento(self, elemento):
        """
        Esse método é responsável por encontrar elementos (utilizando presence_of_element_located)
        :param elemento: elementO a ser procurado
        :return: valor do elemento
        """
        valor = WebDriverWait(self, 40).until(EC.presence_of_element_located((
            elemento
        )))
        return valor

    def verificar_tela_home(self):
        """
        Esse método é responsável por validar se está na página principal
        :return: valor do elemento
        """
        resultados = Base.encontrar_elemento(self.drive, PrincipalSeletores.TEXTO_SELECIONE)
        try:
            resultados
        except NoSuchElementException:
            return False
        return True
