"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open("files/input/data.csv") as file:
        data = file.readlines()

        ans = sorted(
            [
                (
                    letra,
                    int(
                        max(
                            line.split()[1] for line in data if line.split()[0] == letra
                        )
                    ),
                    int(
                        min(
                            line.split()[1] for line in data if line.split()[0] == letra
                        )
                    ),
                )
                for letra in {line.split()[0] for line in data}
            ]
        )
        return ans
