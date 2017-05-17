# IntegraTI
Veja nossa [wiki](https://github.com/bti-imd/IntegraTI-API/wiki).

# Instruções
## Configurando ambiente
- Baixar o [Python 3.6.1](https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe)
- Baixar o [MySQL](https://dev.mysql.com/downloads/installer/)
    - configurar o user ***```root```*** com password ***```root```***
    - criar database IntegraTI com ***```create database IntegraTI;```*** no MySQL
- Criar arquivo ***```logs/error.log```***
- Criar um virtual environment com ***```python -m venv env```***
- Ativar o virutal env
    - On Windows, run: ***```env\Scripts\activate.bat```***
    - On Unix or MacOS, run: ***```source env/bin/activate```***
- Rodar pip install com ***```pip install -r requirements.txt```***

## Rodando aplicação
- Criar tabelas com o manager da aplicação
    - rodar ***```python manage.py db init```***
    - rodar ***```python manage.py db migrate```***
    - rodar ***```python manage.py db upgrade```***
- rodar a aplicação com ***```python run.py```***
