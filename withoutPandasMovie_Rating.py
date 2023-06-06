import csv
# Without using pandas

# movies.csv -> name of csv file
# movies.csv -> contains data about movies and here we're trying to find the max,min,avg rating

# 1.All movies
# 2.Bollywood movies only
# 3.Hollywood movies only

# as -> alternative name for a file

def rating_finder(actual_data,industry=None):
    ratings = []
    # iterate over the entire list
    for row in actual_data:
        # condition:there should be some rating for a movie(should not be null) and it should belong to
        # and industry passed as argument(ex:bollywood)
        # else it should not belong to any
        if row[3] != 'NULL' and (not industry or row[1] == industry):
            ratings.append(float(row[3]))
    avg_ratings = sum(ratings)/len(ratings)

    return max(ratings), min(ratings), avg_ratings

with open('movies.csv') as m:
    # reader() uses DictReader class to read data from files and returns a _csv.reader

    movies_list = list(csv.reader(m))

    # movies_list -> list of list
    print(movies_list)

    # checking total rows
    # it includes 1 row dedicated for heading
    print(len(movies_list))

    # checking total cols
    print(len(movies_list[0]))

    # contains heading
    columns = movies_list[0]

    # contains actual data
    data = movies_list[1:]

    # max_rat = min_rat = avg_rat = 0.0

    max_rat, min_rat, avg_rat = rating_finder(data)

    print(f'All movies:\nMax Rating={max_rat}\n Min Rating={min_rat}\n Average Rating={avg_rat}')

    max_rat, min_rat, avg_rat = rating_finder(data, 'Bollywood')

    print(f'Bollywood movies:\nMax Rating={max_rat}\n Min Rating={min_rat}\n Average Rating={avg_rat}')

    max_rat, min_rat, avg_rat = rating_finder(data, 'Hollywood')

    print(f'Hollywood movies:\nMax Rating={max_rat}\n Min Rating={min_rat}\n Average Rating={avg_rat}')