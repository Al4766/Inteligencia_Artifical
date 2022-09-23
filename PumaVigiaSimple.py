REGLAS={'moneda':'dar-boleto',
        'boleto':'levantar-pluma', 'pasar-coche':'bajar-pluma'
        }

class PumaVigiaRS:
    def __init__ (self,reglas):
        self.reglas=reglas
    def actuar(self,percepcion,accion_basica=""):
        if not percepcion:
            return accion_basica
        if percepcion in self.reglas.keys():
            return self.reglas[percepcion]

        return accion_basica

vig = PumaVigiaRS(REGLAS)
percepcion = input("Percepcion:")
while percepcion:
    accion = vig.actuar(percepcion,"Hable más fuerte que traigo una toalla")
    print(accion)
    percepcion = input("Otra percepcion: ")