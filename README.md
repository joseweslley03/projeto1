# Meu primeiro projeto Django
Este é o meu primeiro projeto Django, que aborda as bases do framework.

## Instrução para baixar, editar e executar local
1. Clone o projeto
```bash
git clone https://github.com/joseweslley03/projeto1.git
```
2. Entre na pasta do projeto e crie um ambiente virtual python
```bash
cd projeto1
```
```bash
python -m venv .venv

3. ative o ambiente virtual no windows:
```bash
.venv\Scripts\activate
```
no Linux:
```bash
source .venv/bin/activate
```
4. instale as dependencias
```bash
pip install -r requirements-dev.txt
```
5. execute as migrações
```bash
python manage.py migrate
```
6. execute o servidor
```bash
python manage.py runserver
```
