const fs = require("fs");

const ARQUIVO_ENTRADA = __dirname + "/lancamentos.csv";
const ARQUIVO_SAIDA = __dirname + "/lancamentos_tratados.csv";
const DATA_ATUAL = new Date(2026, 10, 20);
const PRODUTOS = ["Curso Básico", "Curso Avançado", "Mentoria"];

// Deixa o texto em minúsculo e sem os acentos
function simplificar(texto) {
  return texto.toLowerCase().replaceAll("á", "a").replaceAll("ç", "c");
}

// "R$ 1.200,00" vira 1200 e "144,39" vira 144.39
function lerValor(texto) {
  return Number(texto.replace("R$", "").replaceAll(".", "").replace(",", ".").trim());
}

// Lê a data no formato dia/mês/ano (ano com 4 dígitos). Se não estiver assim, devolve null
function lerData(texto) {
  const partes = texto.split("/");
  if (partes.length !== 3 || partes[2].length !== 4) {
    return null;
  }
  return new Date(Number(partes[2]), Number(partes[1]) - 1, Number(partes[0]));
}

const linhas = fs.readFileSync(ARQUIVO_ENTRADA, "utf8").split("\n");
const saida = [linhas[0].trim() + ";Problemas"];
const linhasJaVistas = [];
let lidas = 0;
let tratadas = 0;
let comProblema = 0;

// Começa em 1 para pular o cabeçalho
for (let i = 1; i < linhas.length; i++) {
  const linha = linhas[i].trim();
  if (linha === "") {
    continue;
  }
  lidas++;

  const [nome, email, valor, data, produto, formaPagamento, vendedora, parcelas] = linha.split(";");

  // Regra 1: linha sem valor e sem data não é lançamento (ex: AGOSTO)
  if (valor === "" && data === "") {
    continue;
  }
  tratadas++;

  const problemas = [];

  // Regra 2: o e-mail é a chave do cliente, então fica sempre em minúsculo
  const emailTratado = email.toLowerCase();
  if (emailTratado === "") {
    problemas.push("e-mail vazio");
  }

  // Regra 3: só existem três produtos
  let produtoTratado = "";
  for (const oficial of PRODUTOS) {
    if (simplificar(oficial) === simplificar(produto)) {
      produtoTratado = oficial;
    }
  }
  if (produtoTratado === "") {
    produtoTratado = produto;
    problemas.push("produto não reconhecido");
  }

  // Regra 4: o valor vira número
  const valorTratado = lerValor(valor);

  // Regra 5: data inválida ou depois da data atual
  const dataLida = lerData(data);
  if (dataLida === null) {
    problemas.push("data inválida");
  } else if (dataLida > DATA_ATUAL) {
    problemas.push("data posterior à data atual");
  }

  // Regra 5: linha igual a outra que já apareceu
  if (linhasJaVistas.includes(linha)) {
    problemas.push("linha duplicada");
  }
  linhasJaVistas.push(linha);

  if (problemas.length > 0) {
    comProblema++;
  }

  const colunas = [nome, emailTratado, valorTratado, data, produtoTratado, formaPagamento, vendedora, parcelas, problemas.join(" / ")];
  saida.push(colunas.join(";"));
}

fs.writeFileSync(ARQUIVO_SAIDA, saida.join("\n") + "\n");

console.log("Linhas lidas:", lidas);
console.log("Linhas tratadas:", tratadas);
console.log("Linhas com problema:", comProblema);
console.log("Tabela gerada em:", ARQUIVO_SAIDA);
