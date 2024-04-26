# control_venta_fresas.py

import pandas as pd

class ControlVentaFresas:
    def __init__(self):
        self.inventario_fresas = 10000
        self.fresas_vendidas = 0
        self.negocios = {}
        self.ventas_mensuales = []
        self.reporte_ventas = pd.DataFrame(columns=['Mes', 'Negocio', 'Cantidad'])

    def venta_fresa(self, cantidad, negocio):
        self.fresas_vendidas += cantidad
        self.negocios[negocio] = cantidad
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

    def generar_reporte_ventas(self):
        print("Reporte de ventas:")
        print(self.reporte_ventas)
