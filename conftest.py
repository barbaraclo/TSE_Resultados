import pytest
from appium import webdriver


@pytest.fixture(scope='class')
def test_setup():
    """
    Configuração para a conexão entre Appium e o DUT
    :return: conexão
    """
    desired_cap = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'app': 'C:\\TSE_Resultados\\recursos\\apk\\br.resultado.apk',
        'autoGrantPermissions': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    yield driver
    driver.quit()
