# Discover  

Discover es una aplicación desarrollada para descubrir nuevos artistas musicales financiada por UOC Sound Dynamics.
Donde se han creado una seria de funciones para, analizar, visualizar y optimizar nuestros datos.

# Instalación

Para poder disponer de esta aplicación deberemos de seguir los siguientes pasos:

En primer lugar, procederemos a instalar PyCharm, siguiendo las instrucciones oficiales:

```$ sudo snap install pycharm-community --classic```

Una vez instalado, ejecutaremos PyCharm:

```$ pycharm-community```

Para crear el proyecto en Pycharm emplearemos el comando

```$ mkdir PycharmProjects/Discover```

Y lo activaremos con el comando

```$ source bin/activate```

A continuación instalaremos las librerías necesarias, para ello emplearemos el comando

```pip install -r requirements.txt```

Para poder mostrar los gráficos debemos de instalar el GUI backend `tk`.
Todo lo que debemos de hacer es instalar `tkinter` a través de la terminal
de Linux en nuestro entorno virtual de Pycharm con el comando

 ```sudo apt-get install python3-tk```

# Despliegue

## Intalación

Ejectamos cd en el directorio raiz donde se encuentra setup.py

Y a continuación ejectamos el comando ```python setup.py install```

Una vez tengamos instaladas las librerías necesarias ya podemos pasar al despliegue del proyecto,
primero de todo deberemos de ejecutar el documento Tareas.py, que contiene la función que descomprimirá 
el archivo con los datos con los que necesitaremos trabajar en un futuro y una serie de ejemplos para cada una de
las funciones creadas, con las que posteriormente podrás practicar y aprender su funcionalidad.

Para ello ejecutaremos el comando

```python3 Tareas.py```

# Test

Para ejecutar los test lo haremos con el comando ```python3 test.py```, observaremos si los test se
ejecutan correctamente

Finalmente para saber que porcentaje de codigo está cubierbo por nuestras funciones ejecutaremos
en primer lugar el cmando ```coverage run test.py``` y en segundo lugar para ver el resultado
```coverage report -m```

