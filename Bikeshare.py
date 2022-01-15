import time
import pandas as pd
import numpy as np
import os

# Change directory to yours before running
os.chdir('D:/python_folder/final/')
a = os.getcwd()
print(a)

# Dicts to check for user inputs
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
DAYS = {"Sat": "Saturday", "Sun": "Sunday", "Mon": "Monday", "Tues": "Tuesday", "Wed": "Wednesday", "Thur": "Thursday",
        "Fri": "Friday", "No": 7}
months = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, "no": 7}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input(
            "\nEnter city name you want to show statistics from the list: (chicago, new york city, washington) "
            ": \n ").lower()
        try:
            CITY_DATA[city] is None == 0
            break
        except KeyError:
            print('You entered invalid city name, please choose from the list ')

    # get user input for month (all, january, february, ... , june)

    while True:
        try:
            month = (input("Enter month number (1-6) you want to show statistics \n(or type no for no month "
                           "filtering)\n"))
            if month.lower() == "no":
                month = month.lower()
            else:
                month = int(month)
            months[month] is None == 0
            month = months[month]
            break
        except KeyError:
            print('You entered invalid month, it should range from 1 to 12')
    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            day = input("Enter day name you want to show statistics, eg: Thur, Fri. \n(or type no for no month "
                        "filtering)\n").title()
            DAYS[day] is None == 0
            day = DAYS[day]
            break
        except KeyError:
            print('You entered invalid day, it should be short form like Sun for Sunday')
    print('-' * 40)
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

    dff = pd.read_csv(CITY_DATA[city])
    dff_o = pd.read_csv(CITY_DATA[city])

    dff['Start Time'] = pd.to_datetime(dff['Start Time'])
    dff['End Time'] = pd.to_datetime(dff['End Time'])

    dff['Month'] = dff['Start Time'].dt.month
    dff['day'] = dff['Start Time'].dt.day_name()
    dff['hour'] = dff['Start Time'].dt.hour

    if month != 7:
        month_filt = (dff['Month'] == month)
    else:
        month_filt = (dff['Month'] == dff['Month'])
    if day != 7:
        # 7 is a code refers to no filtering
        day_filt = (dff['day'] == day)
    else:
        day_filt = (dff['day'] == dff['day'])

    dff = dff[month_filt & day_filt]
    # dff = dff[day_filt]
    return dff, dff_o


def time_stats(df):
    # Displays statistics on the most frequent times of travel.
    print('\n')
    print('-' * 40)
    print('Calculating statistics within selected filtered data')
    print('-' * 40)
    print('\n'*2)
    print('-' * 40)
    print('Calculating The Most Frequent Times of Travel...')
    print('-' * 40)
    start_time = time.time()

    # display the most common month
    most_common_month = df['Month'].mode()[0]
    print('\nthe most common month is :...\n{}'.format(most_common_month))
    month_count = df['Month'].value_counts().max()
    print('With count equals :...\n{}'.format(month_count))
    # display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('\nthe most common day of week is...\n{}'.format(most_common_day))
    day_count = df['day'].value_counts().max()
    print('With count equals :...\n{}'.format(day_count))
    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('\nthe most common start hour ...\n{}'.format(most_common_hour))
    hour_count = df['hour'].value_counts().max()
    print('With count equals :...\n{}'.format(hour_count))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...')
    start_time = time.time()
    print('-' * 40)

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('\nthe most commonly used start station...\n{}'.format(most_common_start_station))
    start_station_count = df['Start Station'].value_counts().max()
    print('With count equals :...\n{}'.format(start_station_count))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nthe most commonly used end station...\n{}'.format(most_common_end_station))
    end_station_count = df['End Station'].value_counts().max()
    print('With count equals :...\n{}'.format(end_station_count))

    # display most frequent combination of start station and end station trip
    most_common_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print('\nthe most commonly used trip...\n{}'.format(most_common_trip))
    popular_trip_count = (df['Start Station'] + " to " + df['End Station']).value_counts().max()
    print('With count equals :...\n{}'.format(popular_trip_count))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...')
    print('-' * 40)
    start_time = time.time()

    # display total travel time
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Travel Time'].sum()
    print('\nthe total travel time is ...\n{}'.format(total_travel_time))
    # display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print('\nthe mean travel time is ...\n{}'.format(mean_travel_time))
    # display total trips
    total_trips = df['Travel Time'].count()
    print('\nthe total trips count is ...\n{}'.format(total_trips))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('Calculating User Stats...')
    print('-' * 40)
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\n User types count are ...\n{}'.format(user_types))
    # Washington has no data for gender or birth year
    if city != 'washington':
        # Display counts of gender
        user_gender = df['Gender'].value_counts()
        print('\n User types genders are ...\n{}'.format(user_gender))

        # Display earliest, most recent, and most common year of birth

        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        df_years = df[df['Birth Year'] == earliest_birth_year]
        earliest_birth_count = df_years['Birth Year'].value_counts().min()

        df_years = df[df['Birth Year'] == most_recent_birth_year]
        most_recent_birth_year_count = df_years['Birth Year'].value_counts().min()

        df_years = df[df['Birth Year'] == most_common_birth_year]
        most_common_birth_year_count = df_years['Birth Year'].value_counts().min()

        print('\nEarliest birth year is {}, count: {}\nMost recent birth year is {}, count: {} \nMost common birth year'
              ' is {}, count: {}\n'.format(earliest_birth_year, earliest_birth_count, most_recent_birth_year,
                                           most_recent_birth_year_count, most_common_birth_year,
                                           most_common_birth_year_count))
    else:
        print('\nNo Gender or Birth year data available for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df, dfo = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        looping = input('\nWould you like show 5 raw data examples without filtering? Enter yes or no.\n').lower()
        i, j = 0, 5
        while looping == 'yes':
            print(dfo.iloc[i:j])
            i += 5
            j += 5
            if j >= dfo.shape[0]:
                print('You have reached the end of data')
                break
            looping = input('\nWould you like show 5 raw data examples without filtering? Enter yes or no.\n').lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
