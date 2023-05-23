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
