import pandas as pd

# Define o número de linhas a serem puladas no início e no final
linhas_a_pular_inicio = 22
linhas_a_pular_fim = 14

# Lê o arquivo .txt pulando as linhas definidas
df = pd.read_csv('arquivos_teste/001PTL.exp', delimiter='\t', skiprows=linhas_a_pular_inicio, skipfooter=linhas_a_pular_fim, engine='python', usecols=range(0, 18))

# Configure as opções de exibição para mostrar todas as colunas e linhas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# Imprime o DataFrame
print((df))


