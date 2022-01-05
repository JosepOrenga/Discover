import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))

sys.path.append(d)

import unittest

from discover.data.make_dataset import *
from discover.features.build_features import *
from discover.preprocessing.data_prepocessing import *
from discover.visualization.visualize import *
from discover.optimization.optimization import *
from discover.analysis.data_analysis import *
from discover.API.request import *

if __name__ == "__main__":

    # Test para las funciones de data_analysis
    class TestDataAnalysis(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            # Importamos nuestros data
            cls._df = fill_null_by_mean(
                capital_letter(denormalized_df('../data/tracks_norm.csv', '../data/albums_norm.csv',
                                               '../data/artists_norm.csv', ';', 'inner', 'album_id', 'artist_id'),
                               'artist_name'), 'track_popularity')

        def test_nulls_column(self):

            # Comprobamos que se sustituyen todos los nulos
            self.assertEqual(nulls_of_column(self._df, 'track_popularity'), 0)

        def test_max_mean_min(self):
            # Comprobamos que los valores se calculan correctamente
            maximum, mean, minimum = max_mean_min(self._df, "artist_name", "Adele", "liveness")
            self.assertEqual(maximum, 0.978)
            self.assertEqual(mean, 0.2326340909090909)
            self.assertEqual(minimum, 0.0473)

        def test_mean_feature_album(self):
            # Comprobamos que el valor se calcula correctamente
            self.assertEqual(mean_feature_album(self._df, "artist_name", "Extremoduro", "album_name", "energy")["Agila"],
                             0.9075714285714286)

        def test_number_of_columns(self):
            # Comprobamos que el valor se calcula correctamente
            self.assertEqual(number_of_columns(self._df), 33)

        def test_number_of_rows(self):
            # Comprobamos que el valor se calcula correctamente
            self.assertEqual(number_of_rows(self._df), 35574)

        def test_tracks_of_epoch(self):
            # Comprobamos que el valor se calcula correctamente
            self.assertEqual(tracks_of_epoch(self._df, "release_year", 1990, 1999), 4638)

        def test_tracks_max_popularity_of_epoch(self):
            # Comprobamos que el valor se calcula correctamente
            self.assertEqual(
                tracks_max_popularity_of_epoch(self._df, "track_name", "release_year", "track_popularity", 2000, 2021),
                "Beggin'")
            self.assertNotEqual(
                tracks_max_popularity_of_epoch(self._df, "track_name", "release_year", "track_popularity", 2000, 2021),
                "Airbag - Remastered")

        def test_tracks_of_artist(self):
            # Comprobamos que el valor se calcula correctamente
            self.assertEqual(tracks_of_artist(self._df, "artist_name", "The Killers"), 206)
            self.assertNotEqual(tracks_of_artist(self._df, "artist_name", "The Killers"), 123)
            self.assertNotEqual(tracks_of_artist(self._df, "artist_name", "The Killers"), 'e')

        def test_word_in_track(self):
            # Comprobamos que el valor se cambia correctamente
            self.assertEqual(word_in_track(self._df, 'track_name', 'The'), 5193)

        def test_every_decade(self):
            # Comprobamos que el valor se calcula correctamente
            self.assertIn('David Bowie', every_decade(self._df, "artist_name", "release_year"))
            self.assertIn('Ennio Morricone', every_decade(self._df, "artist_name", "release_year"))
            self.assertNotIn('AC/DC', every_decade(self._df, "artist_name", "release_year"))


    class TestDataVisualization(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            # Importamos nuestros data
            cls._df = fill_null_by_mean(
                capital_letter(denormalized_df('../data/tracks_norm.csv', '../data/albums_norm.csv',
                                               '../data/artists_norm.csv', ';', 'inner', 'album_id', 'artist_id'),
                               'artist_name'), 'track_popularity')

        def test_density_histogram(self):
            # Sabemos que la suma de altura de todas las barras debe ser uno
            self.assertEqual(round(density_histogram(self._df, 'artist_name', 'Ed Sheeran', 'acousticness', 90), 2), 1)

        def test_density_hist_two_singers(self):
            # Como tenemos a dos cantantes la suma de la altura de sus barras debe ser 2
            self.assertEqual(round(density_hist_two_singers(self._df, 'artist_name', 'Adele', 'Extremoduro', 'energy', 90), 2), 2)

        def test_cosinus_similarity(self):
            cs = plot_cosinus_similarity(self._df,
                                      ['artist_name', 'danceability', 'energy', 'key',
                                       'loudness', 'mode', 'speechiness', 'acousticness',
                                       'instrumentalness', 'liveness', 'valence', 'tempo',
                                       'time_signature'],
                                      ['Metallica', 'Extremoduro', 'AC/DC', 'Hans Zimmer'],
                                     'artist_name')

            self.assertLessEqual(cs.all(), 1)
            # Comprobamos de que se trara de una matriz simétrica
            self.assertTrue(cs.all(), cs.T.all())

            # Comprbamos que es una matriz 4x4 con el número de artístas introducidos
            self.assertEqual(cs.shape, (4, 4))

            # Comprbamos que la diagonal principal son 1
            self.assertTrue(np.around(np.diag(cs), 2).all(), 1)

        def test_euclidean_similarity(self):
            es = plot_euclidean_similarity(self._df,
                                      ['artist_name', 'danceability', 'energy', 'key',
                                       'loudness', 'mode', 'speechiness', 'acousticness',
                                       'instrumentalness', 'liveness', 'valence', 'tempo',
                                       'time_signature'],
                                      ['Metallica', 'Extremoduro', 'AC/DC', 'Hans Zimmer'],
                                     'artist_name')
            # Todos los elemtos de la matriz deben de ser cero o menor
            self.assertLessEqual(es.all(), 1)

            # Comprobamos de que se trara de una matriz simétrica
            self.assertTrue(es.all(), es.T.all())

            # Comprobamos que es una matriz 4x4 con el número de artístas introducidos
            self.assertEqual(es.shape, (4, 4))

            # Comprobamos que la diagonal principal son 1
            self.assertTrue(np.around(np.diag(es), 2).all(), 1)

        def test_barplot_albums(self):
            self.assertIn('A Head Full of Dreams', barplot_albums(self._df, 'artist_name', 'Coldplay', 'album_name', 'danceability', 90))
            self.assertTrue(15, len(barplot_albums(self._df, 'artist_name', 'Coldplay', 'album_name', 'danceability', 90)))


    class TestOptimization(unittest.TestCase):
        def test_pandas_method(self):

            # Comprobamos que selecciona a todos los artistas
            self.assertEqual(len(get_column_pandas('../data/artists_norm.csv', 'name')), 68)

            # Comprobamos que contiene los nombre de los artistas
            self.assertIn('Radiohead', get_column_pandas('../data/artists_norm.csv', 'name'))

        def test_readcsv_method(self):

            # Comprobamos que selecciona a todos los artistas
            self.assertEqual(len(get_column_read('../data/artists_norm.csv', 'name')), 68)

            # Comprobamos que contiene los nombre de los artistas
            self.assertIn('Radiohead', get_column_read('../data/artists_norm.csv', 'name'))

        def test_compare_methods(self):
            pandas_time, read_time = compare_methods('../data/artists_norm.csv', 'artist_id')

            # Comprobsmos que nuesrto méstodo es más rápido
            self.assertLess(read_time, pandas_time)


    class TestMakeDataset(unittest.TestCase):

        def test_unzip_file(self):

            # Comprobamos que los archivos se descomprimen,
            # Para ello comprobamos que el directorio donde se descomprimen
            # tiene más de un archivo, el zip inicial
            self.assertGreater(unzip_file('../data/data.zip', '../data'), 1)

    class TestAPI(unittest.TestCase):

        def setUp(self):
            # Cargamos los datos
            # En ese caso no empleamos setUpclass, ya que altener solamente una función
            # no repetimos código
            self.df =  api_audio(['Radiohead', 'David Bowie', 'Måneskin'])

        def test_from_df_to_csv(self):

            # Comprobamos que el archivos se ha creado
            self.assertTrue(from_df_to_csv(self.df, 'artists_audiodb.csv'))


    suite_tracks = unittest.TestSuite()
    suite_tracks.addTest(unittest.makeSuite(TestDataAnalysis))
    suite_tracks.addTest(unittest.makeSuite(TestDataVisualization))
    suite_tracks.addTest(unittest.makeSuite(TestOptimization))
    suite_tracks.addTest(unittest.makeSuite(TestMakeDataset))
    suite_tracks.addTest(unittest.makeSuite(TestAPI))
    unittest.TextTestRunner(verbosity=2).run(suite_tracks)