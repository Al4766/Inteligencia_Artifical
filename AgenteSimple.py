REGLAS={'moneda':'pedir-codigo',
        'a1':'servir-a1', 'a2':'servir-a2',
        'a3':'servir-a3'}

class AgenteRS:
    def __init__ (self,reglas):
        self.reglas=reglas
    def actuar(self,percepcion,accion_basica=""):
        if not percepcion:
            return accion_basica
        if percepcion in self.reglas.keys():
            return self.reglas[percepcion]

        return accion_basica

exp = AgenteRS(REGLAS)
percepcion = input("Percepcion: ")
while percepcion:
    accion = exp.actuar(percepcion,"reinicio")
    print(accion)
    percepcion = input("Otra percepcion: ")
