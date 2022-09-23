ACCIONES = {'moneda':'dar-boleto',
        'boleto':'levantar-pluma', 'pasar-coche':'bajar-pluma'}

class PumaVigiaTable:

    def __init__(self, acciones):
        self.acciones = acciones
        self.percepciones = " "
    def actuar(self,percepcion,accion_basica=""):
        if not percepcion:
            print("Aqui estoy")
            return accion_basica
        if len(self.percepciones) != 0:
            self.percepciones +=  ','
        self.percepciones += percepcion
        if self.percepciones in self.acciones.keys():
            return self.acciones[self.percepciones]
        self.percepciones = ' '
        
        return accion_basica

expendedora = PumaVigiaTable(ACCIONES)
percepcion = input("Inicia percepción:")
while percepcion:
    accion = expendedora.actuar(percepcion, 'Hable más fuerte que traigo una toalla')
    print(accion)
    percepcion = input("Otra percepción:")
