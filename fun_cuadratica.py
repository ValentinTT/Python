import math

# Valor global para identificar las distintas funciones cuadraticas.
funcion_id = 0


class FuncionCuadratica ():
    lista_de_funciones = []

    def mostrar_datos(self):
        print ("""\n\nFuncion_Cuadratica() N{}:
f(x) ={}
a = {}		b = {}		c = {}
x1 = {}|
x2 = {}
vertice {}\n\n""".format(self.id, self.representacion, self.a, self.b, self.c,
                         self.x1, self.x2, self.vert))

    def calcular_punto(self, x):
        y = self.a * (x ** 2) + self.b * x + self.c
        return "El punto posee coordenadas ({};{})".format(x, y)


class FuncionPolinomica (FuncionCuadratica):

    def __init__(self):
        global funcion_id
        funcion_id += 1
        self.id = funcion_id
        self.modificar()

    def terminos_polinomica(self):
        self.a = float(input("Introduce a: "))
        self.b = float(input("Introduce b: "))
        self.c = float(input("Introduce c: "))

    def raices(self):
        """Calcula las raices de la funcion cuadratica"""
        discriminante = self.b ** 2 - 4 * self.a * self.c
        if discriminante < 0:
            self.x1 = round(
                (-(self.b) + math.sqrt(-discriminante)) / (2 * self.a), 4) + "i"
            self.x2 = round(
                (-(self.b) - math.sqrt(-discriminante)) / (2 * self.a), 4) + "i"

        else:
            self.x1 = (-(self.b) + math.sqrt(discriminante)) / (2 * self.a)
            self.x2 = (-(self.b) - math.sqrt(discriminante)) / (2 * self.a)

    def vertice(self):
        """Calcula el vertice de una raiz cuadratica"""
        if type(self.x1) != str:
            self.xv = (self.x1 + self.x2) / 2
            self.yv = self.a * (self.xv ** 2) + self.b * self.xv + self.c
            self.vert = (self.xv, self.yv)
        else:
            self.xv = "No hay vertice complejo"
            self.yv = "No hay vertice complejo"
            self.vert = "No hay vertice complejo"

    def modificar(self):
        self.terminos_polinomica()
        self.representacion = "{}x^2 + {}x + {}".format(self.a, self.b, self.c)
        self.raices()
        self.vertice()
        self.mostrar_datos()


class FuncionCanonica (FuncionCuadratica):

    def __init__(self):
        global funcion_id
        funcion_id += 1
        self.id = funcion_id
        self.modificar()

    def terminos_canonica(self):
        self.a = float(input("Introduce a: "))
        self.xv = float(input("Introduce xv: "))
        self.yv = float(input("Introduyve yv: "))
        self.vert = (self.xv, self.yv)

    def bc(self):
        """Calcula el vertice de una raiz cuadratica"""
        self.b = -(self.a * self.xv * 2)
        self.c = ((self.xv ** 2) * self.a) + self.yv

    def raices(self):
        """Calcula las raices de la funcion cuadratica"""
        discriminante = self.b ** 2 - 4 * self.a * self.c
        if discriminante < 0:
            self.x1 = round(
                (-(self.b) + math.sqrt(-discriminante)) / (2 * self.a), 4) + "i"
            self.x2 = round(
                (-(self.b) - math.sqrt(-discriminante)) / (2 * self.a), 4) + "i"

        else:
            self.x1 = (-(self.b) + math.sqrt(discriminante)) / (2 * self.a)
            self.x2 = (-(self.b) - math.sqrt(discriminante)) / (2 * self.a)

    def modificar(self):
        self.terminos_canonica()
        self.representacion = "{} (x - {})^2 + {}".format(self.a,
                                                          self.xv, self.yv)
        self.bc()
        self.raices()
        self.mostrar_datos()


class FuncionFactorizada (FuncionCuadratica):

    def __init__(self):
        global funcion_id
        funcion_id += 1
        self.id = funcion_id
        self.modificar()

    def terminos_factorizada(self):
        self.a = float(input("Introduce a: "))
        self.x1 = float(input("Introduce x1: "))
        self.x2 = float(input("Introduce x2: "))

    def bc(self):
        self.b = -(self.x1 + self.x2) * self.a
        self.c = (self.x1 * self.x2) * self.a

    def vertice(self):
        """Calcula el vertice de una raiz cuadratica"""
        if type(self.x1) != str:
            self.xv = (self.x1 + self.x2) / 2
            self.yv = self.a * (self.xv ** 2) + self.b * self.xv + self.c
            self.vert = (self.xv, self.yv)
        else:
            self.xv = "No hay vertice complejo"
            self.yv = "No hay vertice complejo"
            self.vert = "No hay vertice complejo"

    def modificar(self):
        self.terminos_factorizada()
        self.representacion = "{} (x - {}) (x - {})".format(self.a,
                                                            self.x1, self.x2)
        self.bc()
        self.vertice()
        self.mostrar_datos()


def search_function():
    """Muestra todas las funciones cuadráticas creadas para poder seleccionar una
    en particular, devolviendo la posicion en la lista_de_funciones"""
    for i in range(len(FuncionCuadratica.lista_de_funciones)):
        print(
            "{}. {}".format(i + 1, FuncionCuadratica.lista_de_funciones[i].representacion))
    search_id = int(input("Opción: "))
    search_id -= 1
    while search_id not in range(len(FuncionCuadratica.lista_de_funciones)):
        search_id = int(input("Opción: "))
        search_id -= 1
    return search_id


class Base:
    pass

    def main():
        while True:
            print("Opciones".center(80, "*"))
            print("Agregar:")
            print("	1.Función Polinómica")
            print("	2.Función Canónica")
            print("	3.Función Factorizada")
            print("4.Mostrar")
            print("5.Modificar")
            print("6.Obtener y de x")
            print("6.Salir")
            respuesta = int(input("Opción: "))
            while respuesta not in range(1, 8):
                respuesta = int(input("Opción: "))

            print()

            if respuesta == 1:
                print("Polinómica".center(80, "_"))
                FuncionCuadratica.lista_de_funciones.append(
                    FuncionPolinomica())
            elif respuesta == 2:
                print("Canónica".center(80, "_"))
                FuncionCuadratica.lista_de_funciones.append(FuncionCanonica())
            elif respuesta == 3:
                print("Factorizada".center(80, "_"))
                FuncionCuadratica.lista_de_funciones.append(
                    FuncionFactorizada())
            elif respuesta == 4:
                funcion_id = search_function()
                FuncionCuadratica.lista_de_funciones[
                    funcion_id].mostrar_datos()
            elif respuesta == 5:
                funcion_id = search_function()
                FuncionCuadratica.lista_de_funciones[funcion_id].modificar()
            elif respuesta == 6:
                funcion_id = search_function()
                FuncionCuadratica.lista_de_funciones[
                    funcion_id].calcular_punto()
            elif respuesta == 7:
                break
