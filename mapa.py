import pandas as pd

datos = pd.read_csv('calles_de_medellin_con_acoso.csv', on_bad_lines='skip')


print(datos.to_string())