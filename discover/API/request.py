import requests
import json
import pandas as pd
import os


def api_audio(artists):

    """
    Hace una consulta mediante la api de AudioDB, y crea un
    data frame para los artisas  buscados
    :param artists: artistas a buscar
    :return: devuleve el dataframe con los dtaos
    """

    # Contendrán los datos seleccionados

    artist_name = []
    formed_year = []
    country = []

    # Iteremos por cada artista
    for i in artists:

        # Con la lebrería request y la función get, mas la dirección donde se
        # encuntran los artistas conseguimos todos sus datos
        response = requests.get('https://www.theaudiodb.com/api/v1/json/2/search.php?s={}'.format(i))

        # Comprobamos que la respuesta del servidor
        # es correcta
        if response.status_code == 200:

            # Conseguimos un objeto jason para iterar
            # y conseguir las características deseadas
            datos = json.loads(response.text)

            # Comprobamos que la respuesta no está vacia
            if datos['artists'] is not None:

                # Obtenemos el nombre
                artist_name.append(datos['artists'][0]['strArtist'])

                # Obtenemos el año de formación
                formed_year.append(datos['artists'][0]['intFormedYear'])

                # Obetemos la ciudad
                country.append(datos['artists'][0]['strCountry'])

    # Creamos las columna para el datframe
    columns = ['artist_name', 'formed_year', 'country']

    # Creamos el dataframe con las listas creadas
    dataframe = pd.DataFrame(list(zip(artist_name, formed_year, country)), columns=columns)

    return dataframe


def from_df_to_csv(df, path):

    """
    Tranforma un dataframe en csv
    :param df: datframe a almacenar
    :param path:dirección donde se almacena el csv
    :return:devulve un booleano que compruebe que el
    archivo se ha creado
    """

    df.to_csv(path, sep=',', index=False)

    return os.path.exists(path)

