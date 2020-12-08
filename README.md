# TSE RESULTADOS

**Projeto da disciplina de Tópicos Avançados I - Testes Mobile**

Este projeto tem como objetivo automatizar alguns fluxos do aplicativo "Resultados" do TSE. 

Realizado por:
Bárbara Lima
Nikollas Filgueiras

___

**Estrutura do projeto:**

Neste projeto foi utilizado o Python + pytest + Appium. Abaixo econtra-se a estrutura realizada no projeto :

```
TSE_Resultados/
  pages/
      seletores /
          pagina_principal_seletor.py
          resultados_seletores.py
      base.py
      pagina_principal.py
      resultados.py
  recursos/
      apk/
          br.resultado.apk
  testes /
      test_resultados.py
```

🗂 **Explicação sobre a estrutura do projeto**

Pages >> PageObjects relacionados, um arquivo .py para cada página e suas funcionalidades.

Recursos >> Indicação da apk a ser usada

Testes >> Fluxo de teste para a execução.
___

**Recursos**

🎯 Foi utilizado:

Python <br>
Pytest <br>
Appium-Python-Client <br>
Selenium <br>

🛠 Como instalar?

Basta executar o arquivo requirements.txt usando o seguinte comando no caminho raiz:

```
pip install -r requirements.txt
```
___


💻 **Configuração do ambiente de teste**

Modifique no arquivo conftest.py os seguintes parametros de acordo com a sua configuração de device.

```
'deviceName': 'NomedoSeuDevice',
'app': SeuCaminho\\TSE_Resultados\\recursos\\apk\\br.resultado.apk'
```

Para executar o projeto, basta chamar pytest no terminal:

```
pytest
```
___

