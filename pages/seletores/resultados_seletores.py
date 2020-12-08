from appium.webdriver.common.mobileby import MobileBy


class ResultadosSeletores(object):
    """
    Essa classe contém todos os seletores da página de resultados
    """

    BTN_RESULTADOS = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Resultados\")')
    BTN_TURNO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"1ºTURNO\")')
    BTN_ESCOLHER_LOCAL = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Escolher local\")')
    DROP_DOWN_ELEICOES = (
    MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                     ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                     ".ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View"
                     "/android.view.View/android.view.View/android.view.View/android.view.View/android"
                     ".view.View/android.view.View/android.view.View/android.view.View["
                     "2]/android.view.View[2]/android.view.View[1]"))

    BTN_2_TURNO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"2º Turno\")')

    DROP_DOWN_ESTADO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Selecione o estado\")')

    BTN_ESTADO_PERNAMBUCO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Pernambuco\")')
    BTN_CONFIRMAR_LOCAL = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Confirmar\")')

    DROP_DOWN_MUNICIPIO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Selecione o município\")')
    BTN_MUNICIPIO_RECIFE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Recife\")')

    HOME_TEXTO_RECIFE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Recife, PE\")')

    CANDIDATO_TEXTO_MARILIA = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"MARILIA ARRAES\")')
    BTN_FAVORITAR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Favoritar\")')
    FAVORITO_TEXTO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Favorito\")')

    BTN_FECHAR = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Fechar\")')

    BTN_FAVORITOS_TAB = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Favoritos\")')

    BTN_ESCOLHE_TURNO_TOP = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                             ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                             "/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android"
                                             ".view.View/android.view.View/android.view.View/android.view.View/android.view"
                                             ".View/android.view.View/android.view.View/android.view.View/android.view"
                                             ".View[1]/android.view.View[1]/android.view.View/android.widget.Button")
    DIALOG_1_TURNO = (MobileBy.XPATH,
                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                      "/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit"
                      ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.app.Dialog/android"
                      ".view.View[3]/android.view.View[2]/android.widget.RadioButton[1]")
    BTN_CONFIRMAR_TURNO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"CONFIRMAR\")')

    BTN_RESUL = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                                 ".ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
                                 ".view.View/android.view.View/android.view.View/android.view.View/android.widget"
                                 ".TabWidget/android.view.View[1]/android.view.View")

    BTN_PESQUISAR_CANDIDATO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Pesquisar candidato\")')
    BARRA_BUSCA = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                                    ".ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View"
                                    "/android.view.View/android.view.View/android.app.Dialog/android.view.View"
                                    "/android.view.View[1]/android.view.View[2]/android.view.View["
                                    "2]/android.view.View/android.view.View/android.widget.EditText"))


    RESULTADO_PESQUISA = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"DANI PORTELA\")')
