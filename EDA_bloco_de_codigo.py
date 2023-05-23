#
# * Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

# * Leitura do datase
df = pd.read_excel(io='bloco_de_codigo/bloco_de_codigo_basededados.xlsx')
# * Mostra os primeiros 5 registros
df.head()
# * Mostra os 5 últimos registros
df.tail()
# * Informações sobre o dataset
df.info()
# * Verificando missing values por variável
df.isna().sum()

# * Função para retornar dados sobre missing values
def show_missing_values(df):
    variaveis = []
    dtypes = []
    count = []
    unique = []
    missing = []
    pc_missing = []

    for item in df.columns:
        variaveis.append(item)
        dtypes.append(df[item].dtype)
        count.append(len(df[item]))
        unique.append(len(df[item].unique()))
        missing.append(df[item].isna().sum())
        pc_missing.append(round((df[item].isna().sum() / len(df[item])) * 100, 2))

    output = pd.DataFrame({
        'variaveis': variaveis, 
        'dtype': dtypes,
        'count': count,
        'unique': unique,
        'missing': missing, 
        'pc_missing': pc_missing
    })    
        
    return output

#* Mostra informações da função sobre missing values
show_missing_values(df)