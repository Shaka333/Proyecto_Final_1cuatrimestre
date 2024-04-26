# interfaz_usuario.py

from control_venta_fresas import ControlVentaFresas
from graficos import GeneradorGraficos

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
                print("1. Graficar ventas del mes")
                print("2. Graficar empresas que compraron")
                print("3. Salir al menú principal")

                opcion1 = int(input("Ingrese su opción: "))

                if opcion1 == 1:
                    control_fresas.registrar_ventas_mes()
                    GeneradorGraficos.grafico_ventas_del_mes(control_fresas.ventas_mensuales)
                elif opcion1 == 2:
                    GeneradorGraficos.grafico_empresa_que_mas_compro(control_fresas.negocios)
                elif opcion1 == 3:
                    print("Volviendo al menú principal...")
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
