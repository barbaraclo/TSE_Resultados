import os
from pages.seletores.pagina_principal_seletor import PrincipalSeletores
from pages.base import Base


class Initial(Base):
    def realizar_fluxo_inicial(self):
        """
        Esse método realiza o fluxo inicial do app
        :return: None
        """
        btn_prox = Base.encontrar_elemento(self.drive, PrincipalSeletores.BTN_PROX)
        btn_prox.click()
        btn_entendi = Base.encontrar_elemento(self.drive, PrincipalSeletores.BTN_ENTENDI)
        btn_entendi.click()
        os.system('adb shell input swipe 500 1000 500 0')
        btn_li_aceito = Base.encontrar_elemento(self.drive, PrincipalSeletores.BTN_LI_ACEITO)
        btn_li_aceito.click()


