from cmath import nan
import pandas as pd
import numpy as np

# Create a DataFrame
## From a Python Dictionary
df = pd.DataFrame({'name': ['Bob', 'Lisa', 'Mike', 'Fatima', 'Zahra', 'Ali', 'Maryam', 'Maryam'],
'Age': [23, 23, 25, 19, 42, '54', 107, 107],
'Sex': ['M', 'F', 'M', 'F', 'F', 'M', 'F', 'F'],
'Job': ['Designer', 'Marketing Manager', 'Product Manager', 'Software Engineer', 'Data Scientist', 'Machine Learning Engineer', np.NaN, np.NaN],
'Hobbies': ['Waterskiing', 'Skydiving', 'Rock Climbing', 'Skateboarding', 'Baking', 'Improv Acting', 'Trolling', 'Trolling']})

# Preview a Dataframe
## Head: view first 5 rows
df.head()
df.head(3)

## Tail: view final 5 rows
df.tail()
df.tail(3)

## Show column names 
df.columns

## Shape: Get rows and columns of a dataframe
df.shape

len(df) ## Rows
len(df.columns) ## Columns

## Show data types for each column in a dataframe
df.dtypes

df['Sex'].dtype

## Subsetting columns in a dataframe. We use the square brackets like we do with lists
df['name']
df[['name', 'Hobbies']]

## Subset rows with iloc
df.iloc[3, :] # Gets 3rd row and all columns

df.iloc[[3,4], :] # Gets rows 3 and 4 and all columns

df.iloc[:, 2] # Gets all rows and only 2nd column

df.iloc[:, [3,4]] # Gets all rows and 3rd and 4th columns

df.iloc[[0,1], [3,4]] # Gets 0th and 1st rows and 3rd and 4th columns

## Get unique values for a column
df['Age']

df['Age'].unique()

# Descriptive Stats for a Dataframe
df.describe()

df.value_counts()

df['Age'].value_counts()
df['Sex'].value_counts()

# Cast column types
df.dtypes
df['Age'] = df['Age'].astype(int)
df.dtypes

# Data Wrangling
df_copy = df.copy()

## Filter rows
df_copy[df_copy.Job == 'Data Scientist']

df_copy[(df_copy.Sex == 'F') & (df_copy.Age > 25)]

df_copy[(df_copy.Sex == 'F') | (df_copy.Age < 25)]

df_copy[df_copy.Job.isin(['Designer', 'Machine Learning Engineer'])]
df_copy[~df_copy.Hobbies.isin(['Trolling', 'Skydiving'])]

## Mutate columns
df_copy['new_age'] = df_copy['Age'] - 2

df_copy['log_age'] = df_copy['Age'].apply(np.log)

df_copy['full_hobbies'] = df_copy['Hobbies'].apply(lambda x: x + ' & Scuba Diving')

df_copy['Sex'] = df_copy['Sex'].apply(lambda x: x.lower())

## Sort values
df_copy.sort_values(by = ['Age'], ascending = [True])
df_copy.sort_values(by = ['Age'], ascending = [False])

df_copy.sort_values(by = ['Hobbies'], ascending = [True])
df_copy.sort_values(by = ['Sex', 'Age'], ascending = [True, False])

## Rename Columns

df_copy.columns = ['Name', 'Age', 'Sex', 'Job', 'Hobbies', 'new_age', 'log_age', 'full_hobbies']
df_copy

df_copy = df_copy.rename(columns = {'new_age': 'Younger_Age', 'log_age': 'Log_Age'})
df_copy

# Grouping and Aggregating
df_copy.groupby(['Sex'], as_index=False).agg({'Age': 'mean'})

df_copy.groupby(['Sex'], as_index=False).agg({'Age': ['mean', 'min', 'max']})

## Add a new column for Salary and Ethnic Name
df_copy['Salary'] = [72, 65, 67, 71, 70, 89, 23, 23]
df_copy['Ethnic_Name'] = ["n", "n", "n", "n", "y", "y", "y", "y"]

df_copy.groupby(['Sex'], as_index=False).agg({'Salary': ['mean', 'median']})
df_copy.groupby(['Sex', 'Ethnic_Name'], as_index=False).agg({'Salary': ['mean', 'median']})

## Making your own aggregation functions - These run much slower for large dataframes
def exp_mean(x):
    y = np.exp(np.array(x))
    return np.mean(y)

exp_mean([1,2,3,4])

df_copy.groupby(['Sex'], as_index=False).agg({'Salary': exp_mean})

# Conditional Logic on Dataframe Columns
## We can perform if else logic on columns
df_copy['eligible_for_membership'] = np.where(df_copy.Age >= 25, True, False)
df_copy

## More than 2 conditions
df_copy['Adventurous'] = np.select([df_copy.Hobbies == 'Waterskiing', df_copy.Hobbies == 'Skydiving', df_copy.Hobbies == 'Rock Climbing', df_copy.Hobbies == 'Skateboarding', df_copy.Hobbies == 'Baking']
, ['very_adventurous', 'extremely_adventurous', 'adventurous', 'adventurous', 'not adventurous']
, default = 'mildly_adventurous')

df_copy

# Check Null values
df['Job'].isna()

# Drop all rows with a Null value in at least one column
df.dropna()

# Replace Null value with a value
df['Job'].fillna('Tik Tok Star')

# Restrict dataframe to Null rows
df[pd.isnull(df.Job)]

# Check how many duplicate values there are in a column
df['Age'].duplicated()

# Remove all duplicate rows in a dataframe
df.drop_duplicates()

# Multiple Dataframes

## Union Dataframes/ Stack them on top of each other
df2 = pd.DataFrame({'name': ['James', 'Frankie'],
'Age': [47, 48],
'Sex': ['M', 'F'],
'Job': ['Accountant', 'Chef'],
'Hobbies': ['Travelling', 'Kickboxing']})

df3 = pd.concat([df, df2], ignore_index=True)

## Add columns to a dataframe 
df_extra_cols = pd.DataFrame({'Country': ['USA', 'Japan', 'UK', 'UK', 'UK', 'Tanzania', 'Narnia', 'Narnia', 'Australia', 'Netherlands']})

df4 = pd.concat([df3, df_extra_cols], axis = 1)

## Joining Dataframes
### One common key
df_a = pd.DataFrame({'Country': ['USA', 'Japan', 'UK', 'Tanzania', 'Australia', 'Netherlands'],
'National_Sport': ['Baseball', 'Sumo', 'Football', 'Football', 'Netball', 'Cycling']})

df_4a = pd.merge(df4, df_a, on = ['Country'], how = 'left')

### Multiple Keys 
df_b = pd.DataFrame({'Country': ['USA', 'USA', 'Japan', 'Japan', 'UK', 'UK'],
'Sex': ['M', 'F', 'M', 'F', 'M', 'F'],
'Sexist_National_Sport': ['Baseball', 'Cheerleading', 'Sumo', 'Ballet', 'Football', 'Gymnastics']})

df_4b = pd.merge(df4, df_b, on = ['Country', 'Sex'], how = 'left')

# Importing and Exporting Dataframes
## Reading From CSV
diamonds = pd.read_csv("./W2_Intro_Python/data/diamonds.csv")
diamonds.head()

## Writing to CSV
diamonds['Junaid_verdict'] = np.where(diamonds.cut == "Ideal", "Me Likey!", "Meh")

diamonds.to_csv("./W2_Intro_Python/data/diamonds_edited.csv", index = False)
