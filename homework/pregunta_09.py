"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    with open("files/input/data.csv") as file:
        data = file.readlines()

        ans = {
            item.split(":")[0]: sum(
                1
                for line in data
                for code in {line.split()[4]}
                for cant in code.split(",")
                if cant.split(":")[0] == item.split(":")[0]
            )
            for line in data
            for code in {line.split()[4]}
            for item in code.split(",")
        }

        return ans
