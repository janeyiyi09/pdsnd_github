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
    city=input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
    while city not in ["chicago", "new york city", "washington"]:
        print("That's not a valid input.")
        city=input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month_options = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("Would you like to see data for January, February, March, April, May, June or all\n").lower()
    while month not in month_options:
        print("That's not a valid input.")
        month = input("Would you like to see data for January, February, March, April, May, June or all?\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
    day = input("Would you like to see data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n").title()
    while day not in day_options:
        print("That's not a valid input.")
        day = input("Would you like to see data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n").title()


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    if month == 'all':
        common_month = int(df['month'].mode()[0])
        print('Most common Month:', months[common_month-1])


    # TO DO: display the most common day of week
    if day == 'All':
        common_day = df['day_of_week'].mode()[0]
        print('Most common Day:', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('Most common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most commonly used Start Station:', start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most commonly used End Station:', end_station)


    # TO DO: display most frequent combination of start station and end station trip
    trip = (df['Start Station']+' to '+df['End Station']).mode()[0]
    print('Most frequent combination of start station and end station trip: from', trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total Trip Duration:', total_travel)


    # TO DO: display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print('Average Trip Duration:', avg_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Breakdown of user types:')
    print(user_types.to_string())


    # TO DO: Display counts of gender
    if city in ['chicago', 'new york city']:
        gender_count = df['Gender'].value_counts()
        print('\nBreakdown of genders:')
        print(gender_count.to_string())


    # TO DO: Display earliest, most recent, and most common year of birth
    if city in ['chicago', 'new york city']:
        print('\nThe earliest, most recent, and most common year of birth:')
        early_birth = int(df['Birth Year'].min())
        print('The earliest Year of Birth:', early_birth)
        recent_birth = int(df['Birth Year'].max())
        print('The most recent Year of Birth:', recent_birth)
        common_birth = int(df['Birth Year'].mode()[0])
        print('The most common Year of Birth:', common_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(city):
    """
    Ask if user would like to see individual trip data.
    Script prompt the user whether they would like want to see the raw data.
    If the user answers 'yes,' then the script should print 5 rows of the data at a time,
    then ask the user if they would like to see 5 more rows of the data.
    The script should continue prompting and printing the next 5 rows at a time until the user chooses 'no,'
    """

    count = 0
    raw_data = pd.read_csv(CITY_DATA[city]).rename(columns = {'Unnamed: 0' : ''})
    while True:
        ans = input('\nWould you like to view individual trip data? Enter Y for yes, N for no.\n').lower()
        while ans not in ['y', 'n']:
            print("That's not a valid input.")
            ans = input('Would you like to view individual data? Enter Y for yes, N for no.\n').lower()
        if ans == 'n':
            break
        else:
            for n in range(count,count + 5):
                print('\n',raw_data.iloc[n].to_string())
            count += 5


def main():
    while True:
        city, month, day = get_filters()
        if month != 'all':
            print('Filtered Month (by user):',month.title())

        if day != 'All':
            print('Filtered Day of Week (by user):', day)

        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in ['yes', 'no']:
            print("That's not a valid input.")
            restart = input('Would you like to restart? Enter yes or no.\n').lower()

        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
