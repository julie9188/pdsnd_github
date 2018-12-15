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
    while True:
        try:
            city = str(input('Please Type Name of the City.').lower())
            df = pd.read_csv(CITY_DATA[city])
            break
        except Error:
            print('\n Please Select from Chicago, New York, Washington.')


    # TO DO: get user input for month (all, january, february, ... , june)
    month_list= ['all', 'january', 'february', 'march','april','may','june']
    while True:
      try:
          month = input(('\n Please filter the month by name or type all.').lower())
          month_index= month_list.index(month)
          break
      except:
          print('\n Please select from Janurary to June or type all.')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',                  'Sunday']
    while True:
        try:
          day = input('\nSelect the Day of Week or Type "all".').capitalize()
          day_index = day_list.index(day)
          break
        except:
            print('\nPlease Select from monday, tuesday,...,sunday or Select all.')


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
        df=pd.read_csv(CITY_DATA[city])
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['month']=df['Start Time'].dt.month
        df['day_of_week']=df['Start Time'].dt.weekday_name

        # filter by month if applicable
        if month != "all":
            # use tge indexx of month list ro get the corresponding int
            months = ['januray','februray','march','april','may','june']
            month = months.index(month)+1
            # filter by month to creat the new dataframe
            df = df[df['month']== month]
         #filter by day of week if applicable
        if day != 'all':
            df = df[df['day_of_week'] == day]
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('most common month is' ,most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Month is', most_common_day_of_week)

    # TO DO: display the most common start hour
    df ['hour'] = df ['Start Time'].dt.hour
    most_common_start_hour= df['hour'].mode()[0]
    print('Most Common Start Hour is', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station is', most_used_start_station)

    # TO DO: display most commonly used end station
    most_used_end_station= df['End Station'].mode()[0]
    print('Most Commomly Used End Statio is', most_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination= df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most Frequent Combination of Start ad End Station is', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time is ',df['Trip Duration'].sum()/3600/24,'days.')

    # TO DO: display mean travel time
    print('Mean Travel Time is ',df['Trip Duration'].mean()/60,'minutes.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types is ', user_types)

    # TO DO: Display counts of gender
    if city !='washington':
        df.dropna(axis = 0)
        gender_counts = df['Gender'].value_counts()
        print('Counts of Gender is ', gender_counts)
    else:
        print('Washington has No Gender Info')


    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        df.dropna(axis = 0)
        earliest = int(df['Birth Year'].min())
        print('Earliest Year of Birth is ', earliest)
        most_recent = int(df['Birth Year'].max())
        print('Most Recent Year of Brith is ', most_recent)
        most_common = int(df['Birth Year'].mode()[0])
        print('Most Common Year of Birth is ', most_common)
    else:
        print('Washington has No Birth Year Information')

    answer_list = ['yes','no']
    i = 0
    j = 5
    while True:
        try:
            answer=input(('Would you like to see 5 rows of data? Yes/No ').lower())
            answer_index = answer_list.index(answer)
            if answer == 'yes':
                print(df[i:j])
                i += 5
                j += 5
                continue
            else:
                break
        except:
            print('Please enter Yes/No')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
