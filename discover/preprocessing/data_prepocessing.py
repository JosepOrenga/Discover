def capital_letter(df,  column=str):
    """
    Transforma una columna para que cada
    palabra empiece por mayúscula
    :param df: dataframe
    :param column: columna a transformar
    :return: dataframe transformado
    """

    # Para que cada palabra del nombre empiece
    # por mayúscula podemos emplear la función title()
    # Si la palabra empieza por minúscula islower()
    df[column] = [i.title() if i.islower() else i for i in df[column]]

    return df


def fill_null_by_mean(df, column=str):
    """
    Sustiyue los nulos de una columna por la media
    :param df: dataframe a modificar
    :param column: columna a modificar
    :return: float() la media de la columna
    """
    # Denotamos la media de la columna
    mean = df[column].mean()

    # Con fillna() sustituimos los nulos por el valor indicado
    # es este caso la media
    df[column] = df[column].fillna(
        mean)

    return df

