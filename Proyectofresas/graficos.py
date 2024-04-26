# graficos.py

import matplotlib.pyplot as plt

class GeneradorGraficos:
    @staticmethod
    def grafico_ventas_del_mes(ventas_mensuales):
        meses = list(range(1, len(ventas_mensuales) + 1))
        plt.plot(meses, ventas_mensuales, marker='o')
        plt.title('Ventas mensuales')
        plt.xlabel('Mes')
        plt.ylabel('Fresas vendidas')
        plt.show()

    @staticmethod
    def grafico_empresa_que_mas_compro(negocios):
        nombres_negocios = list(negocios.keys())
        ventas_por_negocio = list(negocios.values())
        plt.bar(nombres_negocios, ventas_por_negocio)
        plt.title('Empresa que más compró')
        plt.xlabel('Negocio')
        plt.ylabel('Fresas vendidas')
        plt.show()
