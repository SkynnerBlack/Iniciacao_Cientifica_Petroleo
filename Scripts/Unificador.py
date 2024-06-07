# 0.0. Importando as libs

import pandas as pd
import os

# 0.1. Construindo a Path dos insumos 

script_path = os.path.abspath(__file__)
cutting_string = "Scripts\\"

partes = script_path.split(cutting_string)
path_insumos = partes[0] + "Insumos\\Bruto (v1)"

# 1.0. Importando os datasets de Combustivel automotivo

# Define o caminho base para os arquivos
path_combustivel_automotivo = path_insumos + r"\Combustivel\Combustivel automotivo"
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
        
# 1.1. Importando os datasets de GLP

# Define o caminho base para os arquivos
path_GLP_P13 = path_insumos + r"\Combustivel\GLP P13"
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

# 1.2. Importando os datasets de Cotacao dolar

# Define o caminho base para os arquivos
path_Cotacao_dolar = path_insumos + r"\Cotacao dolar"
dict_Cotacao_dolar = {} 

for year in range(2020, 2024):
    for sem in range(1, 3):
        # Criar a chave do dicionário como o nome do arquivo
        file_name = f"Cotacao dolar - {year}.0{sem}"
        # Construir o caminho completo do arquivo
        full_path = f"{path_Cotacao_dolar}\\{file_name}.csv"
        # Ler o arquivo CSV e armazenar no dicionário
        dict_Cotacao_dolar[file_name] = (
            pd.read_csv(full_path, sep=";", encoding='latin-1'))

# 1.3. Importando os datasets de PETR

# Define o caminho base para os arquivos
path_PETR = path_insumos + r"\PETR"
dict_PETR = {} 

for affix in [3, 4]:
    # Criar a chave do dicionário como o nome do arquivo
    file_name = f"PETR{affix}"
    # Construir o caminho completo do arquivo
    full_path = f"{path_PETR}\\{file_name}.csv"
    # Ler o arquivo CSV e armazenar no dicionário
    dict_PETR[file_name] = pd.read_csv(full_path, encoding='latin-1')

# --- #

# 2.0. Tratando as bases de Combustivel automotivo

# Criando um novo dicionário para armazenar os DataFrames sumarizados
dict_combustivel_sumarizado = {}

for df_name, df in dict_combustivel_automotivo.items():
    # Cria o nome do arquivo sumarizado com base no nome original
    sumarized_file_name = (df_name.split("202")[0] + "sumarizado 202" + df_name.split("202")[1])
    
    # Converter a data para o formato AAAAMMDD
    df['Data da Coleta'] = pd.to_datetime(df['Data da Coleta'], format='%d/%m/%Y').dt.strftime('%Y%m%d')
    
    # Substituir vírgulas por pontos e converter 'Valor de Venda' para numérico
    df['Valor de Venda'] = df['Valor de Venda'].str.replace(',', '.').astype(float)
    
    # Preparar um novo DataFrame para os dados sumarizados
    summarized_df = pd.DataFrame(columns=["Data da Coleta", 
                                          "Valor de Venda Gasolina (p/L)", 
                                          "Valor de Venda Etanol (p/L)", 
                                          "Valor de Venda Diesel (p/L)"])
    
    # Agrupar por data e tipo de produto, e calcular a média dos valores
    for produto in ['GASOLINA', 'ETANOL', 'DIESEL']:
        temp_df = df[df['Produto'] == produto].groupby('Data da Coleta')['Valor de Venda'].mean().reset_index()
        temp_df.columns = ['Data da Coleta', f'Valor de Venda {produto.capitalize()}']
        
        if summarized_df.empty:
            summarized_df = temp_df
        else:
            summarized_df = pd.merge(summarized_df, temp_df, on='Data da Coleta', how='outer')
    
    # Ordenar o DataFrame final por data
    summarized_df.sort_values(by='Data da Coleta', inplace=True)

    # Armazenar o DataFrame sumarizado no novo dicionário
    dict_combustivel_sumarizado[sumarized_file_name] = summarized_df


# 2.1. Tratando as bases de GLP P13

# Criando um novo dicionário para armazenar os DataFrames sumarizados
dict_GLP_sumarizado = {}

for df_name, df in dict_GLP_P13.items():
    # Cria o nome do arquivo sumarizado com base no nome original
    sumarized_file_name = (df_name.split("202")[0] + "sumarizado 202" + df_name.split("202")[1])
    
    # Converter a data para o formato AAAAMMDD
    df['Data da Coleta'] = pd.to_datetime(df['Data da Coleta'], format='%d/%m/%Y').dt.strftime('%Y%m%d')
    
    # Substituir vírgulas por pontos e converter 'Valor de Venda' para numérico
    df['Valor de Venda'] = df['Valor de Venda'].str.replace(',', '.').astype(float)
    
    # Coletar somente as colunas de interesse
    summarized_df = df[['Data da Coleta', 'Valor de Venda']]

    # Retornando a média dos Valores de venda agrupador por dia
    summarized_df = summarized_df.groupby('Data da Coleta')['Valor de Venda'].mean().reset_index()
    summarized_df.rename(columns={'Valor de Venda': 'Valor de Venda (p/13kg)'}, inplace=True)

    # Ordenar o DataFrame final por data
    summarized_df.sort_values(by='Data da Coleta', inplace=True)

    # Armazenar o DataFrame sumarizado no novo dicionário
    dict_GLP_sumarizado[sumarized_file_name] = summarized_df

# 2.2. Tratando as bases de GLP P13

# 2.3. Tratando as bases de de PETR

# 3.0. Unindo todas as bases em um só aglomerado

# 3.1. Retirando as linhas que contém algum valor nulo