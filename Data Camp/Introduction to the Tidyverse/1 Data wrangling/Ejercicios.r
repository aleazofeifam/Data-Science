print ("Loading 2 modules")


library(gapminder)
library(dplyr)

print ("El dataset")
gapminder


##  Estoy diciendo que quiero filtar por observaciones del 2007

print("**************Filter**************")
# Filter the gapminder dataset for the year 1957
gapminder %>%
filter(year==1957)


# Filter for China in 2002, hay dos criterios
gapminder %>%
filter(country=="China", year==2002)



print("**************Sort/Arrange**************")

# Sort in ascending order of lifeExp
gapminder %>%
arrange(lifeExp)

  
# Sort in descending order of lifeExp
gapminder %>%
arrange(desc(lifeExp))


# Filter for the year 1957, then arrange in descending order of population
gapminder %>%
filter(year==1957) %>% arrange(desc(pop))


print("**************Mutate**************")

# Use mutate to change lifeExp to be in months
gapminder %>%
mutate(lifeExp = 12* lifeExp)


# Use mutate to create a new column called lifeExpMonths
gapminder %>%
mutate(lifeExpMonths = 12 * lifeExp)

# Filter, mutate, and arrange the gapminder dataset
gapminder %>%
filter(year==2007) %>%
mutate(lifeExpMonths = 12 * lifeExp) %>%
arrange(desc(lifeExpMonths))
