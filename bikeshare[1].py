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
    cities = ['chicago','new york city','washington']
    city = input("Please, Would you like to see data for Chicago, New York City, or Washington?").lower()
    while city not in cities:
        print("Invalid city. Please select Chicago, New York City, or Washington. ")
        city= input("Try again: ").lower()
              
    # TO DO: get user input for month (all, january, february, ... , june)
    months= ["january","february","march","april","may","june", "all"]
       
    while True:
        month = input("Introduce a month or all: ").lower()
        if month in months:
            break
        else:
            print("Invalid choice")
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days= ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday","all"]
    while True:
        day = input("Which day of the week (Monday, Tuesday, Wednesday, Sunday,Thursday, Friday or all)? ").lower()
        if day in days:
            break
        else:
            print("Invalid choice. Please select (Monday, Tuesday, Wednesday, Sunday,Thursday, Friday or all)")
    
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"]= df["Start Time"].dt.day_name()
    df["hour"]= df["Start Time"].dt.hour
    
    if month != "all":
        months= ["january","february","march","april","may","june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]
     
    if day != "all":
        df = df[df["day_of_week"].str.lower() == day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print(f" The most common month: {most_common_month}")
    
    # TO DO: display the most common day of week
    most_common_week = df["day_of_week"].mode()[0]
    print(f" The most common week: {most_common_week}")
     
    # TO DO: display the most common start hour
    most_common_hour = df["hour"].mode()[0]
    print(f" The most common hour: {most_common_hour}")  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    most_start_station = df["Start Station"].mode()[0]
    print(f"The most common start station: {most_start_station}")

    # TO DO: display most commonly used end station
    most_end_station = df["End Station"].mode()[0]
    print(f"The most common end station: {most_end_station}")
          
    # TO DO: display most frequent combination of start station and end station trip
    most_common_combination = df.groupby(["Start Station", "End Station"]).size().idxmax()
    print(f"The most common combination of start and end station: {most_common_combination}")
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f"The total travel time: {total_travel_time} seconds")
                   
    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print(f"The average travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(f"Count of user types:\n{user_type_counts}\n")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders_counts = df['Gender'].value_counts()
        print(f"Count of genders:\n{genders_counts}\n")
    else:
        print("Gender data not available.\n") 

    # TO DO: Display earliest, most recent, and most common year of birth Birth Year 
    if 'Birth Year' in df.columns:
        earliest_birth = int(df["Birth Year"].min())
        most_recent_birth = int(df["Birth Year"].max())
        most_common_birth = int(df["Birth Year"].mode()[0])
        
        print(f"Earliest year of birth: {earliest_birth}")
        print(f"The most recent year of birth: {most_recent_birth}")
        print(f"The most common year of birth: {most_common_birth}")      
    else:
        print("Birth Year data not available.\n")
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data upon request by the user."""
    print('\nDisplaying Raw Data...\n')
    start_row = 0
    while True:
        display = input('Would you like to see 5 lines of raw data? Enter yes or no: ').lower()
        if display != 'yes':
            break
        print(df.iloc[start_row:start_row + 5])
        start_row += 5
        if start_row >= len(df):
            print('No more data to display.')
            break
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()