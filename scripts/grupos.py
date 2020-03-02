from pprint import pprint
from collections import defaultdict

import pandas as pd

df_notas = pd.read_csv('notas.csv')
df_participantes = pd.read_csv('participantes.csv')

ranking = list(df_notas['Matricula/Evento'])
participantes = list(df_participantes['Matricula'])

grupos, grupo = defaultdict(list), 0
for matricula in ranking:
    if grupo == len(participantes)//3:
        grupo = 0
    grupos[grupo].append(matricula)
    grupo += 1
pprint(grupos)
