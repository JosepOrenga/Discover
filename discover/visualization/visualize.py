import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from discover.analysis.data_analysis import mean_feature_album
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances


def barplot_albums(df, col_group, group_name, col_album, feature, rotation):
    """
    Crea un barplot de la media de los álbums, en refencia a
    una característica
    :param df: dataframe
    :param col_group: columna con el nombre de los grupos
    :param group_name: nombre del grupo
    :param col_album: columna con el nombre de los álbumes
    :param feature: característica a analizar
    :param rotation: rotación etiquetas eje x
    :return: lista, devuelve los álbumes del artista
    """
    # Obtenemos los dat0s
    albums = np.sort(pd.unique(df[df[col_group] == group_name][col_album]))

    # CReamos el gráfico de barras
    plt.bar(albums,
            mean_feature_album(df,
                               col_group,
                               group_name,
                               col_album,
                               feature))

    # Rotamos los valores de los ejes
    plt.xticks(rotation=rotation)

    # Añadimos el título
    plt.title('Albums of {}'.format(group_name))

    # Mostramos el gráfico
    plt.show()

    return albums


def density_histogram(df, col_group, artist, feature, rotation):
    """
    Crea un histograma de densidad para un artista
    :param df: dataframe
    :param col_group: columna con el nombre del artista
    :param artist: nombre del artista
    :param feature: caraterística a comparar
    :param rotation: rotación de las etiquetas del eje x
    :return: float, la suma de las alturas de la barras, que
    debe ser uno
    """
    # Obtenemos los datos del artista
    datos = df[df[col_group] == artist][feature]

    # Para que la suma de todas las barras sea uno,
    # ponderamos cada bin dividiéndolo por el total
    # de valores
    weights = np.ones_like(datos.values) / len(datos.values)

    # Obtenemos los datos correspondientes al histograma,
    # como la altura de las barras
    heights, bins, batches = plt.hist(datos,
                                      label=artist,
                                      weights=weights,
                                      edgecolor='white')

    # Rotamos los valores de los ejes
    plt.xticks(rotation=rotation)

    # Mostramos el título
    plt.title('Density histogram of {}'.format(artist))

    # Mostramos la leyenda
    plt.legend()

    # Mostramos el gráfico
    plt.show()

    return sum(heights)


def density_hist_two_singers(df, col_name, artist_1, artist_2, feature, rotation):
    """
    Crea un histograma de densidad para dos artistas
    :param df: dataframe
    :param col_name: columna con el nombre de los artistas
    :param artist_1: nombre del primer artista
    :param artist_2: nombre del segundo artista
    :param feature: caraterística a comparar
    :param rotation: rotación de las etiquetas del eje x
    :return: float, suma de las alturas de las barras de los
    dos histogramas, que debe ser 2, 1 cada uno
    """

    # Obtenemos los datos del primer artista
    datos1 = df[df[col_name] == artist_1][feature]

    # Para que la suma de todas las barras sea uno,
    # ponderamos cada bin dividiéndolo por el total
    # de valores
    weights1 = np.ones_like(datos1.values) / len(datos1.values)

    # Obtenemos los datos correspondientes al histograma,
    # como la altura de las barras
    heights1, bins1, batches1 = plt.hist(datos1,
                                         alpha=0.5,  # Denotamos la tranparencia
                                         edgecolor='white',
                                         label=artist_1,
                                         weights=weights1)

    # Obtenemos los datos del segundo artista
    datos2 = df[df[col_name] == artist_2][feature]

    # Para que la suma de todas las barras sea uno,
    # ponderamos cada bin dividiéndolo por el total
    # de valores
    weights2 = np.ones_like(datos2.values) / len(datos2.values)

    # Obtenemos los datos correspondientes al histograma,
    # como la altura de las barras
    heights2, bins2, batches2 = plt.hist(datos2,
                                         edgecolor='white',
                                         alpha=0.5,
                                         label=artist_2,
                                         weights=weights2)

    # Rotamos los valores de los ejes
    plt.xticks(rotation=rotation)

    # Mostramos el título
    plt.title('Density histgram of {}, {}'.format(artist_1,artist_2))

    # Mostramos la leyenda
    plt.legend()

    # Mostramos el gráfico
    plt.show()

    return sum(heights1) + sum(heights2)


def plot_cosinus_similarity(df, features, artists, col_name):
    """
    Calula de similtud del coseno entre dos vectores
    :param df:dataframe original
    :param features: caraterísticas a comparar más el
    nombre de la canciones
    :param artists: artistas a comparar
    :param col_name: columna con el nombre de los artistas
    :return:Devuelve una array, en forma de matriz con el
    resultado de la similitud del coseno
    """
    # Calculamos las medias de las features por artista
    means = df[features].groupby(col_name).mean()

    # Calculamos la similitud del coseno
    cosine_sim = cosine_similarity(means.loc[artists])

    # Generamos la figura y los ejes
    fig, ax = plt.subplots()

    # Creamos la paleta de color
    heatmap = ax.pcolor(cosine_sim, cmap=plt.cm.Blues)

    # Añadimos los ejes
    ax.set_xticks(np.arange(len(artists)))
    ax.set_yticks(np.arange(len(artists)))

    # Añadimos los nombres a los ejes
    ax.set_xticklabels(artists)
    ax.set_yticklabels(artists)

    # Rotamos los nombres de los ejes
    plt.xticks(rotation=45)

    # Añadimos el título
    plt.title('Cosinus Similarity')

    # Añadimos la paleta de color
    plt.colorbar(heatmap)

    # Mostramos el gráfico
    plt.show()

    return cosine_sim


def plot_euclidean_similarity(df, features, artists, col_name):
    """
    Calula de similtud euclidiana entre dos vectores
    :param df:dataframe original
    :param features: caraterísticas a comparar más el
    nombre de la canciones
    :param artists: artistas a comparar
    :param col_name: columna con el nombre de los artistas
    :return: Devuelve una array, en forma de matriz con el
    resultado de la similitud euclideana
    """

    # Calculamos las medias de las features por artista
    means = df[features].groupby(col_name).mean()

    # Calculamos la similitud euclidiana, a partir
    # de la distancia euclidiana
    euclidean_sim = 1 / (1 + euclidean_distances(means.loc[artists]))

    # Generamos la figura y los ejes
    fig, ax = plt.subplots()

    # Creamos la paleta de color
    heatmap = ax.pcolor(euclidean_sim, cmap=plt.cm.Blues)

    # Añadimos los ejes
    ax.set_xticks(np.arange(len(artists)))
    ax.set_yticks(np.arange(len(artists)))

    # Añadimos los nombres a los ejes
    ax.set_xticklabels(artists)
    ax.set_yticklabels(artists)

    # Rotamos los nombres de los ejes
    plt.xticks(rotation=45)

    # Añadimos el título
    plt.title('Euclidean similarity')

    # Añadimos la paleta de color
    plt.colorbar(heatmap)

    # Mostramos el gráfico
    plt.show()

    return euclidean_sim
