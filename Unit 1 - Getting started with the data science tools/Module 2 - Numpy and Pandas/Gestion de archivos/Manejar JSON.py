
##Cargar json y leerlos en consola
import json
with open('mercados.json', 'rb') as InformacionDeMercados:
    mercados =json.load(InformacionDeMercados)
mercados

##Lectura del archivo
print("******Imprimir cada key******")
print(mercados.keys())

print("******Imprimir toda la info de la llave en una sola linea******")
print(mercados['IBEX_MEDIUM_CAP'])

print("******Imprimir los arrays de cada key de manera ordenada******")
for Arreglos in mercados['IBEX_MEDIUM_CAP']:
    print(Arreglos)

print("******Imprimir los values de cada key de manera ordenada******")
for Arreglos in mercados['IBEX_MEDIUM_CAP']:
    for Valores in Arreglos.keys():
        print(Arreglos[Valores])

##Escritura en el archivo
NuevoMercado = [
    {'MSFT': [1, 2, 3, 4, 5]},
    {'APPL': [5, 4, 3, 2, 1]}
]
mercados.update({'NASDAQ' : NuevoMercado})

print("La lista completa de la llaves, incluyendo los nuevos")
print(mercados.keys())

with open('Mercados_update.json', 'w') as outfile:
    json.dump(mercados, outfile)

