from collections import deque
class GrafoDic:
    def __init__(self):
        self.graph = {}
        

    def obtenerPeso(self,origen,destino):
        if origen in self.graph:
            if destino in self.graph:
                return self.graph[origen][destino]
        return 0

    def cambiarPeso(self,origen,destino,peso):
        if origen in self.graph:
            self.graph[origen][destino] = peso
        else:
            self.graph[origen] = {destino:peso}

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


    def imprimirCaminoMásCorto(self, dist):
        #print("Destinos \t\t\t Peso")
        tablaDist={}
        a=[]
        for graph in dist:
            if dist[graph]==10000000.0:
                continue;
            else:
                tablaDist[dist[graph]]=graph
                a.append(dist[graph])
        
        a.sort()
    
        print("El destino con la menor longitud es",tablaDist[a[1]],"con una distancia de",a[1])
        # es a[1] porque a[0], es la distancia 0 (osea a si mismo)
        #jsajdasj nmms si cierto
        
        


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
                    
        self.imprimirCaminoMásCorto(dist)
        

    def __str__(self):
        return str(self.graph)
