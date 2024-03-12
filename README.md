# Automação de Testes de UI com PyTest e Playwright.

## Pré-requisitos mínimos de ambiente:

[Python](https://www.python.org/downloads/) 3.11.x.

[Node.js](https://nodejs.org/en) 18.17.x.


## Instalação do projeto:

```
pip install -r requirements.txt
```

## Instruções:

Executar o comando abaixo no terminal:

```
playwright install
```

## Execução dos testes:

```
pytest --headed --html=reports/report.html tests/submit_form.py
```

## Execução dos testes em paralelo:

```
pytest --headed --html=reports/report.html --numprocesses 7 tests/submit_form.py
```

---

<a href="https://www.linkedin.com/in/thinogueiras"><img alt="Linkedin" src="https://img.shields.io/badge/-LinkedIn-blue?style=for-the-badge&logo=Linkedin&logoColor=white"></a>

<strong>Thiago Nogueira dos Santos</strong> 🤓 ✌🏻

QA Automation Engineer 🔎 🐞
