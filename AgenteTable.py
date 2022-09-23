ACCIONES = {"limpio":"izquierda-derecha padrino",
                "sucio":"no sea puerco (ya limpie mi rey)"}

class AgenteTable:

    def __init__(self, acciones):
        self.acciones = acciones
        self.percepciones = " "
    def actuar(self,percepcion,accion_basica= ' '):
        if not percepcion:
            return accion_basica
        if len(self.percepciones) != 0:
            self.percepciones
        self.percepciones
        if self.percepciones in self.acciones.keys():
            return self.acciones[self.percepciones]
        self.percepciones = ' '
        return accion_basica

expendedora = AgenteTable(ACCIONES)
percepcion = input("Inicia percepción: ")
while percepcion:
    accion = expendedora.actuar(percepcion, 'Espera')
    print(accion)
    percepcion = input("Inicia percepción: ")

