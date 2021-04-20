# Procesamiento de datos y librerías para ciencia de datos: Numpy, Pandas

Profesor: Alejandro Azofeifa **||** Clase: Las herramientas del científico de datos ||

## Trabajar con datos estructurados

### CSV

Un archivo de extensión CSV (comma separated values) se trata de un archivo de texto plano que contiene todos sus datos separados por comas. Estos archivos se encuentran estructurados por líneas (filas) y cada campo separado por comas puede actuar como una columna. Por lo general, son visualizados en software para hojas de cálculo, aunque, en esta ocasión, veremos cómo leer y escribir CSV desde Python.

Para importar y poder leer un archivo CSV en Python, lo primero que tenemos que saber es cómo importar una librería.

Una librería consiste en un conjunto de funciones empaquetadas que, al importarse en Python, nos permiten disponer de más funcionalidades para realizar diferentes tareas, en este caso, para procesar archivos. En Python, para importar una librería escribiremos lo siguiente: “import nombre_de_la_librería”.

**Paso 1** 

Tener la data en un formato esperado y ordenado.

Guardar esa información en un archivo con extension csv.

```csv
FECHA,ARTICULO,CUANTIA,PRECIO UNIDAD,TOTAL
15/03/2020,Barra Pan,2,0.55,1.1
16/03/2020,Bolígrafo Bic,3,0.22,0.66
17/03/2020,Cuaderno,1,1.25,1.25
18/03/2020,Refresco,5,0.8,4
19/03/2020,Silla Gamer,1,153,153
20/03/2020,Paquete folios A4,3,2.48,7.44
21/03/2020,Pack x6 Vaso cristal,2,6,12
22/03/2020,Manzanas (Kg.),1,2.48,2.48
23/03/2020,Naranjas (Kg.),2,1.29,2.58
24/03/2020,Naranja Malla,1,1.5,1.5
```

**Paso 2**

Hacer uso de la librería CSV e importarla al inicio de nuestro código. 

```python
import csv
```

**Paso 3**

Inicializar el archivo en una variable para poder trabajar con el.

```python
ArchivoDeCompras = open('ElCSVFile.csv', mode='rt')
ArchivoDeCompras 
```

Cuando se abre un archivo se tiene que especificar si se quiere leer "r" o si se quiere escribir "w".
Otro parámetro que se puede indicar es si el tipo de data que se va a trabajar es de tipo texto "t" o binario "b".

**Paso 4**

Procesar el archivo y que tenga en Python la estética de una tabla, se hará uso de la función de la librería CSV “csv.reader”

```python
ElArchivoDeComprasLeido = csv.reader(ArchivoDeCompras)
ElArchivoDeComprasLeido 
```

**Paso 5**

Limpiar el objeto y darle formato de lista para ser usado

```python
ElArchivoDeComprasComoLista = list(ElArchivoDeComprasLeido)
ElArchivoDeComprasComoLista 
```

### XML

```xml
<Catalog>
   <Book id="bk101">
      <Author>Garghentini, Davide</Author>
      <Title>XML Developer's Guide</Title>
      <Genre>Computer</Genre>
      <Price>44.95</Price>
      <PublishDate>2000-10-01</PublishDate>
      <Description>An in-depth look at creating applications
      with XML.</Description>
   </Book>
   <Book id="bk102">
      <Author>Garcia, Debra</Author>
      <Title>Midnight Rain</Title>
      <Genre>Fantasy</Genre>
      <Price>5.95</Price>
      <PublishDate>2000-12-16</PublishDate>
      <Description>A former architect battles corporate zombies,
      an evil sorceress, and her own childhood to become queen
      of the world.</Description>
   </Book>
</Catalog>
```

### JSON

```json
{
    "IBEX_35": [
        {
            "ACCIONA": [
                95.95,
                14.7,
                95.95,
                95.95,
                6.302
            ]
        },
        {
            "B. SANTANDER": [
                2.2195,
                9.99,
                2.2195,
                2.2195,
                203.685
            ]
        },
        {
            "IBERDROLA": [
                8.588,
                4.32,
                8.588,
                8.588,
                98.298
            ]
        }
    ],
    "IBEX_MEDIUM_CAP": [
        {
            "EUSKALTEL": [
                6.15,
                3.71,
                6.15,
                6.02,
                947
            ]
        },
        {
            "LIBERBANK": [
                0.1552,
                7.48,
                0.1648,
                0.1551,
                304.384
            ]
        },
        {
            "SACYR": [
                1.196,
                4.09,
                1.226,
                1.196,
                125.271
            ]
        }
    ],
    "NASDAQ": [
        {
            "MSFT": [
                1,
                2,
                3,
                4,
                5
            ]
        },
        {
            "APPL": [
                5,
                4,
                3,
                2,
                1
            ]
        }
    ]
}
```