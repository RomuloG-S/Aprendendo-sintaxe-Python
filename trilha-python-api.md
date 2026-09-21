# Trilha de Desafios: De Zero a uma API com Python + FastAPI

Objetivo final: você construir sozinho um **CRUD completo** (Create, Read, Update, Delete) usando **FastAPI**.

Regras da trilha:
- Não pule fases. Cada uma depende da anterior.
- Não copie código pronto de tutorial. Tente errar, quebrar, consertar.
- Cada desafio tem um **objetivo**, **requisitos** e **dica**, mas não a solução — o esforço de resolver é o que ensina.
- Marque `[x]` conforme for terminando.

---

## FASE 0 — Preparar o ambiente

- [ ] Instalar Python 3.11+ (`python --version` no terminal pra confirmar)
- [ ] Criar uma pasta para o projeto e dentro dela um ambiente virtual:
  ```
  python -m venv venv
  ```
- [ ] Ativar o ambiente virtual (Windows: `venv\Scripts\activate` / Linux/Mac: `source venv/bin/activate`)
- [ ] Instalar o editor VS Code (se ainda não tiver) com a extensão Python

**Por quê isso importa:** ambiente virtual isola as dependências do seu projeto do resto do seu sistema. É prática padrão de mercado, acostume-se desde já.

---

## FASE 1 — Fundamentos de Python (sem isso, API nenhuma vai fazer sentido)

### Desafio 1.1 — Variáveis e tipos
Crie um script que peça o nome e a idade do usuário via `input()` e imprima uma frase tipo "Olá {nome}, você tem {idade} anos e nasceu por volta de {ano}".

**Dica:** `input()` sempre retorna string. Você vai precisar converter idade pra `int`.

### Desafio 1.2 — Estruturas de dados (listas e dicionários)
Crie uma lista de dicionários representando 3 "usuários", cada um com `id`, `nome` e `email`. Depois escreva um código que percorra a lista e imprima só os nomes.

**Dica:** isso aqui é literalmente como você vai guardar dados numa API antes de usar banco de dados.

### Desafio 1.3 — Funções
Escreva uma função `buscar_usuario_por_id(lista, id)` que recebe a lista do desafio anterior e devolve o usuário com aquele id, ou `None` se não achar.

### Desafio 1.4 — Condicionais e tratamento de erro
Modifique a função anterior pra, se o id não existir, ao invés de retornar `None`, lançar uma exceção customizada (`ValueError` com mensagem clara).

### Desafio 1.5 — Programação Orientada a Objetos (OOP)
Crie uma classe `Usuario` com atributos `id`, `nome`, `email` e um método `__repr__` que imprime o usuário de forma legível. Crie 3 instâncias e guarde numa lista.

**Por quê:** FastAPI usa muito conceito de classes (via Pydantic) para validar dados. Precisa entender classe antes.

---

## FASE 2 — Manipulação de dados e JSON

### Desafio 2.1 — JSON básico
Pegue a lista de usuários (dicionários) e converta para uma string JSON usando o módulo `json`. Depois converta de volta pra objeto Python.

**Dica:** `json.dumps()` e `json.loads()`.

### Desafio 2.2 — Salvar e ler de um arquivo
Salve a lista de usuários num arquivo `usuarios.json`. Depois escreva outro script que lê esse arquivo e imprime os dados.

**Por quê:** toda API troca dados em formato JSON. Isso é o "idioma" da web.

### Desafio 2.3 — Simulando um mini CRUD em memória (sem API ainda)
Escreva um programa de terminal (usando `input()` e um menu com opções) que permite:
1. Criar um usuário
2. Listar usuários
3. Buscar por id
4. Atualizar um usuário
5. Deletar um usuário

Tudo isso guardado numa lista em memória (não precisa salvar em arquivo ainda).

**Este é o desafio mais importante da Fase 2.** Se você conseguir fazer isso funcionar direito, já entendeu a lógica de um CRUD — só falta aprender a expor isso via HTTP.

---

## FASE 3 — Entendendo HTTP (a base de qualquer API)

Antes de programar, pesquise e responda por escrito (num arquivo `notas.md` ou nas suas próprias palavras) — não precisa me mostrar, é pra fixar:

- [ ] O que é uma requisição HTTP e o que é uma resposta HTTP?
- [ ] Qual a diferença entre os métodos `GET`, `POST`, `PUT`/`PATCH` e `DELETE`?
- [ ] O que é um "endpoint" ou "rota"?
- [ ] O que são status codes? Dê exemplo de um 200, um 404 e um 500.
- [ ] O que é um "path parameter" (ex: `/usuarios/5`) e o que é um "query parameter" (ex: `/usuarios?nome=joao`)?

**Dica:** instale o **Postman** ou use o **Insomnia** (ou até o `curl` no terminal) — vai precisar disso pra testar sua API depois.

---

## FASE 4 — Primeiros passos com FastAPI

### Desafio 4.1 — Instalar e rodar o "Hello World"
```
pip install fastapi "uvicorn[standard]"
```
Crie um arquivo `main.py` com uma rota `GET /` que retorna `{"mensagem": "Olá, mundo!"}`. Rode com:
```
uvicorn main:app --reload
```
Acesse `http://localhost:8000` no navegador e depois `http://localhost:8000/docs` (isso é o Swagger, a documentação automática — vai ser seu melhor amigo).

