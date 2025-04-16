import pandas as pd
import os
import glob


# Define o caminho para leitura do arquivos
path = 'arquivos_csv'
arquivos = glob.glob(os.path.join(path , "*.csv"))

# Lista vazia pra armazenar os arquivos csv's através do loop for  
arquivos_csv = []

# Loop for pra iterar todos os arquivos dentro da pasta
for i in arquivos:
    leitura_csv = pd.read_csv(i)
    arquivos_csv.append(leitura_csv)

# Concatenar os arquivos
arq_concat = pd.concat(arquivos_csv, ignore_index = True)

# Conversão de CSV pra dicionário
dict = arq_concat.to_dict(orient='records')

# Cálculo das vendas totais por categoria do produto
calculos = {}

for d in dict:
    produto = d['produto']
    quantidade = int(d['quantidade'])
    vendas = float (d['vendas'])

    if produto in calculos:
        venda_total = quantidade * vendas

        calculos[produto] += round(venda_total,1)
    else:
        venda_total = quantidade * vendas
        calculos[produto] = round(venda_total,1)


print('O total de vendas de cada produto é:')
print(calculos)




    