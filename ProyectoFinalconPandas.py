import matplotlib.pyplot as plt
import pandas as pd

class ControlVentaFresas:
    def __init__(self):
        self.inventario_fresas = 10000
        self.fresas_vendidas = 0
        self.negocio1 = 0
        self.negocio2 = 0
        self.negocio3 = 0
        self.ventas_mensuales = []
        self.reporte_ventas = pd.DataFrame(columns=['Mes', 'Negocio', 'Cantidad'])

    def venta_fresa(self, cantidad, negocio):
        self.fresas_vendidas += cantidad
        if negocio == negocio:
            self.negocio1 += cantidad
        elif negocio == negocio:
            self.negocio2 += cantidad
        elif negocio == negocio:
            self.negocio3 += cantidad
        self.registrar_venta(cantidad, negocio)

    def registrar_venta(self, cantidad, negocio):
         mes = len(self.ventas_mensuales) + 1
         nueva_venta = pd.DataFrame({'Mes': [mes], 'Negocio': [negocio], 'Cantidad': [cantidad]})
         self.reporte_ventas = pd.concat([self.reporte_ventas, nueva_venta], ignore_index=True)

    def agregar_venta_inventario(self, cantidad):
        self.inventario_fresas -= cantidad

    def agregar_inventario(self, cantidad):
        self.inventario_fresas += cantidad


    def registrar_ventas_mes(self):
        self.ventas_mensuales.append(self.fresas_vendidas)

    def grafico_vendedor_mes(self):
        meses = list(range(1, len(self.ventas_mensuales) + 1))
        plt.plot(meses, self.ventas_mensuales, marker='o')
        plt.title('Ventas mensuales')
        plt.xlabel('Mes')
        plt.ylabel('Fresas vendidas')
        plt.show()

    def grafico_producto_mas_vendido(self):
        negocios = ['Negocio1', 'Negocio2', 'Negocio3']
        ventas_por_negocio = [self.negocio1, self.negocio2, self.negocio3]
        plt.bar(negocios, ventas_por_negocio)
        plt.title('Producto más vendido')
        plt.xlabel('Negocio')
        plt.ylabel('Fresas vendidas')
        plt.show()

    def grafico_producto_menos_vendido(self):
        negocios = ['Negocio1', 'Negocio2', 'Negocio3']
        ventas_por_negocio = [self.negocio1, self.negocio2, self.negocio3]
        plt.bar(negocios, ventas_por_negocio, color='red')
        plt.title('Producto menos vendido')
        plt.xlabel('Negocio')
        plt.ylabel('Fresas vendidas')
        plt.show()

    def grafico_ventas_mes(self):
        meses = list(range(1, len(self.ventas_mensuales) + 1))
        plt.plot(meses, self.ventas_mensuales, marker='o')
        plt.title('Ventas mensuales')
        plt.xlabel('Mes')
        plt.ylabel('Fresas vendidas')
        plt.show()

    def generar_reporte_ventas(self):
        print("Reporte de ventas:")
        print(self.reporte_ventas)

def main():
    control_fresas = ControlVentaFresas()

    while True:
        print("1. Ingresar venta")
        print("2. ¿Cuánto producto hay en bodega?")
        print("3. ¿Cuál es la cantidad total de fresas vendidas?")
        print("4. ¿Cuántas fresas desea agregar al inventario?")
        print("5. Generar gráficos")
        print("6. Generar reporte de ventas")
        print("7. Salir")

        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            cantidad = int(input("¿Cuántas fresas se vendieron? "))
            negocio = input("¿Cuál compañía fue? ")
            control_fresas.venta_fresa(cantidad, negocio)
            control_fresas.agregar_venta_inventario(cantidad)
        elif opcion == 2:
            print("La cantidad total de fresas en inventario es de:", control_fresas.inventario_fresas)
        elif opcion == 3:
            print("La cantidad de fresas vendidas es de:", control_fresas.fresas_vendidas)
        elif opcion == 4:
            cantidad = int(input("¿Cuántas fresas desea agregar al inventario? "))
            control_fresas.agregar_inventario(cantidad)
            print("Se ha actualizado el inventario con éxito.")
            print("La cantidad total de fresas en inventario es de:", control_fresas.inventario_fresas)
        elif opcion == 5:
            while True:
                print("1. Grafica vendedor del mes")
                print("2. Grafico producto mas vendido")
                print("3. Grafico producto menos vendido")
                print("4. Grafico ventas del mes")
                print("5. Salir al menu principal")

                opcion1 = int(input("Ingrese su opción: "))

                if opcion1 == 1:
                    control_fresas.registrar_ventas_mes()
                    control_fresas.grafico_vendedor_mes()
                elif opcion1 == 2:
                    control_fresas.registrar_ventas_mes()
                    control_fresas.grafico_producto_mas_vendido()
                elif opcion1 == 3:
                    control_fresas.registrar_ventas_mes()
                    control_fresas.grafico_producto_menos_vendido()
                elif opcion1 == 4:
                    control_fresas.registrar_ventas_mes()
                    control_fresas.grafico_ventas_mes()
                elif opcion == 5:
                     print("Gracias por usar el sistema")
                     break
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == 6:
            control_fresas.generar_reporte_ventas()
        elif opcion == 7:
            print("Gracias por usar el sistema")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