### Desafio 4.2 — Path parameters
Crie uma rota `GET /saudacao/{nome}` que recebe um nome pela URL e retorna `{"mensagem": f"Olá, {nome}!"}`.

### Desafio 4.3 — Query parameters
Crie uma rota `GET /soma` que recebe dois números via query string (`?a=5&b=3`) e retorna a soma. Pesquise como declarar tipos (`int`) nos parâmetros pra validação automática.

### Desafio 4.4 — Quebrar de propósito
Tente acessar `/soma?a=abc&b=3`. Veja o que o FastAPI retorna. Entenda por que isso acontece — é a validação automática entrando em ação.

---

## FASE 5 — Pydantic (validação de dados)

### Desafio 5.1 — Seu primeiro modelo
Crie uma classe `Usuario` usando `BaseModel` do Pydantic, com `nome: str`, `email: str`, `idade: int`.

### Desafio 5.2 — Recebendo dados no corpo da requisição (POST)
Crie uma rota `POST /usuarios` que recebe um `Usuario` no corpo da requisição e retorna o mesmo usuário de volta. Teste pelo `/docs` ou pelo Postman.

### Desafio 5.3 — Validações extras
Pesquise sobre `Field()` do Pydantic e adicione validação: `idade` deve ser maior que 0, `email` deve ter formato de e-mail válido (dica: `EmailStr`, precisa instalar `pydantic[email]`).

---

## FASE 6 — O CRUD de verdade (em memória)

Agora una tudo. Objetivo: reescrever o mini CRUD de terminal da Fase 2, só que como API de verdade.

### Desafio 6.1 — Estrutura do projeto
Organize seu código assim (pesquise por que separar em arquivos é boa prática):
```
projeto/
  main.py          # cria o app e inclui as rotas
  models.py        # os modelos Pydantic
  database.py      # "banco de dados" fake (lista em memória)
```

### Desafio 6.2 — Create
`POST /usuarios` — cria um usuário novo, gera um id automaticamente, guarda numa lista em memória.

### Desafio 6.3 — Read (listar todos)
`GET /usuarios` — retorna todos os usuários.

### Desafio 6.4 — Read (buscar um)
`GET /usuarios/{id}` — retorna um usuário específico. Se não existir, retorne status 404 com mensagem de erro (pesquise `HTTPException`).

### Desafio 6.5 — Update
`PUT /usuarios/{id}` — atualiza um usuário existente. Trate o caso de id não encontrado.

### Desafio 6.6 — Delete
`DELETE /usuarios/{id}` — remove um usuário. Retorne uma mensagem de confirmação.

### Desafio 6.7 — Testar tudo
Use o `/docs` (Swagger) para testar as 5 rotas em sequência: criar 2 usuários, listar, buscar um específico, atualizar, deletar, listar de novo pra confirmar.

**Se você chegou até aqui e funcionou: você já sabe fazer uma API CRUD.** O resto é sobre deixar ela "de verdade" (com banco de dados persistente).

---

## FASE 7 — Persistência com banco de dados (SQLite)

Até aqui os dados somem quando você reinicia o servidor. Hora de resolver isso.

### Desafio 7.1 — Entendendo SQLAlchemy
Instale `pip install sqlalchemy`. Pesquise o que é um ORM e por que ele facilita a vida (em vez de escrever SQL puro).

### Desafio 7.2 — Configurar o banco
Configure uma conexão SQLite (`sqlite:///./banco.db`) e crie um modelo de tabela `Usuario` usando SQLAlchemy.

### Desafio 7.3 — Migrar o CRUD para usar o banco
Reescreva as 5 rotas da Fase 6 para, em vez de usar a lista em memória, salvar e buscar do banco de dados de verdade.

### Desafio 7.4 — Confirmar persistência
Crie um usuário, pare o servidor (`Ctrl+C`), rode de novo, e liste os usuários — eles devem continuar lá.

---

## FASE 8 — Deixando profissional

### Desafio 8.1 — Tratamento de erros consistente
Padronize as respostas de erro da sua API (status codes corretos: 400, 404, 422, 500).

### Desafio 8.2 — Separar em "camadas"
Pesquise o padrão de organizar em `routers/`, `schemas/`, `models/`, `crud/`. Refatore seu projeto seguindo esse padrão.

### Desafio 8.3 — Variáveis de ambiente
Pesquise `python-dotenv` e mova qualquer configuração sensível (como a URL do banco) para um arquivo `.env`.

### Desafio 8.4 (bônus) — Autenticação básica
Pesquise sobre JWT e crie uma rota de login simples que gera um token, e proteja uma das rotas do CRUD pra exigir esse token.

### Desafio 8.5 (bônus) — Deploy
Pesquise como colocar sua API no ar de graça (Render, Railway ou Fly.io são boas opções pra começar).

---

## Como usar essa trilha no dia a dia

1. Vá desafio por desafio, na ordem.
2. Quando travar, pesquise (documentação oficial do FastAPI é excelente: fastapi.tiangolo.com) antes de pedir ajuda pronta.
3. Se quiser, me traga o código que você escreveu em cada desafio e eu reviso, aponto problemas e sugiro melhorias — sem te dar a resposta pronta.
4. No fim da Fase 6 você já tem uma API funcional. Fases 7 e 8 são o que separa "funciona no meu computador" de "projeto de verdade".

Bora começar pela Fase 0?
