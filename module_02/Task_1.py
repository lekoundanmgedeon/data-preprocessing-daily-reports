

#1.
import pandas as pd

df_togo =  pd.DataFrame(togo_data)



# You can try and access to first few rows of the data to get some flavour of it.

df_togo.head()

# For the last few rows

df_togo.tail()


# You can randomly access 10 rows

df_togo.sample(10)

# 2.

# Please note that there are so many questions one can  derive from just observing the dataframe. See some below

 """Just by looking at hospital names, we can see that some have German names. Therefore, some questions can  emerge
 - Just look at the access to electricity column, some questions can also emerge.
 - Look at the birth rate, some questions can also emerge.
 """
 
# ==============================


#4. 
"""
     Here are some other questions.
"""     

"""   
a- how many German hospitals do we have in Togo?
"""
# We do this based on the index of the rows. 
df_germans_01  = df_togo.iloc[  [10, 11, 15 , 16 , 19] , : ]

"""
We can also do it based on some patterns that we noticed from the dataframe. For 
instance, the names of german hospitals contain "Deu", "Berlin" or  "Ger" or "Vog".
Let us use that to filter the german hospitals.
"""

df_germans_02 = df_togo[  df_togo['Hospital Name'].str.contains("Ger|Deu|Berlin|Vog")]

"""
b- How many non-german hospitals do we have?

We can just use the complementary of the condition above to filter the NON-GERMAN hospitals
"""
df_non_germans = df_togo[  df_togo['Hospital Name'].str.contains("Ger|Deu|Berlin|Vog")  == False]


"""
c- What are the hospitals where children have more than 14% of chance to stay alive after birth?
"""

df_togo[df_togo['Birth rate'] > 0.14]


"""
d- How many of them are Germans?
....
"""
df_togo[  (df_togo['Hospital Name'].str.contains("Ger|Deu|Berlin|Vog"))  &  (df_togo['Birth rate'] > 0.14  )]


# ==============================


# ==============================


# ==============================


#6.
"""
What are the hospitals where the birth rate is less than `0.50`?
"""

df_togo[df_togo['Birth_Rate'] < 0.5]


"""
What are the hospitals that have access to electricity?
"""
df_togo[df_togo['Light'] == 'Yes']



"""
Are the Germans Hospitals in Togo always supplied with electricity?
"""
# Look at the column "Access to Electricity and conclude"

df_togo[  df_togo['Hospital Name'].str.contains("Ger|Deu|Berlin|Vog")]



#7. 

"""#First, create a new column called date and assign the scheduled dates variable to it
#and then use the pd.to_datetime  function to convert it into a date_time format."""

# Before you run the line below make sure the schedule_dates variables is created in your notebook.


df_togo['Delivery_Dates'] =   scheduled_dates
df_togo['Delivery_Dates'] = pd.to_datetime(df_togo['Delivery_Dates'])


#7.
"""Create a week_No column that indicates the week of the year from the Dates column
It has been made possible, thanks to the pd.to_datetime function"""

df_togo['Week_No'] = df_togo['Delivery_Dates'].dt.isocalendar().week

# how many ceremonies  will she be able to make it in person? 

df_minister_presence = df_togo[ (df_togo['Week_No']>= 20 )  & (df_togo['Week_No']< 40)]



# You can write the content of  this new sub-data frame into a csv file for later purposes.

df_minister_presence.to_csv("minister_presence.csv", index=False)

#The index=False  is to avoid to save indexes. After saving it, make sure you see where it is located in your machine.



