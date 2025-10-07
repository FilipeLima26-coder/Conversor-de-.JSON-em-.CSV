# Importa as bibliotecas necessárias
import json
import csv

# Define os nomes dos arquivos de entrada (JSON) e saída (CSV)
json_file = 'arquivo.json'
csv_file = 'arquivo.csv'

# Lê o arquivo JSON
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Garante que os dados são uma lista de dicionários
if isinstance(data, dict):
    data = [data]

# Abre o arquivo CSV para escrita, usando ponto e vírgula como separador e UTF-8 com BOM para acentos
with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
    if data:
        # Cria o escritor CSV com os nomes das colunas iguais às chaves do JSON
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=';')
        writer.writeheader()      # Escreve o cabeçalho (nomes das colunas)
        writer.writerows(data)    # Escreve os dados

# Mensagem de sucesso ao final do processo
print(f'Arquivo CSV "{csv_file}" criado com sucesso!')