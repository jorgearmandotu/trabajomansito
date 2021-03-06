import os
import sys

class products():
    
    
        
    productos = [
    {'nombre':'arroz','cantidad':0,'vlrCompra':100,'vlrVenta':1000},
    {'nombre':'papa','cantidad':0,'vlrCompra':10,'vlrVenta':100},
    ]

    def limpiar(self):
        plataforma = sys.platform
        if plataforma.startswith('linux'):
            os.system('clear')
        elif plataforma.startswith('win'):
            os.system('cls')
            
    def menu(self):
        self.limpiar()
        op = None
        while(op != '0'):
            print('********* Menu *********')
            print('Agregar productos------1')
            print('listar productos-------2')
            print('Comprar productos------3')
            print('Venta de productos-----4')
            print('self.limpiar pantalla-------5')
            print('Salir------------------0')
            
            op = input('Elija una opcion: \n')
            self.limpiar()
            if(op == '1'):
                self.agregar()
                
                self.limpiar()
            elif(op == '2'):
                self.listar()
            elif(op == '3'):
                self.comprar()
            elif(op == '4'):
                self.ventas()
            
    def agregar(self):
        print('**** Agregar Producto ****')
        nom = input('ingrese nombre producto: ')
        cantidad = input('ingrese cantidad de '+nom+': ')
        vlrCompra = input('ingrese valor de compra del producto: ')
        vlrVenta = input('ingrese valor de Venta del producto: ')
        product = {'nombre':nom,'cantidad': int(cantidad), 'vlrCompra':int(vlrCompra),
                'vlrVenta':int(vlrVenta)}
        self.productos.append(product)
        input('producto agregado')
    
    def listar(self):
        for x in self.productos:
            print('producto: %s cantidad: %i' %(x['nombre'],x['cantidad']))
        input('presione enter para continuar')
        self.limpiar()
        
    def comprar (self):
        op = 's'
        total = 0
        carritoCompra = []
        while(op == 's'):
            nom = input('ingrese nombre de producto a comprar: ')
            indice = self.buscar(nom)
            if(indice != None):
                cant = int(input('ingrese cantidad de producto a conprar: '))
                vlrCompra = int(input('ingrese valor del producto: '))
                total += cant * vlrCompra
                print('total a pagar: %d' %total)
                carritoCompra.append({'nombre':nom,'cantidad': cant, 'vlrCompra':vlrCompra})
                op = input('presione s para seguir comprando, \ng para finalizar compra, o \nx para cancelar compra. ')
                self.limpiar()
            
            else: 
                print('producto no existe')
                input('enter para continuar')
                self.limpiar()
        if(op == 'g'):
            for x in carritoCompra:
                indice = self.buscar(x['nombre'])
                self.productos[indice]['cantidad'] += x['cantidad']
                self.productos[indice]['vlrCompra'] += x['vlrCompra']
                
    def ventas(self):
        op = 's'
        total = int(0)
        carritoCompra = []
        while(op == 's'):
            nom = input('ingrese nombre de producto a vender: ')
            indice = self.buscar(nom)
            if(indice != None):
                cant = int(input('ingrese cantidad de producto a vender: '))
                if(cant == 0 or cant > self.productos[indice]['cantidad']):
                        op = input('No hay suficientes existencias en inventario.\npresione s para seguir vendiendo n para dalir al menu.')
                                    
                        #self.limpiar()
                else:
                    total += int(cant) * int(self.productos[indice]['vlrVenta'])
                    print('total a pagar: %d' %total)
                    carritoCompra.append({'nombre':nom,'cantidad': cant})
                    op = input('presione s para seguir vendiendo, \ng para finalizar venta, o \nx para cancelar venta. ')
                    #self.limpiar()
            
            else: 
                print('producto no existe')
                input('enter para continuar')
                #self.limpiar()
        if(op == 'g'):
            for x in carritoCompra:
                indice = self.buscar(x['nombre'])
                self.productos[indice]['cantidad'] -= x['cantidad']
                
        
    def buscar(self, nombre):
        indice = None;
        for x in self.productos:
            if(x['nombre'] == nombre):
                indice = self.productos.index(x)
                break
        return indice
        
miApp = products()
miApp.menu()