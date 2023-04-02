#include <Python.h>
// #include "funkcje.h"

//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){

static PyObject *mod_met(PyObject *self, PyObject *args){
	int a,b;
	int c;
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "ii|iO", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}

	int s=0;

	if(d){
		int r=PyList_Size(d);
		for(int i=0; i<r; i++)
			s+=PyLong_AsLong(PyList_GetItem(d, i));
		s+=a+b+c;
	}
	else if(c)
		s = a+b+c;
	else
		s = a+b;

	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}


static PyObject *mod_CSort(PyObject *self, PyObject *args){
	PyObject *a;
	int b;
	if(!PyArg_ParseTuple(args, "Oi", &a, &b)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	PyObject *tmp = malloc(b*sizeof(PyObject));
	for(int i = 0; i < b; i++)
		tmp[i] = a[i];

    for(int i = 1; i < b; i++)
    {
        int add_el = PyLong_AsLong(PyList_GetItem(tmp, i));
        int j = i-1;
        while(j >= 0 && PyLong_AsLong(PyList_GetItem(tmp, j))>add_el)
        {
			PyList_SetItem(tmp, j+1, PyList_GetItem(tmp, j));
            j = j-1;
        }
		PyList_SetItem(tmp, j+1, Py_BuildValue("i", add_el));
    }

	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("O", tmp);
}

//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."}, 
	{"CSort", (PyCFunction)mod_CSort, METH_VARARGS, "Funkcja ..."}, 
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
