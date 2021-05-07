# Laboratorio_E5

## Setup
Es requerido tener instalado las librerias Open Camera Vision (OpenCV), argparse, matplotlib y Numpy para que funcione el proyecto, en caso de no tenerlas instaladas, se requerirá ingresar en la consola los siguientes comandos:

Para instalar el módulo de Open Camera Vision (OpenCV) de python:

```
pip install opencv-python
```
Para instalar el módulo de argparse:

```
pip install argparse
```
Para instalar el módulo de Matplotlib de python:

```
pip install matplotlib
```
Para instalar el módulo de Numpy de python:

```
pip install numpy
```

## Funcionamiento
Para que el programa corra le debera ingresar el path de la imagen que desea utilizar con los filtros en forma de argumento. Debera ingresarlo de la siguiente forma, remplazando image por el path o nombre de la imagen que desea utilizar:
```
python convolution.py -i image.jpg
```

En caso de no querer visualizar el resultado en representacion, y solo desea guardar las imagenes con sus respectivos nombres, se necesita corre rel siguiente comando:
```
python convolution.py -i image.jpg -v False
```

El programa se encargara de convertir la imagen en forma de matriz bidimensional en escala de grises para su procesamiento, el cual pasara por tres filtros kernel, un detector de bordes (edge_detection); un desenfoque gaussiano (gaussian_blur); y un desenfoque simple (simple_blur), donde cada uno sera guardado con su nombre respectivo de **"*Output_kernel.jpg*"**.

