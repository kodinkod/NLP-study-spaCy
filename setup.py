from distutils.core import setup
from Cython.Build import cythonize
import numpy


setup(name='spacy text app',
     ext_modules=cythonize("spacytext.pyx", language="c++"),
     include_dirs=[numpy.get_include()]
)

"""
Это обычный сценарий setup.py для distutils/setuptools, за исключением двух дополнений, 
связанных с нашим примером. Во-первых, мы импортировали numpy , 
после чего явным образом указали, где искать заголовочные (.h)
 файлы библиотеки  во избежание ошибки компиляции numpy/arrayobject.h, 
 возникающей на некоторых системах. Во-вторых, мы воспользовались еще одной опцией — language="c++" , 
 указав тем самым на необходимость применить компилятор C++, а не C, как это происходит по умолчанию.
"""