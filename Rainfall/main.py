#Title: Rainfall
#Author: Dominic Corneliusen
#Date last modified: 3/5/2026

#Start
import statistics
months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
rainfall = []
for month in months:
    is_rainfall_valid = False
    printText = 'How much rainfall was in', month, '?'
    rainfall_in_month = float(input(printText))
    while not is_rainfall_valid:
        if rainfall_in_month < 0:
            is_rainfall_valid = False
            print('Sorry, the rainfall amount was invalid. Please try again.')
        else:
            rainfall.append(rainfall_in_month)
            is_rainfall_valid = True
print('The average rainfall over the year was: ', statistics.mean(rainfall), 'inches')
print('The minimum rainfall was: ', min(rainfall), 'inches')
print('The maximum rainfall was: ', max(rainfall), 'inches')