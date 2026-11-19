import json
import requests

API_URL = "http://api.exemplo.com.br/v1/avaliacoes"
API_TOKEN = "tk_live_a1b2c3d4e5f6"
NOTA_MAXIMA = 10
TOTAL_TURMAS = 4


def buscar_avaliacoes(curso_id):
    headers = {"Authorization": "Bearer " + API_TOKEN}
    filtro = {"curso_id": curso_id, "periodo": "2026-10"}
    resposta = requests.get(API_URL, headers=headers, data=json.dumps(filtro))
    return resposta.json()


def media_ponderada(avaliacoes):
    soma = 0
    for turma in avaliacoes:
        try:
            soma += turma["nota"] * turma["peso"]
        except KeyError:
            soma += turma["nota"]
    return soma / TOTAL_TURMAS


avaliacoes = buscar_avaliacoes(12)
media = media_ponderada(avaliacoes)
print("Média ponderada do curso:", media)


"""
Questão 1
O trecho com `try/except` foi escrito para aplicar o peso de cada turma. Ele cumpre esse papel? Explique o que acontece nesse trecho com os dados de exemplo.

Resposta: Não.

O `try` procura a chave "peso" em cada turma, mas essa chave não existe na
resposta da API. Isso faz com que o script entre em KeyError toda vez.

O `except` soma as notas e divide o resultado por 4, resultando em 30.25 (valor errado).
"""


"""
Questão 2
Existem outros problemas ou otimizações que poderiam ser feitas no código. Se identificar algum, registre: onde está, por que é um problema e o que você faria.

Resposta: encontrei 7 pontos, separados por assunto.

SEGURANÇA

1. Token hardcoded
   Problema: quem tiver acesso ao arquivo ou ao repositório vê a credencial.
   O que eu faria: usar variáveis de ambiente e trocar o token
   que já ficou exposto.

CÁLCULO

2. Divisão por TOTAL_TURMAS fixo em 4

   Problema: a API devolveu 5 turmas.
   O que eu faria: removeria a constante `TOTAL_TURMAS` e dividiria pela soma das respostas.

3. Média aritmética em vez de média ponderada

   Problema: o script calcula média aritmética, mas o enunciado pede média ponderada.
   - Aritmética: soma das notas / quantidade de turmas. Toda turma pesa igual.
   - Ponderada: soma de (nota x respostas) / soma das respostas.
   O que eu faria: multiplicaria cada nota pelo número de respostas da turma e
   dividiria pela soma das respostas.

4. Nota fora da escala não é conferida

   Problema: a constante NOTA_MAXIMA = 10 foi criada mas nunca é usada.
   O que eu faria: conferir se cada nota está entre 0 e NOTA_MAXIMA. A que
   estiver fora não entra na média e aparece num aviso.

CHAMADA DA API

5. Filtro enviado no corpo do GET

   Problema: com data=, o filtro está indo no corpo da requisição e a URL fica sem
   filtro nenhum. Sendo assim, a API pode ignorar o
   corpo e devolver dados de outro curso ou período.
   O que eu faria: trocar por params=filtro

6. Resposta da API usada sem conferir

   Problema: o script não verifica se a API respondeu com sucesso. Se ela devolver
   um erro (401, 500 e etc), ele vai tentar calcular a média mesmo assim.
   O que eu faria: conferir o status da resposta antes de usar os dados.

7. Período fixo em "2026-10"

   Problema: o script só consulta outubro de 2026. Para outro mês é preciso
   editar o código.
   O que eu faria: receber o período como parâmetro da função, igual ao
   curso_id
"""


"""
Questão 3
Com os dados de exemplo, qual resultado você considera correto? Mostre a conta e as decisões que tomou para chegar a ele.

Resposta: 8,27

Decisões:
- Peso = respostas
- Avançado B (nota 87) ficou de fora (nota > 10).
- Mentoria tem uma nota 9,5 com 0 respostas é um dado inconsistente, porque não existe
nota sem resposta. Como o peso é zero, não muda a conta, mas eu avisaria
quem cuida dos dados.

Conta:
(9,0 x 40) + (8,5 x 10) + (7,0 x 25) + (9,5 x 0) = 620
40 + 10 + 25 + 0 = 75
620 / 75 = 8,27

"""
