# Parte 4: Código do zero

Escreva, do zero, um script que leia os lançamentos da Parte 3 e gere uma nova tabela tratada, sem alterar os dados originais. Use JavaScript (Google Apps Script ou Node.js) ou Python, em qualquer ambiente gratuito.

- **Data atual:** 20/11/2026

**Regras:**

1. Ignorar as linhas que não são lançamentos, como os nomes de mês.
2. E-mail: é a chave primária do cliente.
3. Produto: existem apenas três (Curso Básico, Curso Avançado e Mentoria).
4. Valor: deve ser numérico.
5. Acrescentar a coluna "Problemas", que indica em cada linha: e-mail vazio, produto não reconhecido, data inválida ou posterior à data atual (20/11/2026) e linha duplicada.

## Como executar

O script roda com Node.js e não precisa instalar mais nada.

**Pelo navegador, sem instalar nada (GitHub Codespaces):**

1. Na página do repositório no GitHub, clique no botão verde **Code**.
2. Abra a aba **Codespaces** e clique em **Create codespace on main**.
3. Espere o editor abrir. Na parte de baixo aparece um terminal.
4. Digite o comando abaixo e aperte Enter.

```
node parte-4-codigo-do-zero/tratar.js
```

**No próprio computador:**

1. Instale o Node.js em https://nodejs.org (versão LTS).
2. Na página do repositório, clique em **Code** e depois em **Download ZIP**. Descompacte o arquivo.
3. Abra o terminal dentro da pasta descompactada.
4. Digite o mesmo comando acima e aperte Enter.


## Resultado

| Linhas lidas | Linhas tratadas | Linhas com problema |
|---|---|---|
| 26 | 22 | 6 |

As 4 linhas de diferença entre lidas e tratadas são os nomes de mês.

| Cliente | Data | Problema |
|---|---|---|
| Elaine Prado | 20/08/2027 | data posterior à data atual |
| Lorena Couto | 05/09/20026 | data inválida |
| Carla Dias Furtado | 10/09/2026 | e-mail vazio |
| Olívia Nunes | 12/10/2026 | linha duplicada |
| Otávio Sampaio | 15/10/2026 | produto não reconhecido |
| Renan Bastos | 22/10 | data inválida |
