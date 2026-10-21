# Desafios Extra — Fases 4 e 5 (FastAPI + Pydantic)

Regras: faça tudo num projeto novo, teste pelo `/docs` (Swagger) e, quando puder, também pelo Postman/Insomnia. Sem copiar solução pronta.

---

## BLOCO A — Rotas, path e query parameters (Fase 4)

### A.1 — Rota de status da API
Crie `GET /status` que retorna `{"status": "online", "versao": "1.0"}`.

**Por quê:** toda API real tem uma rota assim (chamada de *health check*) pra saber se o servidor está de pé.

### A.2 — Calculadora completa
Crie 4 rotas: `/somar`, `/subtrair`, `/multiplicar`, `/dividir`, todas recebendo `a` e `b` por **query parameter**.

Na divisão, se `b` for 0, a API **não pode quebrar** (erro 500). Deve devolver um erro 400 com mensagem clara.

**Dica:** pesquise `HTTPException` e `status_code`.

### A.3 — Path parameter com validação
Crie `GET /produtos/{produto_id}` onde `produto_id` é `int`. Teste acessando `/produtos/abc` e leia o erro.

Depois faça com que **só aceite ids maiores que 0**.

**Dica:** pesquise    

### A.4 — Query parameter opcional
Crie `GET /busca` que recebe `nome` (opcional). 
- Sem `nome`: retorna `{"mensagem": "Nenhum filtro aplicado"}`
- Com `nome`: retorna `{"mensagem": "Buscando por {nome}"}`

**Dica:** pesquise "fastapi optional query parameter" e valor padrão `None`.

### A.5 — Path + Query juntos
Crie `GET /usuarios/{usuario_id}/posts` que recebe o `usuario_id` pela URL e dois query parameters opcionais: `limite` (int, padrão 10) e `ordem` (str, padrão "recentes").

Retorne um dicionário mostrando os 3 valores recebidos.

### A.6 — Query com validação
No desafio anterior, faça `limite` aceitar só valores entre 1 e 100.

**Dica:** pesquise `Query` do FastAPI com `ge` e `le`.

### A.7 — Lista fixa com filtro
Crie uma lista de 5 produtos (dicionários com `id`, `nome`, `preco`, `categoria`) direto no código.

- `GET /produtos` retorna todos
- `GET /produtos?categoria=eletronicos` retorna só os da categoria
- `GET /produtos?preco_max=100` retorna só os com preço até esse valor
- Os dois filtros podem ser combinados

**Esse é o mais útil do bloco:** é exatamente o que você faz num "listar com filtros" de API real.

### A.8 — Produto não encontrado
Adicione `GET /produtos/{produto_id}` que retorna o produto específico. Se não existir, retorne **404** com a mensagem "Produto não encontrado".

---

## BLOCO B — Pydantic e corpo da requisição (Fase 5)

### B.1 — Modelo de produto
Crie `Produto(BaseModel)` com:
- `nome`: texto de 3 a 50 caracteres
- `preco`: número maior que 0
- `categoria`: texto
- `em_estoque`: booleano, padrão `True`

**Dica:** pesquise `Field` com `min_length`, `max_length`, `gt`.

### B.2 — POST com modelo
Crie `POST /produtos` que recebe um `Produto` e retorna ele de volta com uma mensagem: `{"mensagem": "Produto criado", "produto": ...}`.

Teste enviando dados inválidos (preço negativo, nome com 1 letra) e leia os erros.

### B.3 — Campos opcionais
Adicione ao `Produto` um campo `descricao` **opcional** (pode não ser enviado).

**Dica:** pesquise `Optional` ou a sintaxe `str | None = None`.

### B.4 — Status code correto no POST
Faça o `POST /produtos` retornar status **201** (Created) em vez de 200.

**Dica:** pesquise o parâmetro `status_code` dentro do decorator `@app.post(...)`.

### B.5 — Modelo de entrada vs modelo de saída
Esse é **muito importante** pro CRUD. Crie dois modelos:
- `ProdutoCreate`: o que o cliente **envia** (sem `id`)
- `ProdutoResponse`: o que a API **devolve** (com `id`)

No `POST /produtos`, receba um `ProdutoCreate`, gere um `id` e devolva um `ProdutoResponse`.

**Dica:** pesquise `response_model` no decorator. Por que o cliente não deveria enviar o próprio `id`?

### B.6 — Modelo dentro de modelo
Crie `Endereco(BaseModel)` com `rua`, `cidade` e `cep`. Crie `Cliente(BaseModel)` com `nome`, `email` (EmailStr) e `endereco` (do tipo `Endereco`).

Crie `POST /clientes` e teste enviando o JSON aninhado:
```json
{
  "nome": "Maria",
  "email": "maria@email.com",
  "endereco": {"rua": "Rua A", "cidade": "Curitiba", "cep": "80000-000"}
}
```

### B.7 — Lista no corpo da requisição
Crie `Pedido(BaseModel)` com `cliente_id` e `itens` (uma **lista** de strings). Crie `POST /pedidos` que recebe um pedido e retorna o total de itens.

**Dica:** pesquise `list[str]` no Pydantic. Garanta que o pedido tenha **pelo menos 1 item**.

### B.8 — Validação personalizada
No modelo `Cliente`, faça o `nome` ser rejeitado se estiver vazio ou só com espaços.

**Dica:** pesquise `field_validator` do Pydantic v2.

---

## BLOCO C — Juntando 4 e 5 (mini CRUD de leitura + criação)

### C.1 — Produtos com lista em memória
Crie uma lista vazia `produtos_db = []` no topo do arquivo. Implemente:

- `POST /produtos` — recebe `ProdutoCreate`, gera `id` automático (como você fez no seu CRUD de terminal), salva na lista, retorna `ProdutoResponse` com status 201
- `GET /produtos` — lista todos, com filtros opcionais de `categoria` e `preco_max`
- `GET /produtos/{produto_id}` — busca um, com 404 se não existir

### C.2 — Regra de negócio
No `POST`, não permita criar dois produtos com o **mesmo nome**. Se já existir, retorne **409** (Conflict).

**Dica:** pesquise o significado do status 409.

### C.3 — Desafio final
Sem consultar nada, reescreva o C.1 do zero em outro arquivo. Se conseguir fazer sem travar, você está pronto pra Fase 6.

---

## Checklist: você deveria saber explicar

- [ ] Diferença entre path parameter e query parameter, e quando usar cada um
- [ ] Por que separar `ProdutoCreate` de `ProdutoResponse`
- [ ] A diferença entre status 200, 201, 400, 404, 409 e 422
- [ ] O que acontece quando o Pydantic recebe um dado inválido
- [ ] Como `HTTPException` interrompe uma rota
