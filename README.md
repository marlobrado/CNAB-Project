# CNAB-Project

## Iniciando o projeto

1 - Criar o ambiente virtual para a instalação das dependencias:

```
python -m venv venv
```

2 - Ativar o ambiente virtual:

###Linux
```
source venv/bin/activate
```
###Windows 
```
source venv/scripts/activate
```
3 - Instalar as dependências do projeto
```
pip install -r requirements.txt
```

4 - Rodar as migrações

```
python manage.py makemigrations
```
```
python manage.py migrate
```

5 - Inciair o servidor
```
python manage.py runserver
```

## Para fazer um post:
1- Acesse
```
http://127.0.0.1:8000/
```

2 - Envie o arquivo de texto no formulãrio

3 - Será redirecionado par o end point /list/ com os dados do .txt parseados
