import sys
import time

from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from discover.data.make_dataset import *
from discover.features.build_features import *
from discover.visualization.visualize import *
from discover.optimization.optimization import *
from discover.analysis.data_analysis import *
from discover.preprocessing.data_prepocessing import *
from discover.API.request import *

if __name__ == "__main__":
    # Tarea 1

    # Descomprimimos el archivo data
    unzip_file('../data/data.zip', '../data')

    result = denormalized_df('../data/tracks_norm.csv', '../data/albums_norm.csv',
                             '../data/artists_norm.csv', ';', 'inner', 'album_id', 'artist_id')

    # result = denormalized_df(tracks, albums, artists, 'inner', 'album_id', 'artist_id')

    # Aplicamos la función que transforma a mayúscula primera letra,
    result = capital_letter(result, 'artist_name')

    # Mostramos los nulos de popularity
    print(f'Tracks que no tienen valor de popularity {nulls_of_column(result, "track_popularity")}')

    # Aplicamos la función para sustituir por la media
    fill_null_by_mean(result, 'track_popularity')

    print(f'El total de tracks es {number_of_rows(result)}, y el total de columnas es {number_of_columns(result)}')

    # Tarea 2

    # Comparamos con el dataframe de los artistas
    get_column_pandas('../data/artists_norm.csv', 'artist_id')
    get_column_read('../data/artists_norm.csv', 'artist_id')

    # Comparamos los métodos
    compare_methods('../data/artists_norm.csv', 'artist_id')

    # Comparamos con el dataframe de los álbums
    get_column_pandas('../data/albums_norm.csv', 'album_id')

    get_column_read('../data/albums_norm.csv', 'album_id')

    # Comparamos los métodos
    compare_methods('../data/albums_norm.csv', 'album_id')

    # Comparamos con el dataframe de los tracks
    get_column_pandas('../data/tracks_norm.csv', 'track_id')

    get_column_read('../data/tracks_norm.csv', 'track_id')

    # Comparamos los métodos
    compare_methods('../data/tracks_norm.csv', 'track_id')

    # Tarea 3

    # ¿Cuántas tracks hay del artista Radiohead?

    print(f'Radiohead tiene {tracks_of_artist(result, "artist_name", "Radiohead")} canciones')

    # ¿Cuántas tracks contienen la palabra 'police' en el título?

    print(f'La palabra police la contienen {word_in_track(result, "track_name", "police")} canciones')

    # ¿Cuántas tracks son de álbumes publicados en la década del 1990?

    print(f'En la década de los 90 hay {tracks_of_epoch(result, "release_year", 1990, 1999)} canciones')

    # ¿Cuál es la track con más popularidad de los últimos 10 años?

    print(f'La canción con más popularidad de los 10 últimos años es ' + "\n" +
          f'{tracks_max_popularity_of_epoch(result, "track_name", "release_year", "track_popularity", 2011, 2021)}')

    # ¿Qué artistas tienen tracks en cada una de las décadas desde el 1960?

    print(f'Los artistas que han publicado una canción en todas las décadas desde 1906 son' + "\n" +
          f'{every_decade(result, "artist_name", "release_year")}')
    # Tarea 4

    # Calcular el mínimo, la media y el máximo de la feature energy de todas las tracks de
    # Metallica.

    print(f'El máximo, media y mínimo para energy de Metallica es '
          f'{max_mean_min(result, "artist_name", "Metallica", "energy")} respectivamente')

    #  Calcular la media de la feature danceability de cada álbum de Coldplay y crear una
    # gráfica para visualizar el resultado.

    print(f'La media de danceabilty de cada álbum de Coldplay es' + "\n" +
          f'{mean_feature_album(result, "artist_name", "Coldplay", "album_name", "danceability")}')

    barplot_albums(result, 'artist_name', 'Coldplay', 'album_name', 'danceability', 90)

    # Tarea 5

    density_histogram(result, 'artist_name', 'Ed Sheeran', 'acousticness', 90)

    # Tarea 6

    density_hist_two_singers(result, 'artist_name', 'Adele', 'Extremoduro', 'energy', 90)

    # Tarea 7

    # denotamos las características
    features = ['artist_name', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']

    # Denotamos a los artistas
    artists = ['Metallica', 'Extremoduro', 'AC/DC', 'Hans Zimmer']

    # Calculamos y mostramos la similitud del coseno entre artistas

    plot_cosinus_similarity(result, features, artists, 'artist_name')

    # Calculamos y mostramos la similitud euclidiana entre artistas

    plot_euclidean_similarity(result, features, artists, 'artist_name')

    # Tras observar los heatmap podemos concluir que la similitud del coseno en este caso es un mejor
    # método para comparar artistas, ya que obtenemos el resultado esperado de gran similitud entre
    # Metallica, Extremoduro y AC/DC de género hard rock y diferencias con Hans Zimmer un compositor
    # de bandas sonoras. Sin embargo, con la similitud euclidiana hemos obtenido que ningún artista se parece
    # entre él, en ese caso esto no es correcto

    # Tarea 8
    a = api_audio(['Radiohead', 'David Bowie', 'Måneskin'])

    # Mostramos la tabla creada
    print(a)

    # Creamos el archio csv
    from_df_to_csv(a, 'artists_audiodb.csv')


    artista = list(set(result['artist_name']))
    a = api_audio(artista)

