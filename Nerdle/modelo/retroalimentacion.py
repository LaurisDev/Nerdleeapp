
class Retroalimentacion:

    def __init__(self, ecuacion: list):

        self.ecuacion_actual: list = ecuacion

    def verificar_posiciones(self, ingreso: list) -> list:

        lista_retorno: list = ["" for i in ingreso]
        print(f"lista generada {lista_retorno}")
        for i in range(len(self.ecuacion_actual)):
            if ingreso[i] not in self.ecuacion_actual:
                lista_retorno[i] = "#808080"
            elif ingreso[i] in self.ecuacion_actual:
                if self.ecuacion_actual[i] != ingreso[i]:
                    lista_retorno[i] = "#FFFF00"
                elif self.ecuacion_actual[i] == ingreso[i]:
                    lista_retorno[i] = "#008000"

        print(f"lista retornada {lista_retorno}")
        return lista_retorno