from setuptools import setup
from Cython.Build import cythonize

import numpy

setup(ext_modules = cythonize('run_as_cython.pyx'))