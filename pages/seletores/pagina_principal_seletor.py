from appium.webdriver.common.mobileby import MobileBy


class PrincipalSeletores(object):
    """
    Essa classe contém todos os seletores da página principal
    """
    BTN_PROX = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Próximo\")')
    BTN_ENTENDI = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Entendi\")')
    BTN_LI_ACEITO = (MobileBy.XPATH, ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                      ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                      "/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android"
                                      ".view.View/android.view.View/android.view.View/android.view.View/android.view"
                                      ".View[2]/android.view.View[2]/android.view.View[3]/android.widget.Button"))
    TEXTO_SELECIONE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Selecione\")')