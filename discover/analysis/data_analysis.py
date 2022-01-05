import numpy as np
# import re


def number_of_rows(df):
    """
    Cuenta el número de filas de un dataframe
    :param df: dataframe
    :return: int, número de filas
    """

    # Contamos las filas con la función len()
    return len(df)


def number_of_columns(df):
    """
    Cuenta el número de columnas de un dataframe
    :param df: dataframe
    :return: int, númmero de columnas
    """

    # Contamos los elementos en la lista
    # con las columnas
    return len(df.columns)


def nulls_of_column(df, column=str):
    """
    Calcula los nulos de una columna del
    datframe
    :param df: dataframe a anilizar
    :param column: columna a anlizar
    :return: int Nulos de la colunna
    """

    # Conseguimos los nulos con isnull(), con sum()
    # obtenemos el número total de nulos
    nulos = df[column].isnull().sum()

    return nulos


def max_mean_min(df, column_name=str, group=str, feature=str):
    """
    Calcula el máximo, media y mínimo de una caracteríctica
    de un determinado grupo de música
    :param df: dataframe
    :param column_name: columna con el nombre de los grupos
    :param group: nombre del grupo
    :param feature: característica a analizar
    :return: Devuelve una tupla con el máximo,
    media, y mínimos de la característica indicada respectivamente
    """

    # Conseguimos el máximo con max(), de los datos seleccionados
    maximum = max(df[df[column_name] == group][feature])

    # Conseguimos la media con np.mean(), de los datos seleccionados
    mean = np.mean(df[df[column_name] == group][feature])

    # Conseguimos el mínimo con min(), de los datos seleccionados
    minimum = min(df[df[column_name] == group][feature])

    return maximum, mean, minimum


def mean_feature_album(df, col_groups=str, name_group=str, col_albums=str, feature=str):
    """
    calcula la media de la caraterística para cada
    álbum de un grupo de música
    :param df: dataframe a analizar
    :param col_groups: columna con los grupos
    :param name_group: nombre del grupo
    :param col_albums: columna con los álbums
    :param feature: caraterística a analizar
    :return: Devuelve la media de la caraterística para cada
    álbum de un grupo de música
    """

    # Seleccionamos los datos, agrupamos y calculamos la media de estos
    return df[df[col_groups] == name_group].groupby(col_albums)[feature].mean()


def tracks_of_artist(df, column=str, artist=str):
    """
    Calcula las caciones del artista seleccionado
    :param df: dataframe a analizar
    :param column: columna a selccionar con el nombre del artista
    :param artist: nombre del artista
    :return: int, la cantidad de canciones que tiene el artita
    """

    # Seleccionamos al artista, como cada fila es una canción
    # contamos la filas para saber cuantas canciones tiene
    return len(df[df[column] == artist])


def word_in_track(df, column=str, word=str):
    """
    Busca una palabra en una columna y calcula
    la cantidad de filas en dicha columna
    :param df: dataframe a analizar
    :param column: columna a seleccionar con el nombre de las canciones
    :param word: palabra a o elemento a buscar
    :return: int, cantidad de filas con dicha palabra
    """

    # Con contains(), conseguimo un booleano
    # sobre si el string entero completo contiene la palabra
    # Sumamos los True = 1
    return sum(df[column].str.contains(word))
    # return sum(df[column].str.contains(word, flags=re.IGNORECASE, regex=True))


def tracks_of_epoch(df, column=str, year_1=int, year_2=int):
    """
    Cuenta los canciones que hay entre unos años
    :param df: dataframe a anlizar
    :param column: columna a seleccionar
    :param year_1: primer año a buscar, inclusive
    :param year_2: último año a buscar inclusive
    :return: int, Las canciones que hay entre esos años
    """

    # Utilizamos la función between para obtener uan booleano
    # sobre si la fila cumple las condiciones de estar entre
    # dos valores.
    # Con sum sumamos los True = 1
    return sum(df[column].between(year_1, year_2))


def tracks_max_popularity_of_epoch(df, tracks=str, col_year=str, popularity=str, year_1=int, year_2=int):
    """
    Busca las canciones con máxima popularidad para
    un rango de años
    :param df: nombre del datafreme
    :param tracks: columna con el nombre de las canciones
    :param col_year: columna con los años
    :param popularity:  columna con la popularidad
    :param year_1: primer año a buscar
    :param year_2: último año a buscar
    :return: Devuelve un Serie con las canciones
    más populares en un rago de años
    """

    # En este caso seleccionamos por rango con between(),
    # Y además que sea el máximo
    track = df[(df[popularity] == max(df[popularity])) &
               (df[col_year].between(year_1, year_2))][tracks]

    return track.values


def every_decade(df, col_name=str, col_year=str):
    """
    Encuentra los artistas que han publicado una canción
    en cada década desde 1960
    :param df: dataframe original
    :param col_name: columna con los artistas
    :param col_year: columna con los años
    :return: lista(nombre de los artistas)
    """

    # Lista que almacenerá los artistas
    artists = []

    # La columna del año la estructuramos por décadas
    df[col_year] = (df[col_year] // 10) * 10

    # Agrpupamos por artista y año, contamos loa que en cada grupo
    # Con size() y reseteamos el índice, dando nombre a la nuva columna
    a = df.groupby([col_name, col_year]).size().reset_index(name='count')

    # Para cada artista sin repetir
    for artist in set(df[col_name]):

        # Obtenemos las décadas que han publicado
        years = list(a[a[col_name] == artist][col_year])

        # Condición que se debe de cumplir
        # Que tengan 7 años, pero que 1950 no esté para controlar
        # que no es desde 1950-2010
        if len(years) == 7 and 1950 not in years:
            # Los añadimos a la lista
            artists.append(artist)

    return artists
