from claseVentana import Ventana

def test():
    print('Abriendo test...')
    ventana1 = Ventana('Test1')
    ventana2 = Ventana('test_incorrecto',100,100,600,600)#Caso incorrecto
    ventana1.mostrar()
    ventana1.moverDerecha()
    ventana1.mostrar()
    ventana1.subir(600)#caso incorrecto
    print('Cerrado test...\n\n')


if __name__ ==  '__main__':
    test()

    print('==== Ventana Inicio ====')
    ventanaInicio= Ventana('Inicio')
    ventanaInicio.mostrar()
    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print('==== Ventana Cargar ====')
    ventanaCargar= Ventana('Cargar',10,20)
    ventanaCargar.mostrar()
    print('*** Mueve a la derecha ***')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()
    print('*** Mueve a la izquierda ***')
    ventanaCargar.moverIzquierda(10)
    ventanaCargar.mostrar()
    print('*** Bajar ***')
    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()
    print('==== Ventana Borrar ====')
    ventanaBorrar = Ventana('Borrar', 10,20,100,200)
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir(5)   
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir()
    ventanaBorrar.mostrar()
    print('*** Bajar ***')
    ventanaBorrar.bajar()
    ventanaBorrar.mostrar()