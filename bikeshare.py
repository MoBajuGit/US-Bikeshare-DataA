import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """     
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please Choose the City Name chicago or new york or washington: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "Please enter Chicago, New York City, or Washington: ").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please Enter a month name: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        month = input(
        "Please Enter invalid Month name: ").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please Enter a day name: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input(
        "Please Enter invalid Day name is: ").lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month,:]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day,:]

        return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nThe Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {}".format(
        str(df['month'].mode().values[0]))
    )

    # TO DO: display the most common day of week
    print("The most common day of the week: {}".format(
    str(df['day_of_week'].mode().values[0]))
    )

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode().values[0]))
    )

    print("\nPercentage %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nThe Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used end station
    print("The most common start station is: {} ".format(
        df['Start Station'].mode().values[0])
    )

    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    print("The most common start and end station combo is: {}".format(
        df['routes'].mode().values[0])
    )

    print("\nPnercentage took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

    #TO DO: display total travel time
    print("The total travel time is: {}".format(
            str(df['duration'].sum()))
    )

    # TO DO: display mean travel time
    print("The mean travel time is: {}".format(
        str(df['duration'].mean()))
    )

    print("\nPnercentage took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nUser Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Please see the counts of various user types here:")
    print(df['User Type'].value_counts())

    if city != 'washington':
    # TO DO: Display counts of gender
        print("Please see the counts of gender here:")
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birth year is: {}".format(
            str(int(df['Birth Year'].min())))
            )
        print("The latest birth year is: {}".format(
            str(int(df['Birth Year'].max())))
            )
        print("The most common birth year is: {}".format(
            str(int(df['Birth Year'].mode().values[0])))
            )

    print("\nPnercentage took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Display raw data.
    """

    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
       while True:
            print(df.iloc[start_loc:end_loc])
            start_loc += 5
            end_loc += 5

            end_display = input("Would like to to continue?: ").lower()
            if end_display == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()