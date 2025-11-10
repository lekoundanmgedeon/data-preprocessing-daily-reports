
import pandas as pd


#this command read the dataset and save it in a variable called world_gapminder
world_gapminder = pd.read_csv('data/gapminder.tsv' , sep='\t')


#Here we are writing filter conditions: "country=angola"  and "life exp > 40"
world_gapminder[(world_gapminder['country'] == 'Angola')  & ( world_gapminder['lifeExp']> 40)]


# Here we are filtering the original dataframe to only focus on entries from the African continent
african_slice =  world_gapminder[world_gapminder['continent']=='Africa']

#from the african continent entries, we want only the entries where the years go from 1980 to 1990
african_slice_80s = african_slice[african_slice['year'].between(1980 , 1990,inclusive="both")]

#you could have also done it this way:
another_african_slice_80s = african_slice[(african_slice['year']>=1980)&(african_slice['year']<=1990)]


#from the observations coming from Africa and the 80s, lets find the one that has the highest GDP
african_slice_80s[african_slice_80s['gdpPercap'] == african_slice_80s['gdpPercap'].max()]
