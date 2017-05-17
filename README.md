 # IntegraTI

É a API que irá fornecer os dados para o sistema IntegraTI.

Veja nossa [wiki](https://github.com/bti-imd/IntegraTI-API/wiki). E se você pretende ajudar no desenvolvimento, leia e siga nosso [arquivo de contribuição](./CONTRIBUTING.md).

# Instruções

> **Atenção***: as configurações de desenvolvimento são instáveis e se atualizando constantemente, não sendo adequadas para produção

## Configurando ambiente de desenvolvimento

- Instale os seguintes programas e certifique-se de que as **versões** usadas estão sempre corretas e os serviços estão **ativos**:
    - [Python 3.6.1](https://www.python.org/downloads/release/python-361) (mas provavelmente qualquer versão acima de 3.3 irá servir)
        - Tenha certeza de que seu Python3 tem o ```pip``` adequado a ele (no Linux, às vezes é pip3), com módulo ```virtualenv``` instalado
    - [MySQL](https://dev.mysql.com/downloads/installer/) recente
- Prepare o ambiente virtual:
    - Crie banco de dados chamado IntegraTI (com ```create database IntegraTI``` em um console do MySQL)
    - Edite as variáveis de prefixo ```DB_``` no arquivo [config.py](./config.py) com os dados de instalação do seu MySQL
    - Crie um arquivo vazio ```logs/error.log```
    - Crie o ambiente virtual via console usando ```python -m venv env```
- Ative o ambiente virtual (e você irá **precisar refazer este único passo sempre que executar usar o sistema**):
    - No Windows, execute no prompt (cmd): ```env\Scripts\activate.bat```
    - No Unix ou MacOS, execute no terminal (bash): ```source env/bin/activate```
- Rode o ```pip``` para instalar as dependências do sistema com ```pip install -r requirements.txt```.
- Termine de configurar o banco de dados adicionando as tabelas dele através do console do seu SO:
    - Rode ```python manage.py db init```: Inicializa o banco de dados pelos models
    - Rode ```python manage.py db migrate```: Cria uma migração com nase nas alterações feitas dos models
    - Rode ```python manage.py db upgrade```: Altera o banco de dados com base nas migrações criadas

## Rodando o servidor

Considerando que todo o ambiente foi corretamente instalado e configurado, sempre que for executar o sistema:

- Execute novamente o passo de ativação do ambiente virtual
- Inicie o servidor com ```python run.py``` e leia o output que lhe dirá em qual endereço IP e porta a aplicação está rodando
    - Se for "0.0.0.0" significa que está aberto para toda sua rede interna, e você deve encontrar seu IP público (no Linux, use ```ifconfig```)
- Se você souber como usar aplicações RESTful, consulte nossa documentação, e o comando ```curl``` poderá lhe ajudar a formar as requisições
- Não se esqueça de que essa aplicação é apenas o server side e precisa da instalação do [repositório web do IntegraTI](https://github.com/discentes-imd/IntegraTI-Web) para se "materializar" para um usuário comum.
