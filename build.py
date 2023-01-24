#!/usr/bin/python3

# Information can be found here about more build options
# https://docs.python.org/3/extending/building.html#building

from distutils.core import setup, Extension

module_name = "module"
version = "1.0"
file = "cppfiles.txt"
files = []
# files = ["module.cpp", "helloworld.cpp"]

with open(file, "r") as f:
	files = f.readlines()
	for i in range(len(files)):
		files[i] = files[i].strip()

setup(name = module_name, version = version, ext_modules = [Extension(module_name, files)])
