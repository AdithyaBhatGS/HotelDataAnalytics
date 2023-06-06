import pandas as pd 
import matplotlib.pyplot
# read_csv returns a dataframe
df_booking = pd.read_csv(r'hotelDataProject\dataset\fact_bookings.csv')

# trying to print first 5 records completely using to_string()
# print(df_booking.head(5).to_string())

# to check no of rows and cols in dataset
# print(df_booking.shape)

# trying to print the name of the cols
# print(tuple(df_booking.columns))

# trying to print unique room category
# print(df_booking.room_category.unique())

# trying to check unique booking platforms from which customers come
# print(df_booking.booking_platform.unique())

# trying to check from which platform we're getting more customers
# print(df_booking['booking_platform'].value_counts())

# percentile of share of different platform in user bookings
# df_booking1 = (df_booking['booking_platform'].value_counts()/df_booking.shape[0])*100

# print(df_booking['booking_platform'].value_counts().plot(kind='barh'))
# matplotlib.pyplot.show()

# print(df_booking.describe().to_string())

df_date = pd.read_csv(r'hotelDataProject\dataset\dim_date.csv')
df_hotels = pd.read_csv(r'hotelDataProject\dataset\dim_hotels.csv')

# print(df_date.sample(5).to_string())
# print(df_hotels.head().to_string())
# print(df_hotels.property_name.value_counts())
# print(df_hotels.city.value_counts().sort_values())
# matplotlib.pyplot.show()

df_agg_bookings = pd.read_csv(r'hotelDataProject\dataset\fact_aggregated_bookings.csv')

print(df_agg_bookings.head().to_string())
print('--------------------------------')
# print(df_agg_bookings.property_id.value_counts())
df_updated = df_agg_bookings[(df_agg_bookings['successful_bookings'] > df_agg_bookings['capacity'])]
print(df_updated['check_in_date'])



