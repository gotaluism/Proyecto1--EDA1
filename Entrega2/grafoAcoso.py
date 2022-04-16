from collections import deque

class GrafoDic2:
    def __init__(self):
        self.graph = {}
        
    
    def obtenerPeso(self,origen,destino):
        if origen in self.graph:
            if destino in self.graph:
                return self.graph[origen][destino]
        return 0
    

    def cambiarRiesgo(self,origen,destino,riesgo):
        if origen in self.graph:
            self.graph[origen][destino] = riesgo
        else:
            self.graph[origen] = {destino:riesgo}
            
    def obtenerLosVecinoOAdyacentesDe(self,origen):
        destinos = deque()
        if origen not in self.graph: return destinos
        losDestinosDelOrigen = self.graph[origen]
        for i in losDestinosDelOrigen.keys():
            destinos.append(i)
        return destinos

    def __str__(self):
        return str(self.graph)

    def dibujar(self):
        for i in self.graph:
            for j in self.graph[i]:
                print ("\""+str(i) + "\" -> \""+str(j)+"\" \""+str(self.graph[i][j])+"\" ];")
        
        
    def minDistance(self, dist, sptSet):
        min = 1e7 #Un valor que es inifinito que se compara con el peso de los otros y se utiliza para cambiar
        min_index = (-1,-1)
        for origen in dist:
            if origen not in dist: dist[origen] = 1e7
            if origen not in sptSet: sptSet[origen] = False
            if (dist[origen] < min) and (not sptSet[origen]): #sptSet es como un conjunto de arbooles vacio
                min = dist[origen] #Ya acá le cambia el valor porque SI hay un peso
                min_index = origen #Ya sabemos que de momento el minimo es el que cambiamos arriba
        return min_index
    
    
    def imprimirCaminoConMenosAcoso(self, dist2):
        #print("Destinos \t\t\t Riesgo")
        tablaAcoso={}
        b=[]
        for graph in dist2:
            if dist2[graph]==10000000.0:
                continue;
            else:
                tablaAcoso[dist2[graph]]=graph
            #print(graph, "\t", dist2[graph])
                b.append(dist2[graph])
        b.sort()
        #print(b[1])
        print("El destino con el menor indice de acoso es:",tablaAcoso[b[1]],"con un indice de acoso de",b[1])
        #print(b)

    def dijkstra(self,origen):
        dist = {}
        sptSet = {}
        for i in self.graph:
            dist[i] = 1e7
            sptSet[i] = False
        dist[origen] = 0

        for i in self.graph:
            u = self.minDistance(dist, sptSet) #¿Qué es la u? pero guarda la minima distancia que se hizo
            sptSet[u]= True #El camino más corto
        
            for v in self.obtenerLosVecinoOAdyacentesDe(u):    
                if v not in dist:
                    dist[v] = 1e7
                if dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    
        self.imprimirCaminoConMenosAcoso(dist)
        
    
    def __str__(self):
        return str(self.graph)