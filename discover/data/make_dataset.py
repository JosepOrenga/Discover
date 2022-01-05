import shutil
import os


def unzip_file(file_name, extrac_dir):
    """
    Descomrime un archivo
    :param file_name: nombre del archivo a descomprimir
    :param extrac_dir: directorio donde se almacená el
    archivo despomprimido
    :return: devulve el número de archivos
    en el directio donde se almacenan los archivos
    descomprimidos
    """

    # Con unpack_archive descomprimimos un archivo
    shutil.unpack_archive(file_name, extrac_dir)

    return len(os.listdir(extrac_dir))
