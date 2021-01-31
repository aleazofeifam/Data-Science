import csv

ArchivoDeCompas = open('compras.csv', mode='rt')

LeerArchivoDeCompras = csv.reader(ArchivoDeCompas)
ArchivosDeComprasLimpio = list(LeerArchivoDeCompras)


print("Leer un archivo")
print(ArchivosDeComprasLimpio)



ArchivosDeComprasLimpio.append(['24/03/2020', 'Nueva libro', '1', '1', '1'])
ArchivosDeComprasLimpio.append(['24/03/2020', 'Nueva ropa', '2', '1.25', '2.5'])
ArchivosDeComprasLimpio.append(['24/03/2020', 'Nueva lapicero', '1', '2', '2'])
file = open('compras_actualizadas.csv', 'wt', newline='')
writer = csv.writer(file)
writer.writerows(ArchivosDeComprasLimpio)
file.close()