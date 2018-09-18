import os
class Menu():
    productos = [
        {'nombre':'arroz','cantidad':20,'valorCompra':23000,'vrVenta':45000},
        {'nombre':'Aceite','cantidad':10,'valorCompra':10000,'vrVenta':30000},
        {'nombre':'Papa','cantidad':15,'valorCompra':15000,'vrVenta':50000},
        {'nombre':'Frijol','cantidad':80,'valorCompra':30000,'vrVenta':20000},
        {'nombre':'Maiz','cantidad':120,'valorCompra':20000,'vrVenta':15000},
        ]
    productoSeleccionado = ''
    
    def presentacion(self):
        os.system('cls')
        print('********************************')
        print('********MENU DE OPCIONES********')
        print('********************************')
        print('GESTION PRODUCTOS..............1')
        print('GESTION DE INVENTARIO..........2')
        print('COMPRAS........................3')
        print('VENTAS.........................4')
        print('SALIR..........................0')
    
    def opciones(self):
        self.presentacion()
        opcion = int(input('Digite una opcion: '))
        while(opcion != 0):
            if (opcion >= 0 and opcion < 5):
                if(opcion == 1):
                    self.gestionProductos()
                if(opcion == 2):
                    self.gestionInventario()
                if(opcion == 3):
                    self.compras()
                if(opcion == 4):
                    self.ventas()
            else:
                self.opciones()
                
    
    def gestionProductos(self):
        print('********************************')
        print('******GESTION DE PRODUCTOS******')
        print('********************************')
        #aqui voy a tener que hacer algo :)

        print("Nombre----Cantidad----ValorCompra----ValorVenta\n")
        for x in self.productos:
            print(str(x['nombre'])+"----"+str(x['cantidad'])
                  +"----"+str(x['valorCompra'])+"----"+str(x['vrVenta']))
        
        input('PRESIONE UNA TECLA PARA CONTINUAR')
        self.opciones()
mimenu = Menu()
mimenu.opciones()
        