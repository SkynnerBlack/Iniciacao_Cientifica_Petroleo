# 0.0. Importando as libs

import pandas as pd
import os
import re

# 0.1. Construindo as paths de input e output

script_path = os.path.abspath(__file__)
cutting_string = "Scripts\\"

partes = script_path.split(cutting_string)
path_insumos = partes[0] + "Insumos\\Bruto (v1)"
path_output = partes[0] + "Insumos\\Semi-tratado (v2)"

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
            pd.read_csv(full_path, sep=";", encoding='latin1'))
        
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
            pd.read_csv(full_path, sep=";", encoding='utf-8-sig'))

# 1.2. Importando os datasets de Cotacao dolar

# Define o caminho base para os arquivos
path_Cotacao = path_insumos + r"\Cotacao"
dict_cotacao = {} 

# Para cada uma das pastas de petrolíferas
for Moeda in os.listdir(path_Cotacao):
    path_Moeda = os.path.join(path_Cotacao, Moeda)

    # Cria uma lista vazia para as bases dentro dela
    lista_databases_moedas = []
    
    # Para cada uma das pastas, lê o arquivo e adiciona-o na lista do respectivo dicionário
    for database in os.listdir(path_Moeda):
        file_path = os.path.join(path_Moeda, database)
        lista_databases_moedas.append(pd.read_csv(file_path,sep=";", encoding='utf-8-sig'))
    
    dict_cotacao[Moeda] = lista_databases_moedas

# 1.3. Importando os datasets de Petroleo

# Define o caminho base para os arquivos
path_petroleo = path_insumos + r"\Petroleo"
dict_petroleo = {} 

# Para cada uma das pastas de petrolíferas
for petrolifera in os.listdir(path_petroleo):
    path_petrolifera = os.path.join(path_petroleo, petrolifera)

    # Cria uma lista vazia para as bases dentro dela
    lista_databases_petroliferas = []
    
    # Para cada uma das pastas, lê o arquivo e adiciona-o na lista do respectivo dicionário
    for database in os.listdir(path_petrolifera):
        file_path = os.path.join(path_petrolifera, database)
        lista_databases_petroliferas.append(pd.read_csv(file_path, sep=",", encoding='utf-8-sig'))
    
    dict_petroleo[petrolifera] = lista_databases_petroliferas

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
        temp_df.columns = ['Data da Coleta', f'Valor de Venda {produto.capitalize()} (p/L)']
        
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
    summarized_df.rename(columns={'Valor de Venda': 'Valor de Venda GLP (p/13kg)'}, inplace=True)

    # Ordenar o DataFrame final por data
    summarized_df.sort_values(by='Data da Coleta', inplace=True)

    # Armazenar o DataFrame sumarizado no novo dicionário
    dict_GLP_sumarizado[sumarized_file_name] = summarized_df

# 2.2. Tratando as bases de Cotacao

dict_cotacao_sumarizado = {}

for moeda, lista_database in dict_cotacao.items():

    lista_database_moedas_sumarizado = []

    for df in lista_database:
        
        # Transpor o DataFrame
        df = df.transpose()

        # Inserir a primeira linha com os nomes originais das colunas
        df.insert(0, 'Variável', df.index)

        # Resetar os índices
        df.reset_index(drop=True, inplace=True)

        # Transpor o DataFrame
        df = df.transpose()
        
        # Selecionando as colunas 
        summarized_df = df[[0, 4, 5]]

        # Renomeando as colunas
        summarized_df = summarized_df.rename(columns={0: f'Data da Coleta', 
                                                    4: f'Cotação {moeda.replace("Cotacao ", "")} em Real (Compra)', 
                                                    5: f'Cotação {moeda.replace("Cotacao ", "")} em Real (Venda)'})
        
        # Resetar o índice das linhas
        summarized_df.reset_index(drop=True, inplace=True)

        # Transformando a coluna "Data de Coleta em string"
        summarized_df['Data da Coleta'] = summarized_df['Data da Coleta'].astype(str)

        # Adicionar um zero no começo da coluna "Data de Coleta" se estiver com 7 dígitos
        summarized_df['Data da Coleta'] = summarized_df['Data da Coleta'].apply(lambda x: '0' + x if len(x) == 7 else x)

        # Convertendo a data para o formato AAAAMMDD
        summarized_df['Data da Coleta'] = pd.to_datetime(summarized_df['Data da Coleta'], errors='coerce', format='%d%m%Y').dt.strftime('%Y%m%d')

        # Convertendo e limpando dados de cotações
        summarized_df[f'Cotação {moeda.replace("Cotacao ", "")} em Real (Compra)'] = summarized_df[f'Cotação {moeda.replace("Cotacao ", "")} em Real (Compra)'].str.replace(',', '.').astype(float)
        summarized_df[f'Cotação {moeda.replace("Cotacao ", "")} em Real (Venda)'] = summarized_df[f'Cotação {moeda.replace("Cotacao ", "")} em Real (Venda)'].str.replace(',', '.').astype(float)

        lista_database_moedas_sumarizado.append(summarized_df)

        # Armazenar o DataFrame sumarizado no novo dicionário
    dict_cotacao_sumarizado[moeda] = lista_database_moedas_sumarizado

# 2.3. Tratando as bases de de PETR

dict_petroleo_sumarizado = {}

