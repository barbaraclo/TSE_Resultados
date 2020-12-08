# TSE RESULTADOS

**Projeto da disciplina de Tópicos Avançados I - Testes Mobile**

Este projeto tem como objetivo automatizar alguns fluxos do aplicativo "Resultados" do TSE. 

Realizado por:

Bárbara Lima e Nikollas Filgueiras

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

📝  **Report**

Para gerar um report da execução, use esse comando quando for rodar o pytest:

```
pytest --html=report.html  
```

Depois da execução, um arquivo "report.html" será gerado na pasta principal do projeto. 
Para verificar o report, clique nele e abra no browser que você utiliza.

___

🎬 **Video da execução**

Neste link é possível visualizar a execução dos testes:
https://drive.google.com/file/d/1Bcl7ZEGm70v9JgGq1pZQC52NsXBfsEIZ/view?usp=sharing
