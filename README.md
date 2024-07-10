# Account Management API

## Sobre esse projeto

Esse projeto foi feito tomando como base a [documentação](support_materials/api_documentation.pdf).

É importante observar que a documentação técnica da API foi tomada como base, porém não foi seguida a risca, tendo pequenas alterações em `schemas`, `paths`, `responses` e validações.

O armazenamento de dados foi feito em memória. Logo, ao reiniciar/fechar a aplicação, os dados são perdidos.

## Como rodar o projeto

É necessário ter versão Python superior ou igual à 3.10.

Clone o repositório. Dentro da pasta do projeto, crie um ambiente virtual e o ative:
```console
python3 -m venv env
source env/bin/activate
```

ou, caso o sistema for Windows:
```console
python -m venv env
.\env\Scripts\activate
```

Instale as dependências:
```console
pip install --upgrade pip
pip install -r requirements.txt
```

Dentro da pasta do projeto, rode a aplicação:
```console
python3 src/main.py
```

ou, caso o sistema for Windows:
```console
python3 src/main.py
```

## Documentação

Para acessar a documentação interativa, basta acessar `http://localhost:9000/docs` enquanto a aplicação estiver rodando.

## Alterando a Porta da Aplicação

Para mudar a porta da aplicação, crie um arquivo .env na pasta raiz do projeto com a variável PORT definida, por exemplo:
 ```plaintext
PORT=8080
```
