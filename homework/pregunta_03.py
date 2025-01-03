"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    with open("files/input/data.csv") as file:
        data = file.readlines()

        for line in data:
            for letra in set(line[0]):
                if line.startswith(letra):
                    for line in data:
                        suma = {
                            letra: sum(
                                int(line[2]) for line in data if line.startswith(letra)
                            )
                            for letra in set(line[0] for line in data)
                        }
                        ans = sorted(suma.items())
    return ans


print(pregunta_03())
