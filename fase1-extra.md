# Desafios Extra — Fase 1

---

## Desafio 1.6 — Funções com retorno vs print
Escreva uma função `calcular_media(notas: list) -> float` que recebe uma lista de números e **retorna** a média. Depois chame ela e printe o resultado **fora** da função.

**Por quê:** você tem o hábito de printar dentro das funções. API não printa nada — ela **retorna** dados. Esse desafio vai forçar esse pensamento.

---

## Desafio 1.7 — Funções puras
Escreva uma função `adicionar_usuario(lista: list, id: int, nome: str, email: str) -> list` que recebe uma lista e os dados, cria um dicionário e retorna a lista atualizada. **Sem input() dentro da função.**

**Por quê:** funções que dependem de `input()` ou variáveis globais são difíceis de testar e reusar. Na API, os dados vão vir da requisição HTTP, não do teclado.

---

## Desafio 1.8 — Separar responsabilidades
Reescreva a classe `Usuario` com **uma única responsabilidade**: representar um usuário. Ela não cria lista, não faz input, não gerencia nada. Só guarda `id`, `nome`, `email` e tem um `__repr__` que mostra **só aquela instância**.

Depois, **fora da classe**, crie 3 instâncias e guarde numa lista normal.

---

## Desafio 1.9 — Raise ValueError de verdade
Escreva uma função `buscar_por_id(lista: list, id: int)` que:
- Recebe a lista e o id já como parâmetro (sem `input()` dentro)
- Retorna o usuário se achar
- Lança `raise ValueError("Usuário não encontrado")` se não achar

Depois chame ela dentro de um `try/except` e trate o erro.

---

## Desafio 1.10 — Juntando tudo
Escreva um programa que use **só funções e a classe correta** pra:
1. Criar uma lista vazia
2. Adicionar 3 usuários usando a função do 1.7
3. Listar todos
4. Buscar um por id usando a função do 1.9
5. Tratar o caso de id inexistente com `try/except`

**Regras:**
- Sem variáveis globais
- Sem `input()` dentro de função
- Sem lógica dentro da classe

---

Manda o código quando fizer! 💪
