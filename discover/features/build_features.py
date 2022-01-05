import pandas as pd


def read_csv(path=str, sep=';'):
    """
    Leer un archivo csv y los transforma a un dataframe
    :param path: dirección del archivo csv
    :param sep: separador del archvio
    :return: dataframe
    """
    # Leemos el archivo con la funcioón read_csv()
    df = pd.read_csv(path, sep=sep)

    return df


def merge_df(df1, df2, how, on=None):
    """
    Combina dos datframes
    :param df1: primer dataframe
    :param df2: segundo dataframe
    :param how: tipo de combinación
    :param on: columna a combinar
    :return: datafre combinado
    """
    # Combinamos con la función merge() de pandas
    df = pd.merge(df1, df2, how=how, on=[on])

    return df


def denormalized_df(path1=str, path2=str, path3=str, sep=';', how=str, on1=None, on2=None):
    """
    Desnormaliza 3 dataframes en uno
    :param path1: ruta del primer dataframe
    :param path2: ruta del segundo dataframe
    :param path3: ruta del tercer dataframe
    :param sep: delimitador de los archivos csv
    :param how: tipo de combinación
    :param on1: columna de combinación primer merge
    :param on2: columna de combinación  segundo merge
    :return: dataframe desnormalizado
    """

    # Leemos los csv con nuestro método
    df1 = read_csv(path1, sep=sep)
    df2 = read_csv(path2, sep=sep)
    df3 = read_csv(path3, sep=sep)

    # Combinamos los dataframes tracks y albums
    tracks_albums = merge_df(df1, df2, how, on1)

    # Renombremos la columna por la que combinar
    tracks_albums = tracks_albums.rename(columns={'artist_id_x': 'artist_id'})

    # Combinamos los dataframes trakcs_albums con artist
    result = merge_df(tracks_albums, df3, how, on2)

    # Renombremos las columnas a nombres más comprensibles
    result = result.rename(columns={'name': 'artist_name', 'name_x': 'track_name',
                                    'name_y': 'album_name', 'popularity': 'artist_popularity',
                                    'popularity_x': 'track_popularity', 'popularity_y': 'album_popularity'})
    return result
