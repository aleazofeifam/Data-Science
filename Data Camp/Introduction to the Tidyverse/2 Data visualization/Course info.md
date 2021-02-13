# Tidyverse 



## Visualizing with ggplot2
- Para instalarlo: **install.packages("ggplot2")**
- Para usarlo en el codigo: **library(ggplot2)**


 



- This is to present data in a graph, since its easier to understand.
- This package helps to build scatterplots with variables on X- and Y- axis
- Se usa frecuentemente con dpylr
- Si yo quisiera revisar la relacion que existe entre el wealth de un pais y lifeexpentancy. Yo podria hacer una comparativa de dos variables y generar algo asi


 ```R
DataRelacionalEntreElGDPPerCapitayLaExpectativaDeAnos <- gapminder %>% 
 filter(year==2007) %>% 
 arrange(desc(gdp))

```
 - Una vez tengo la variable con la informacion filtrada entonces ya puedo visualizarla

 ```R
ggplot(DataRelacionalEntreElGDPPerCapitayLaExpectativaDeAnos,aes(x =gdpPerCap, y =lifeExp)) +
geom_point()

```
- geom_point es el tipo de grafico que quiero imprimir


## Asignacion de variables
- Lo que tengo que hacer es usar una flcha para la derecha y asi se va a guardar, ejemplo:

```R
DataRelacionalEntreElGDPPerCapitayLaExpectativaDeAnos2 <- gapminder %>% 
  mutate(gdp = gdpPercap * pop) %>% 
  filter(year==1952) %>% 
  arrange(desc(gdp))
```
- Y despues si quiero ver el resultado nada mas llamo la variable.



## Log scales

- Cuando la distrubicion de la data no hace clara la informacion es mejor usar una escala logaritimica. Una escala donde cada fixed distance representa la multiplicacion de un valor
- Para indicarle que quiero que la variable en el eje X este en base logaritimica de 10

```R
ggplot(DataRelacionalEntreElGDPPerCapitayLaExpectativaDeAnos,aes(x =gdpPerCap, y =lifeExp)) +
geom_point() +
scale_x_log10()
```

## Estitica en los graficos

### Color
- Ayuda a visualizar la informacion usando una variable. Si yo quisiera que los colores en grafico se agruparan dependiendo el color tengo que meter color = XvariableX dentro de los ejes. Ejemplo:

```R
ggplot(DataRelacionalEntreElGDPPerCapitayLaExpectativaDeAnos,aes(x =gdpPerCap, y =lifeExp, color = continent)) +
geom_point() +
scale_x_log10()
```

### Tamano 
```R
ggplot(DataRelacionalEntreElGDPPerCapitayLaExpectativaDeAnos,aes(x =gdpPerCap, y =lifeExp, size = pop)) +
geom_point() +
scale_x_log10()
```

## Faceting
- Poner otras categorias, con ggplot2 se puede dividir la informacion con base en una variable y se pueden usar diferentes facetas. Para usarlo al igual que con los logaritmos se usa usando un mas 

```R
ggplot(DataRelacionalEntreElGDPPerCapitayLaExpectativaDeAnos,aes(x =gdpPerCap, y =lifeExp, size = pop)) +
geom_point() +
scale_x_log10() +
facet_wrap(~ continent)
```
