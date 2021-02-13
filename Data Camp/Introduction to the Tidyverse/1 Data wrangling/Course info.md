# Tidyverse

Collection of data science tools within R for transforming and visualizing data. 



## Packages

### - Gapminder

- Para instalar: install.packages("gapminder")
- Para usarlo en el codigo: library(gapminder)
    gapminder me va a dar informacion como un dataframe. Esto tiene columnas (variable) y rows (observation).

### - dplyr

- Para instalar: install.packages("dplyr")
- Para usarlo en el condigo: library(dplyr)


## The verbs
- Los pasos pequenos para transformar la data
- Cada vez que aplico un verbo tengo que usar un pipe que se representa como %>% y quiere decir "tome lo que esta antes y coloquelo en el siguiente paso"
- Despues del pipe puedo usar el verbo, como por ejemplo filter


### Filter
- Se usa solo cuando quiero analizar un subset de mis observaciones
- Un filtro lo que contesta es un nuevo dataset pero no sobreescribre el dataset original


### Arrange
- Se explica solo lo que hace es un sort de las observaciones en un dataset de manera desendiente o ascendiente basado en una de sus variables.

- Por defecto se va a hacer un sort por el valor mas bajo
- Para hacerlo de manera descendiente tengo que hacer esto arrange(desc(XvariableX))

### Mutate 
- Se usa para cambiar o agregar una nueva variable.
- Dentro del statement o los parentesis es que se pone lo que se quiere cambiar

Esto se hace para limpar un poco la informacion. Por ejemplo gapminder %>%
  mutate(pop = pop/100) me va a poner todo en base 100 con puntos

Si quisiera agregar una nueva variable para encontrar la cantidad total de personas en un pais y el total de GDP puedo hacer una multiplicacion asi
gapminder %>%
  mutate(gdp = gdpPercap * pop) 


### Combinar verbos
Si yo quiero por ejemplo identificar el GDP-per-capita mas alto en un ano yo puedo correr algo asi:

gapminder %>%
filter(year==2007) %>% arrange(desc(gdpPercap))

Si yo quisiera filtrar por un ano en especifico, hacerle sort descendientemente y crear una nueva variable que me de una multiplicacion aritmetica hago lo siguiente
gapminder %>%
  mutate(gdp = gdpPercap * pop) %>%
  filter(year==2007) %>%
  arrange(desc(gdp))

