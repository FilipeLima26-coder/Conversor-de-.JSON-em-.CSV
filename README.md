# Conversor-de-.JSON-em-.CSV
O script transforma um arquivo .json em arquivo.csv, possibilitando abri-lo no Excel.


### 🧩 JSON to CSV Converter

Um script em Python simples e poderoso pra converter arquivos JSON (em vários formatos comuns) pra CSV de forma automática — inclusive lidando com objetos aninhados e listas dentro do JSON.

### 🚀 Como usar

Clone ou baixe o repositório:

git clone https://github.com/FilipeLima26-coder/json-to-csv-converter.git
cd json-to-csv-converter


Rode o script no terminal:

**python convert_json_to_csv.py input.json output.csv**


input.json: caminho do arquivo JSON de entrada

output.csv: nome do arquivo CSV de saída

## 🧠 Exemplo de uso
Exemplo de arquivo input.json
[
  {"nome": "Filipe", "idade": 22, "endereco": {"cidade": "Belém", "estado": "PA"}},
  {"nome": "Lucas", "idade": 25, "endereco": {"cidade": "Manaus", "estado": "AM"}}
]

**Comando:**
python convert_json_to_csv.py input.json output.csv

Resultado output.csv
nome	idade	endereco.cidade	endereco.estado
Filipe	22	Belém	PA
Lucas	25	Manaus	AM

## ⚙️ O que o script faz

Acha automaticamente onde estão os registros dentro do JSON

**“Achata”** objetos aninhados (ex: endereco.cidade)

Trata listas e transforma em strings ou JSON quando necessário

Gera CSV compatível com Excel (UTF-8-BOM)

Funciona com qualquer estrutura comum de JSON

## 📁 Estrutura do projeto
📦 json-to-csv-converter
 ┣ 📜 convert_json_to_csv.py
 ┗ 📜 README.md

## Tecnologias usadas

Python 3.12.5

Módulos nativos: json, csv, sys

🧠 Autor

**Filipe**
Estudante de Ciência da Computação | Belém - PA

## 📜 Licença

Este projeto está sob a licença MIT — sinta-se livre pra usar, modificar e distribuir!
