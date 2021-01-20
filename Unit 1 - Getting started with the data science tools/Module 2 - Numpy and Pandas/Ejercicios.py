



##MANEJO DE ARCHIVOS JSON
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


##MANEJO DE ARCHIVOS XML

##Cargar el xml
import xml.dom.minidom
raw_xml = xml.dom.minidom.parse('books.xml')

libros_object = raw_xml.documentElement
libros_object

books = libros_object.getElementsByTagName('Book')
books

for item in books:
    Author = item.getElementsByTagName('Author')
    print(Author)

##Aqui compruebo que 'Author' en cada objeto solo tengo un valor. Si me da 1 es que si solo hay una llave que abre y cierre para author
print("La cantidad de autores que hay por libro")
for item in books:
    print(len(item.getElementsByTagName('Author')))


##Leer el xml
print("Los autores (tengo que definir el subindice para seleccionar cual resultado quiero que me traiga)")
for item in books:
    Author = item.getElementsByTagName('Author')[0].childNodes
    print(Author)

print("Los autores con el valor de la data completo, (tengo que definir el indice para seleccionar cual resultado quiero que me traiga)")
for item in books:
    Author = item.getElementsByTagName('Author')[0].childNodes[0].data
    print(Author)

print("********Los autores********")
for item in books:
    target = 'Autor'
    for tag in item.getElementsByTagName('Author'):
        for nodo in tag.childNodes:
            autor = nodo.data
            print(autor)


for item in books:
    print('Procesando libro ...')
    
    # Recuperamos los campos
    Author = item.getElementsByTagName('Author')[1].childNodes[1].data
    Title = item.getElementsByTagName('Title')[0].childNodes[0].data
    Genre = item.getElementsByTagName('Genre')[0].childNodes[0].data
    Price = item.getElementsByTagName('Price')[0].childNodes[0].data
    PublishDate = item.getElementsByTagName('PublishDate')[0].childNodes[0].data
    Description = item.getElementsByTagName('Description')[0].childNodes[0].data
    
    # Imprimimos los campos
    print('\t * Autor: {} '.format(Author))
    print('\t * Título: {} '.format(Title))
    print('\t * Género: {} '.format(Genre))
    print('\t * Precio: {} '.format(Price))
    print('\t * Fecha publicación: {} '.format(PublishDate))
    print('\t * Descripción: {} '.format(Description))
    print('-'*25)


    