class Ventana:
    __titulo = None
    __xSuperiorIzquierdo = None
    __ySuperiorIzquierdo = None
    __xInferiorDerecho = None
    __yInferiorDerecho = None

    def __init__(self, Titulo = None, x_superior = 0, y_superior = 0, x_inferior = 500, y_inferior = 500):
        if x_superior >= 0 and y_superior >= 0 and y_inferior <= 500 and y_superior <= 500:
            self.__titulo = Titulo
            self.__xSuperiorIzquierdo = x_superior
            self.__ySuperiorIzquierdo = y_superior
            self.__xInferiorDerecho = x_inferior
            self.__yInferiorDerecho = y_inferior
        else:
            print('NO puede crearse esa instancia!')    

    def mostrar(self):
        print('Nombre: {}\n({},{}) ({},{})' .format(self.__titulo, self.__xSuperiorIzquierdo,self.__ySuperiorIzquierdo,self.__xInferiorDerecho,self.__yInferiorDerecho))  

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return self.__xSuperiorIzquierdo * self.__ySuperiorIzquierdo

    def ancho(self):
        return self.__ySuperiorIzquierdo * self.__ySuperiorIzquierdo

    def moverDerecha(self, unidad = 1):
        if self.__ySuperiorIzquierdo+unidad < self.__yInferiorDerecho:
            self.__ySuperiorIzquierdo += unidad
            self.__yInferiorDerecho += unidad
        else:
            print('No puede generarse el movimiento!')    

    def moverIzquierda(self, unidad = 1):
        self.__yInferiorDerecho -= unidad
        self.__ySuperiorIzquierdo -= unidad   

    def subir(self, unidad = 1):
        if self.__xSuperiorIzquierdo+unidad < self.__xInferiorDerecho:
            self.__xSuperiorIzquierdo += unidad
            self.__xInferiorDerecho += unidad   
        else:
            print('NO puede generarse el movimiento!')     

    def bajar(self, unidad = 1):
        self.__xSuperiorIzquierdo -= unidad
        self.__xInferiorDerecho -= unidad        