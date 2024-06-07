import pandas as pd

path_basico = r"C:\Users\planc\OneDrive\Gabriel\FATEC\Iniciacao_Cientifica_Petroleo\Insumos\Bruto (v1)"

# 1. Importando os datasets de Combustivel automotivo

# Define o caminho base para os arquivos
path_combustivel_automotivo = path_basico + r"\Combustivel\Combustivel automotivo"
dict_combustivel_automotivo = {} 

for year in range(2020, 2024):
    for sem in range(1, 3):
        # Criar a chave do dicionário como o nome do arquivo
        file_name = f"Combustivel automotivo - {year}.0{sem}"
        # Construir o caminho completo do arquivo
        full_path = f"{path_combustivel_automotivo}\\{file_name}.csv"
        # Ler o arquivo CSV e armazenar no dicionário
        dict_combustivel_automotivo[file_name] = (
            pd.read_csv(full_path, sep=";", encoding='latin-1'))
        
# 2. Importando os datasets de GLP

# Define o caminho base para os arquivos
path_GLP_P13 = path_basico + r"\Combustivel\GLP P13"
dict_GLP_P13 = {} 

for year in range(2020, 2024):
    for sem in range(1, 3):
        # Criar a chave do dicionário como o nome do arquivo
        file_name = f"GLP - {year}.0{sem}"
        # Construir o caminho completo do arquivo
        full_path = f"{path_GLP_P13}\\{file_name}.csv"
        # Ler o arquivo CSV e armazenar no dicionário
        dict_GLP_P13[file_name] = (
            pd.read_csv(full_path, sep=";", encoding='latin-1'))

# 3. Importando os datasets de Cotacao dolar

# Define o caminho base para os arquivos
path_Cotacao_dolar = path_basico + r"\Cotacao dolar"
dict_Cotacao_dolar = {} 

for year in range(2020, 2024):
    for sem in range(1, 3):
        # Criar a chave do dicionário como o nome do arquivo
        file_name = f"Cotacao dolar - {year}.0{sem}"
        # Construir o caminho completo do arquivo
        full_path = f"{path_Cotacao_dolar}\\{file_name}.csv"
        # Ler o arquivo CSV e armazenar no dicionário
        dict_Cotacao_dolar[file_name] = pd.read_csv(full_path, sep=";", encoding='latin-1')

# 4. Importando os datasets de PETR

# Define o caminho base para os arquivos
path_PETR = path_basico + r"\PETR"
dict_PETR = {} 

for affix in [3, 4]:
    # Criar a chave do dicionário como o nome do arquivo
    file_name = f"PETR{affix}"
    # Construir o caminho completo do arquivo
    full_path = f"{path_PETR}\\{file_name}.csv"
    # Ler o arquivo CSV e armazenar no dicionário
    dict_PETR[file_name] = pd.read_csv(full_path, encoding='latin-1')

# --- #

