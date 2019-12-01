# Pandas DataFrames
# Pandas is a high-level data manipulation tool developed by Wes McKinney. It is built on the Numpy package and its key data structure is called the DataFrame. DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.

# There are several ways to create a DataFrame. One way way is to use a dictionary. For example:

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98]
       }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)



# As you can see with the new brics DataFrame, Pandas has assigned a key for each country as the numerical values 0 through 4. If you would like to have different index values, say, the two letter country code, you can do that easily as well.

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

print("====== Print out BRICS ======")
# Print out brics with new index values
print(brics)



# Another way to create a DataFrame is by importing a csv file using Pandas. Now, the csv cars.csv is stored and can be imported using pd.read_csv:

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

print("====== Print out cars ======")
# Print out cars
print(cars)



# Indexing DataFrames

# There are several ways to index a Pandas DataFrame. One of the easiest ways to do this is by using square bracket notation.

# In the example below, you can use square brackets to select one column of the cars DataFrame. You can either use a single bracket or a double bracket. The single bracket with output a Pandas Series, while a double bracket will output a Pandas DataFrame.

# Import cars data
# import pandas as pd
cars = pd.read_csv('cars.csv', index_col=False)

print("======")
# Print out model column as Pandas Series
print(cars['model'])

print("======")
# Print out model column as Pandas DataFrame
print(cars[['model']])

print("======")
# Print out DataFrame with model and brand columns
print(cars[['model', 'brand']])



# Square brackets can also be used to access observations (rows) from a DataFrame. For example:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print("====== Print out first 4 observations ======")
# Print out first 4 observations
print(cars[0:4])

print("====== Print out fifth, sixth, and seventh observation ======")
# Print out fifth, sixth, and seventh observation
print(cars[4:6])



# You can also use loc and iloc to perform just about any data selection operation. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = False)

cars.index = ["Morning", "EcoSport", "Everest", "Innova"]
print("====== iloc ======")
# Print out observation for Everest Trend 2.0 AT 4x2
print(cars.iloc[2])

print("====== loc ======")
# Print out observations for Morning and EcoSport
print(cars.loc[['Morning', 'EcoSport']])