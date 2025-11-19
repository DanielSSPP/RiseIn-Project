# RiseIn-Project
Projeto construido em Django de uma plataforma de divulgação de vagas de estágio e oportunidades para a disciplina desenvolvimento rápido de aplicações em Python

## Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* **Python**
* **Django**
* **Pillow**

## Pré-requisitos

Para rodar o projeto, você vai precisar de:
* **Python** (foi utilizada a versão 3.13.9 para o produção do projeto)
* **Django** (se possível a versão mais recente)
* Ambiente virtual **venv**

## Executando o Projeto

Siga os passos abaixo para executar a aplicação no seu ambiente local.

**1. Clone o repositório:**
```bash
git clone https://github.com/DanielSSPP/RiseIn-Project.git
```

**2. Crie o ambiente virtual:**
```
python -m venv .venv
```

**3. Ative o ambiente virtual:**
```
.venv\Scripts\activate
```

**4. Acesse a pasta da aplicação:**
```bash
cd risein
```

**5. Rode os comandos:**
```
pip install django
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```

**Execute tudo nessa exata ordem para funcionar**

**6. Inicialize o servidor:**
```
python manage.py runserver
```
no terminal terá um link para abrir no seu localhost