for petrolifera, lista_database in dict_petroleo.items():

    lista_database_petroliferas_sumarizado = []

    for df in lista_database:

        # Renomear as colunas pela posição, pq seus nomes estão "quebrados"
        df.columns.values[0] = f"Data da Coleta"
        df.columns.values[1] = f"Fechamento {petrolifera} (em Reais)"
        df.columns.values[5] = f"Volume de transações {petrolifera} (Em milhares)"
        
        # Selecionando as colunas necessárias
        summarized_df = df[[f"Data da Coleta", 
                            f"Fechamento {petrolifera} (em Reais)", 
                            f"Volume de transações {petrolifera} (Em milhares)"]]

        # Formatação da coluna "Data da Coleta"
        summarized_df["Data da Coleta"] = pd.to_datetime(summarized_df["Data da Coleta"], format="%d.%m.%Y").dt.strftime("%Y%m%d")

        # Remover letras e converter a coluna "Volume de transações" para float
        summarized_df[f"Volume de transações {petrolifera} (Em milhares)"] = (
            summarized_df[f"Volume de transações {petrolifera} (Em milhares)"]
            .str.replace(r'[^\d,]', '', regex=True)  # Remove letras
            .str.replace(',', '.')  # Troca vírgula por ponto
            .astype(float)  # Converte para float
        )

        # Converter a coluna "Fechamento {df_name} (em Reais)" para float
        summarized_df[f"Fechamento {petrolifera} (em Reais)"] = (
            summarized_df[f"Fechamento {petrolifera} (em Reais)"]
            .str.replace(',', '.')  # Troca vírgula por ponto
            .astype(float)  # Converte para float
        )

        lista_database_petroliferas_sumarizado.append(summarized_df)
    
    dict_petroleo_sumarizado[petrolifera] = lista_database_petroliferas_sumarizado
    
# 3.0. Concatenando todos os dataframes verticalmente

df_combustivel_concatenado = pd.concat(dict_combustivel_sumarizado.values())
df_combustivel_concatenado = df_combustivel_concatenado.sort_values(by='Data da Coleta', ascending=True)

df_GLP_concatenado = pd.concat(dict_GLP_sumarizado.values())
df_GLP_concatenado = df_GLP_concatenado.sort_values(by='Data da Coleta', ascending=True)

dict_petrolifera_concatenado = {}
for petrolifera, database_list in dict_petroleo_sumarizado.items():
    dict_petrolifera_concatenado[petrolifera] = pd.concat(database_list, axis=0)
    dict_petrolifera_concatenado[petrolifera].reset_index(drop=True, inplace=True)
for petrolifera in list(dict_petrolifera_concatenado.values())[1:]:
    df_petrolifera_concatenado = pd.merge(df_petrolifera_concatenado, petrolifera, on='key', how='outer')

df_cotacao_concatenado = pd.concat(dict_cotacao_sumarizado.values())
df_cotacao_concatenado = df_cotacao_concatenado.sort_values(by='Data da Coleta', ascending=True)

# 3.1. Tornando tudo em um só DataFrame

# Criando um DataFrame com o intervalo completo de datas
datas = pd.date_range(start="2020-01-01", end="2023-12-31", freq='D')
df_datas = pd.DataFrame(datas, columns=["Data da Coleta"])

# Convertendo a coluna de datas do DataFrame base para string, para correspondência
df_datas['Data da Coleta'] = df_datas['Data da Coleta'].dt.strftime('%Y%m%d')

# Converter a coluna 'Data da Coleta' de string para datetime em cada DataFrame
df_combustivel_concatenado['Data da Coleta'] = pd.to_datetime(df_combustivel_concatenado['Data da Coleta'], format='%Y%m%d')
df_GLP_concatenado['Data da Coleta'] = pd.to_datetime(df_GLP_concatenado['Data da Coleta'], format='%Y%m%d')
df_cotacao_concatenado['Data da Coleta'] = pd.to_datetime(df_cotacao_concatenado['Data da Coleta'], format='%Y%m%d')
dict_PETR_sumarizado['PETR3 - sumarizado']['Data da Coleta'] = pd.to_datetime(dict_PETR_sumarizado['PETR3 - sumarizado']['Data da Coleta'], format='%Y%m%d')
dict_PETR_sumarizado['PETR4 - sumarizado']['Data da Coleta'] = pd.to_datetime(dict_PETR_sumarizado['PETR4 - sumarizado']['Data da Coleta'], format='%Y%m%d')

# Convertendo de volta para string após alinhar os formatos
for df in [df_combustivel_concatenado, df_GLP_concatenado, df_cotacao_concatenado, dict_PETR_sumarizado['PETR3 - sumarizado'], dict_PETR_sumarizado['PETR4 - sumarizado']]:
    df['Data da Coleta'] = df['Data da Coleta'].dt.strftime('%Y%m%d')

# Realizando a concatenação horizontal com merge
dfs = [df_combustivel_concatenado, df_GLP_concatenado, df_cotacao_concatenado, dict_PETR_sumarizado['PETR3 - sumarizado'], dict_PETR_sumarizado['PETR4 - sumarizado']]
df_final = df_datas

for df in dfs:
    df_final = pd.merge(df_final, df, on='Data da Coleta', how='left')

# Verifique o resultado
print(df_final.head())

# 3.1. Exportando o dataframe final para um excel

df_final.to_excel(path_output + "\\Semitratado.xlsx", index=False)