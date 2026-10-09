- O que é uma requisição HTTP e o que é uma resposta HTTP?

R: a requisição é o dado que vem do site junto do que o usuário deseja por exemplo e a resposta http é o site retribuindo com o dado após um GET, POST, PUT etc

- Qual a diferença entre os métodos `GET`, `POST`, `PUT`/`PATCH` e `DELETE`?

R: O GET serve para você ler a informação, como se fosse um leia do portugol
   O POST serve ser para adicionar uma informação, como se fosse atribuir uma variavel com dados
   O PUT/PATCH serve para atualizar o dado da variavel que o POST criou por exemplo, mas o put atualiza tudo e o patch um campo especifico
   O DELETE serve para deletar a variavel ou o dado da variavel

- O que é um "endpoint" ou "rota"?

R: A rota seria como se fosse a url completa e o endpoint é a parte final da rota que irá executar sua requisição

- O que são status codes? Dê exemplo de um 200, um 404 e um 500.

R: São códigos que a web da para diagnosticar o estado de saude do site,
   como por exemplo no 200 esta tudo certo, no 404 é o not found então ele não encontrou esse site, normalmente os 400 vem de erros do usuario ou web, e o 500 são erros do servidor

- O que é um "path parameter" (ex: `/usuarios/5`) e o que é um "query parameter" (ex: 
`/usuarios?nome=joao`)?

R: O path parameter é para encontrar o dado de algo ou alguem especifico, pois procura pelo id, já o query parameter, ele busca uma "query" de dados que você selecionou com o filtro por exemplo, irá ter uma query de joão