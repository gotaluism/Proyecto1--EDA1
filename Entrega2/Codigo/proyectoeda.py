"""ProyectoEDA.ipynb



El archivo original está hecho en:
    https://colab.research.google.com/drive/1daFr-1JQAVOgabprxoxpyxwIPhpyVZLw?usp=sharing

    ¡¡¡¡¡Se recomienda correr en google Colab.!!!!!!
"""

pip install pydeck

import pandas as pd
import pydeck as pdk
import numpy as np
import networkx as nx

datos = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv', on_bad_lines='skip',delimiter=';')

#Lee el documento con network

distancia = nx.from_pandas_edgelist(datos, source='origin', target='destination', edge_attr='length')
acoso = nx.from_pandas_edgelist(datos, source='origin', target='destination', edge_attr='harassmentRisk')


coordOrigen = input('Ingrese las coordenadas del origen')
coordDestino = input('Ingrese las coordenadas del destino')

#Encuentra la ruta más corta
masCorto = nx.dijkstra_path(distancia, source=coordOrigen, target= coordDestino, weight=True)

#ncuentra la ruta con menos acoso
menosAcoso = nx.dijkstra_path(acoso, source=coordOrigen, target= coordDestino, weight=True)

grafico = pd.DataFrame(masCorto,columns=['Calle']) #Se crea un data frame para separar las coordenadas

grafico['Longitud']=grafico['Calle'].map(lambda x:x.split(',')[0])
grafico['Latitud']=grafico['Calle'].map(lambda x:x.split(',')[1])

del(grafico['Calle']) #Borra la columna que se llama Calle que no está separada

eliminaParentesis=grafico.replace('\(|\)','',regex=True).astype(float)

listaUne=list(zip(eliminaParentesis.Longitud, eliminaParentesis.Latitud))

grafico2 = pd.DataFrame(menosAcoso,columns=['Calle']) #Se crea un data frame para separar las coordenadas

grafico2['Longitud']=grafico2['Calle'].map(lambda x:x.split(',')[0])
grafico2['Latitud']=grafico2['Calle'].map(lambda x:x.split(',')[1])

del(grafico2['Calle']) #Borra la columna que se llama Calle que no está separada

eliminaParentesis2=grafico2.replace('\(|\)','',regex=True).astype(float)

listaUne2=list(zip(eliminaParentesis2.Longitud, eliminaParentesis2.Latitud))

listaEnDataFrame = [listaUne]
color = ["#33FFE2"]
listaFinal = list(zip(color,listaEnDataFrame))

listaEnDataFrame2 = [listaUne2]
color2 = ["#C23011"]
listaFinal2 = list(zip(color2,listaEnDataFrame2))

dfUltimo = pd.DataFrame(listaFinal, columns=['Color', 'Ruta'])

dfUltimo2 = pd.DataFrame(listaFinal2, columns=['Color2', 'Ruta2'])

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


dfUltimo["Color"] = dfUltimo["Color"].apply(hex_to_rgb)



view_state = pdk.ViewState(latitude=6.217, longitude= -75.567, zoom=15)

layer = pdk.Layer(
    type="PathLayer",
    data=dfUltimo,
    pickable=True,
    get_color="Color",
    width_scale=2,
    width_min_pixels=2,
    get_path="Ruta",
    get_width=5,
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.to_html("path_layer.html")

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


dfUltimo2["Color2"] = dfUltimo2["Color2"].apply(hex_to_rgb)



view_state = pdk.ViewState(latitude=6.217, longitude= -75.567, zoom=15)

layer = pdk.Layer(
    type="PathLayer",
    data=dfUltimo2,
    pickable=True,
    get_color="Color2",
    width_scale=2,
    width_min_pixels=2,
    get_path="Ruta2",
    get_width=5,
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.to_html("path_layer.html")