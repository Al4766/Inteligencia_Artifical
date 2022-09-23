#Estados: sin-moneda, con-moneda, ai-servida, a2-servida, a3-servida
#Acciones: pedir-moneda, pedir-codigo, esperar
#Percepciones: moneda, a1 , a2, a3, servido 

REGLAS = {'sin-moneda':'pedir-moneda', 
            'con-moneda':'pedir-codigo',
            'a1-servida':'esperar',
            'a2-servida':'esperar',
            'a3-servida':'esperar'}
#Crear nuestro modelo (diccionario) para revisar los estados
MODELO = {('sin-moneda','pedir-moneda','moneda'):'con-moneda',
            ('con-moneda','pedir-codigo','a1'):'a1-servida',
            ('con-moneda','pedir-codigo','a2'):'a2-servida',
            ('con-moneda','pedir-codigo','a3'):'a3-servida',
            ('a1-servida','esperar','servido'):'sin-moneda',
            ('a2-servida','esperar','servido'):'sin-moneda',
            ('a3-servida','esperar','servido'):'sin-moneda'}
class ARBM:
    def __init__ (self, modelo, reglas, estado_inicial="", accion_incial=""):
        self.modelo = modelo
        self.reglas = reglas
        self.estado_inicial = estado_inicial
        self.accion_inicial = accion_incial
        self.accion = None
        self.estado = self.estado_inicial
        self.ult_accion = accion_incial

    def actuar(self, percepcion):
        if not percepcion:
            return self.accion_inicial
        clave = (self.estado, self.ult_accion, percepcion)
        if clave not in self.modelo.keys():
            self.estado = self.estado_inicial
            self.accion = self.accion_inicial
            self.ult_accion = self.accion_inicial
            return self.accion_inicial
        self.estado = self.modelo[clave]
        if self.estado not in self.reglas.keys():
            self.estado = self.estado_inicial
            self.accion = self.accion_inicial
            self.ult_accion = self.accion_incial
            return self.accion_inicial
        accion = self.reglas[self.estado]
        self.ult_accion = accion
        return accion

exp = ARBM(MODELO, REGLAS, 'sin-moneda', 'pedir-moneda')
percepcion = input("Indicar percepcion:")
while percepcion:
    accion = exp.actuar(percepcion)
    print(accion)
    percepcion = input("Indicar percepcion:")
