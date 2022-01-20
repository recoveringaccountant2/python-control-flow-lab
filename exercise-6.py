# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year (Jan - Dec) as three characters: ')
day = int(input('Enter the day of the month: '))
season = ''

if month in ('Jan', 'Feb'):
    season = 'Winter'
elif month in ('Apr', 'May'):
    season = 'Spring'
elif month in ('Jul', 'Aug'):
    season = 'Summer'
elif month in ('Apr', 'May'):
    season = 'Fall'
elif month in ('Oct', 'Nov'):
    season = 'Spring'
elif month == 'Mar':
    if day <= 20:
        season = 'Winter'
    else:
        season = 'Spring'
elif month == 'Jun':
    if day <= 21:
        season = 'Spring'
    else:
        season = 'Summer'
elif month == 'Sep':
    if day <= 22:
        season = 'Summer'
    else:
        season = 'Fall'
elif month == 'Dec':
    if day <= 21:
        season = 'Fall'
    else:
        season = 'Winter'
else:
    print('Problem with inputs')

print(f'{month} {day} is in {season}')