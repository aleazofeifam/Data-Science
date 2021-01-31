import numpy

print("****************Incializar un arreglo****************")
ArregloDeNumeros = numpy.array([10, 20, 98, 34])

ArregloDeNumeros
print(type(ArregloDeNumeros))
print("*********************************************************")


print("****************Inicializar una Tupla****************")
mi_tupla = (1, 58, 63, 45)
print(type(mi_tupla))
arr_tuple = numpy.array(mi_tupla)

print(arr_tuple)
print(type(arr_tuple))
print("*********************************************************")

print("****************Diccionario en un arreglo****************")
my_dict = {'one': 'uno', 
           'two': 'dos',
           'three': 'tres'}

dict_list = list(my_dict.items())
print(dict_list)

arr_dict = numpy.array(dict_list)
print(arr_dict)
print("*********************************************************")

