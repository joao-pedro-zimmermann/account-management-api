# Case Assis - Account Management API

## Sobre esse projeto

Esse projeto foi feito tomando como base a [descrição do projeto](support_materials/descricao_teste_tecnico.pdf) e a [documentação](support_materials/api_documentation.pdf).

É importante observar que a documentação técnica da API foi tomada como base, porém não foi seguida a risca, tendo pequenas alterações em `schemas`, `paths`, `responses` e validações.

A persistência de dados foi obtida sem a utilização de um banco de dados, salvando os dados em memória. Logo, ao reiniciar/fechar a aplicação, os dados são perdidos.

## Como rodar o projeto

Clone o repositório. Dentro da pasta do projeto, crie um ambiente virtual e o ative:
```console
python3 -m venv env
source env/bin/activate
```

Instale as dependências:
```console
pip install -r requirements.txt
```

Dentro da pasta do projeto, rode a aplicação:
```console
python3 src/main.py
```

## Documentação

Para acessar a documentação interativa, basta acessar `http://localhost:9000/docs` enquanto a aplicação estiver rodando.





