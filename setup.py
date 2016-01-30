#!/usr/bin/env python
# encoding: utf-8

from numpy.distutils.core import setup, Extension

module = Extension('_floris', sources=['src/florisse/floris.f90', 'src/florisse/adStack.c', 'src/florisse/adBuffer.f'],
                   extra_compile_args=['-O2', '-c'])

setup(
    name='FLORISSE',
    version='0.0.0',
    description='differentiable floris wake model with cosine factor',
    install_requires=['openmdao>=1.5'],
    package_dir={'': 'src'},
    ext_modules=[module],
    packages=['florisse'],
    license='Apache License, Version 2.0',
)