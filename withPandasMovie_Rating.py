import pandas as pd
# DataFrame -> a 2d,tabular data structure

# Column in DataFrame -> Series

df = pd.read_csv('movies.csv')

# print(df) -> will return a dataframe but will not return completely(presence of '...')
# print(df.to_string()) #-> will return a complete a dataframe

# print(df.to_string())

# head() -> returns specific no of rows from top(default 5)
# print(df.head())
# print(df.head(10))

# tail() -> returns specific no of rows from bottom(default 5)
# print(df.tail())
# print(df.tail(10))

# sample() -> returns random 5 rows(or specified no of rows)
# print(df.sample(5))

# shape -> property that returns a tuple(no_of_rows_in_dataframe,no_of_cols_in_dataframe)
# print(df.shape)

# lists the columns of dataframe
# print(df.columns)

# to get info about unique values in a column
# print(df['industry'].unique())

# to get info about how many rows belongs to each of unique values(how many bollywood
# or how many hollywood)
# print(df['industry'].value_counts())


# Accessing a column:
print(df['imdb_rating'].min(), df['imdb_rating'].max(), df['imdb_rating'].mean())

# Horizontal filtering

# If we need only bollywood
bollywood = df[df['industry'] == 'Bollywood']
print(bollywood['imdb_rating'].min(), bollywood['imdb_rating'].max(), bollywood['imdb_rating'].mean())

# If we need only hollywood
hollywood = df[df['industry'] == 'Hollywood']
print(hollywood['imdb_rating'].min(), hollywood['imdb_rating'].max(), hollywood['imdb_rating'].mean())

# Vertical filtering
# df_new = df[['title', 'industry', 'imdb_rating']]
# print(df_new)

# Retrieving rows through iloc

# printing single row index 1
# print(df.iloc[1])

# printing indexes 1,2,10
# print(df.iloc[[1, 2, 10]])

# printing indexes from 3 to 7
# print(df.iloc[3:7])