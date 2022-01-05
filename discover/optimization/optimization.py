import pandas as pd
import time
import matplotlib.pyplot as plt


def get_column_pandas(path=str, column=str):
    """
    Seleciona una columna con la librería pandas
    :param path: ruta del archivo
    :param column: columna a leer
    :return: columna leida
    """

    # Leemos el dataframe con la función
    # read_csv() de pandas
    df = pd.read_csv(path, sep=';')

    return list(df[column])


def get_column_read(path, column=str):
    """
    Selecciona una columna leyendo el archivo
    :type column: columna a seccionar
    :param path: ruta del archivo
    :param column: columna a leer
    :return: columna leida
    """

    # Leemos el archivo
    with open(path, 'r') as file:
        # Creamos al lista que almacenará la columna
        col = []

        # Obtenemos el encabezado
        header = file.readline().split(';')

        # Obtenemos el índice de la columna seleccionada
        index = header.index(column)

        # Obtenemos las líneas del documento
        lines = file.readlines()

        # Iteramos por cada línea
        for line in lines:
            # Separamos por las columnas, con la función
            # split y el delimitador, y posteriormente
            # seleccionamos la columna deseada
            # con el índice y posteriormente la
            # añadimos a la lista con append()
            col.append(line.split(';')[index])

    return col


def compare_methods(path, column):
    """
    Crea una gráfica que compara la velocidad de
    dos métodos
    :param path: ruta del archivo
    :param column: columna a leer
    :return: tupla(float(tiempo_pandas), float(tiempo_read)
    """

    # Calculamos el tiempo que pasa entre las
    # diferentes ejecuciones
    start_time = time.time()
    pandas = get_column_pandas(path, column)
    middle_time = time.time()
    read = get_column_read(path, column)
    stop_time = time.time()

    # Hacemos la diferencia para tener un único
    # número
    pandas_time = middle_time - start_time
    read_time = stop_time - middle_time

    # Instanciamos los puntos en relación al tiempo
    # tardado
    point = [0, 0]
    pandas_point = [len(pandas), pandas_time]
    read_point = [len(read), read_time]

    x = [point[0], pandas_point[0]]
    y1 = [point[1], pandas_point[1]]
    y2 = [point[1], read_point[1]]

    plt.figure()

    # Graficamos las líneas
    plt.plot(x, y1)
    plt.plot(x, y2)

    # Mostramos la Leyenda
    plt.legend(["Pandas", "Read method"])

    # Añadimos etiquetas a los ejes x e y
    plt.xlabel('$n$')
    plt.ylabel('$segundos$')

    # Añadimos el título
    plt.title("Execution time of different methods")

    # Mostramos el gráfico
    plt.show()

    return pandas_time, read_time
