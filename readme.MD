# Universidade Federal Fluminense - UFF
## Autor : Márcio Garrido
### marciogarrido@id.uff.br


[![N|Solid](https://upload.wikimedia.org/wikipedia/pt/thumb/4/47/UFF_bras%C3%A3o.png/200px-UFF_bras%C3%A3o.png)](http://www.ppgeet.uff.br/site/)

## Baixando arquivos de um website utilizando Python
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Siste de pesquisa

![Screenshot](/venv/img/url.png)

### Documentação Python

https://www.python.org/doc/

Instale a versão atualizada do Python na sua máquina caso nao tenha.
## Instalando Python

        pip install Python 3.9.12

## Criando Ambientes de desenvolvimento
Para garantirmos que a versão do seu projeto não conflite com outros apps, o recomendado é criar ambientes isolados.
Para criar, há a parte "Creating virtual environments". Para organizar o projeto, crie um diretório e em sequencia vá para o local criado.


        mkdir -p ~/Users/marciogarrido/TCM-TASK
        cd ~/Users/marciogarrido/TCM-TASK

Com local já identificado, o próximo passo é virtualizar o ambiente de desenvolimento venv

        python3 -m venv ./venv

No decorrer da aplicação, editamos e alteramos o código usando o Visual Studio Code, mas outros editores como PyCharm, Sublime Text ou Atom também são eficientes. 

Abrindo-o, acessamos a pasta "aplicacao > venv" e abrimos o terminal com "Command + J". Na janela "Terminal", precisamos carregar o ambiente virtual digitando pwd para copiar e colar o caminho após escrever source na linha seguinte. 

        pwd
        /Users/marciogarrido/TCM-TASK

No meu caso, o retorno do comando pwd foi o meu perfil, que vai variar de acordo com as suas credenciais. Com seu perfil identificado, o próximo passo é criar de fato o ambiente. Escrevemos /venv/bin/activate na sequência do caminho para acessar a pasta e inicializar com "Enter". Temos confirmação quando aparece (venv) antes do diretório.

         source /Users/marciogarrido/TCM-TASK/venv/bin/activate

Para validar se o processo foi concluído com sucesso, seu terminal agora deve ter o nome venv no início do texto como abaixo:

        (venv) (base) [TCM-TASK]  

Após a configurar o ambiente, é necessário instalar as depenências.

        pip install -r requirements.txt

Para rodar o programa de captura dos CSV, rode o arquivo :

        Tcm.py

O terminal irá gerar o report do download dos arquivos para a pasta download

![Screenshot](/venv/img/response.png)        

Para rodar o programa de modelagem da tabela produto rode o arquivo:

        ModelagemProduto.py

![Screenshot](/venv/img/produto.png) 

Para rodar o programa de modelagem da tabela Estabelecimento e precos rode o arquivo:

        ModelagemEstabelecimento.py

Ao final, serão gerados 3 arquivos na pasta temporaria tmp

![Screenshot](/venv/img/estabelecimentos.png) 

