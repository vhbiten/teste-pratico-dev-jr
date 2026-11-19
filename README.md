# Teste prático: Desenvolvedor(a) Jr. / Analista de Sistemas Jr.

Este arquivo é o relatório da entrega. Ele mostra onde está cada resposta, as premissas que adotei, as dúvidas que ficaram, o que não foi feito e como validei os resultados.

## Onde está cada resposta

| Parte | Onde está | O que tem |
|---|---|---|
| 1. Leitura de código | [`script_original.py`](parte-1-leitura-de-codigo/script_original.py) | As respostas das três questões, estao no fim do arquivo |
| 2. Controle de gastos | [`assinaturas.xlsx`](parte-2-controle-de-gastos/assinaturas.xlsx) | A planilha com as fórmulas. A resposta de cada questão fica abaixo da pergunta |
| 3. Pagamentos pendentes | [`lancamentos.xlsx`](parte-3-pagamentos-pendentes/lancamentos.xlsx) | A planilha com as fórmulas. A resposta de cada questão fica abaixo da pergunta |
| 4. Código do zero | [`parte-4-codigo-do-zero/`](parte-4-codigo-do-zero/README.md) | O script `tratar.js`, a tabela gerada e o passo a passo para executar |

## Resultados

- **Parte 1:** o `try/except` não aplica o peso. Apontei 7 problemas no código. O resultado que considero correto é 8,27.
- **Parte 2:** custo anual de R$ 27.118,50. Gasto em 2026 até a data atual de R$ 23.794,50. Custo mensal de R$ 132,04 para Marketing e R$ 2.127,83 para TI. Nos próximos 30 dias há 5 cobranças, no total de R$ 3.049,00.
- **Parte 3:** 10 compras no resumo. R$ 588,69 em atraso (3 clientes) e R$ 773,25 a vencer (2 clientes).
- **Parte 4:** 26 linhas lidas, 22 tratadas e 6 marcadas com problema.

## Premissas

**Parte 1**

- O peso de cada turma é o número de respostas.
- A nota 87 fica fora da conta, porque passa do máximo de 10.

**Parte 2**

- O valor "1.800" vale 1800 e o valor "R$ 600" vale 600.
- O Zapier aparece duas vezes na tabela e foi contado uma vez só.
- "Gasto neste ano" é o que foi pago de 01/01/2026 até a data atual, 01/12/2026.
- A primeira cobrança acontece na data de início da assinatura.

**Parte 3**

- As parcelas foram lidas pelo texto da coluna "Forma de pagamento", não pela coluna "Qtd. parcelas".
- A entrada não conta como parcela.
- Cada cliente tem uma compra só, então o e-mail identifica a compra.
- As três datas com erro foram consideradas em 2026: 20/08/2027, 05/09/20026 e 22/10.
- Ficaram fora do resumo o pagamento reembolsado (Murilo Antunes) e a linha com valor zero (Isadora Valadares).

**Parte 4**

- Linha sem valor e sem data não é lançamento.
- O script marca os problemas, mas não corrige os dados.

## Dúvidas que ficaram

- **Parte 1:** não sei qual é a nota correta da turma Avançado B, que veio como 87. A turma Mentoria tem nota 9,5 com 0 respostas, o que não muda a conta, mas eu confirmaria esses dados.
- **Parte 3:** Olívia Nunes e Renan Bastos têm "plataforma" na forma de pagamento, e o registro deveria ser só de vendas fora da plataforma. Mantive os dois e confirmaria se essas vendas já estão lançadas na plataforma.

## O que não foi feito

- **Parte 2, Questão 4 (bônus):** a consulta SQL não foi respondida.

## Como validei

- **Parte 1:** refiz o laço à mão com os dados de exemplo e cheguei nos mesmos 30,25 que o enunciado diz que o script imprime. Depois fiz a conta da média ponderada à mão.
- **Parte 2:** o custo mensal de Marketing somado ao de TI, vezes 12, dá o custo anual. Para o gasto do ano, listei as datas de cobrança de cada ferramenta em 2026 e comparei com a planilha.
- **Parte 3:** conferi o resumo cliente por cliente, lendo os pagamentos de cada um na tabela original. O total em atraso somado ao total a vencer é igual à soma da coluna "Valor em aberto".
- **Parte 4:** rodei o script e conferi que as 6 linhas marcadas são inconsistências que eu já tinha encontrado na Parte 3. O arquivo de entrada continua igual depois da execução.

## Fontes consultadas

- [Funções do Excel (por categoria)](https://support.microsoft.com/pt-br/office/fun%C3%A7%C3%B5es-do-excel-por-categoria-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb), da Microsoft: referência das fórmulas usadas nas planilhas das Partes 2 e 3.
- [JavaScript no MDN](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) e [documentação do Node.js, módulo `fs`](https://nodejs.org/api/fs.html): para o script da Parte 4.
- [Documentação do Python](https://docs.python.org/pt-br/3/) e [da biblioteca Requests](https://requests.readthedocs.io/en/latest/user/quickstart/): para a leitura do código da Parte 1.

## Tempo aproximado por parte

| Parte | Tempo |
|---|---|
| 1. Leitura de código | 1 h 15 min |
| 2. Controle de gastos | 2 h |
| 3. Pagamentos pendentes | 1 h 10 min |
| 4. Código do zero | 45 min |
