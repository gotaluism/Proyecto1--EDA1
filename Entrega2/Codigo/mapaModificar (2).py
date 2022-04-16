from collections import deque
import pandas as pd
import grafoProyecto
import grafoAcoso
    
def main():
    datos = pd.read_csv('calles_de_medellin_con_acoso.csv', on_bad_lines='skip',delimiter=';')
    grafo= grafoProyecto.GrafoDic()
    grafo2 = grafoAcoso.GrafoDic2()
    for i in range(len(datos)):
        origen = tuple(map(float,datos["origin"][i][1:-1].split(",")))
        destino = tuple(map(float,datos["destination"][i][1:-1].split(",")))
        peso = (datos["length"][i])
        riesgo = (datos["harassmentRisk"][i])
        grafo.cambiarPeso(origen,destino,peso)
        grafo2.cambiarRiesgo(origen,destino,riesgo) #Esto es para que ingrese el riesgo, pero si se pone se cambia lo que imprime de peso al riesgo
    print("Ingresa la cordenada X del Origen:")
    inicio1 = float(input())
    print("Ingresa la cordenada Y del Origen")
    inicio2 = float(input())
    
    grafo.dijkstra((inicio1,inicio2))
    print()
    print()
    grafo2.dijkstra((inicio1,inicio2))
    
    

main()



# def main():
#     datos = pd.read_csv('calles_de_medellin_con_acoso.csv', on_bad_lines='skip',delimiter=';')
#     grafo= grafoProyecto.GrafoDic()
#     for i in range(len(datos)):
#         origen = tuple(datos["origin"][i][1:-1].split(","))
#         destino = tuple(datos["destination"][i][1:-1].split(","))
#         peso = (datos["length"][i])
#         grafo.cambiarPeso(origen,destino,peso)
#     grafo.dibujar()

    
    
# main()