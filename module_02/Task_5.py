import pandas as pd


#this command read the dataset and save it in a variable called world_gapminder
world_gapminder = pd.read_csv('data/gapminder.tsv' , sep='\t')


# Lets filter the dataset to only focus on the entries that match the SE_Countries.
south_europe = world_gapminder[world_gapminder['country'].isin(SE_countries)]


#from the entries, we want only the entries where the years go from 2000 to 2009
south_eu_2000 = south_europe[(south_europe['year'].between(2000, 2010, inclusive="both"))] 

#for the minimal gdp , see below.
south_eu_2000[south_eu_2000['gdpPercap'] == south_eu_2000['gdpPercap'].min() ]

#you can use the same logic to do the same below.

