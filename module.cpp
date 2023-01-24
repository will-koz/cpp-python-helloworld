#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "helloworld.hpp"
#include "module.hpp"

struct PyMethodDef module_methods[] = {
	{ "helloworld", (PyCFunction) helloworld, METH_NOARGS, "Says Hello World." }, /* METH_VARARGS */
	{ NULL }
};

struct PyModuleDef hellomodule = {
	PyModuleDef_HEAD_INIT, "module", "Hello World Module", -1, module_methods
};

PyObject* helloworld (PyObject* self) {
	printf("Hello World from module.cpp .\n");
	return Py_BuildValue("s", gettext());
	// Py_RETURN_NONE;
}

PyMODINIT_FUNC PyInit_module () {
	return PyModule_Create(&hellomodule);
}
