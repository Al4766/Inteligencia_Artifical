GRAFO = {"A":["B", "C", "D"],
         "B":["E"],
         "C":["F", "G"],
         "D":["H"],
         "E":["I"],
         "F":["J"]}
class BusquedaProfu:
    def __init__ (self, limite, destino):

        self.limite = limite
        self.destino = destino
      
    def prof(grafo, origen,limite, destino, sol=[]):
        contadorLimite = 0
        if origen == destino:
            return sol.append(origen) 
        if origen not in grafo:
            return sol
        for vecino in grafo[origen]:

        



