import csv

from datetime import datetime

import matplotlib.pylab as plt

filename = 'data//sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
     
    #Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
    #Plot the high and low temperatures
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.9)
    ax.plot(dates, lows, c='blue', alpha=0.9)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')

    #Format plot
    plt.title("Daily high and low temperatures- 2018", fontsize=12)
    plt.xlabel("Dates\n2018-2019", fontsize=8)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=8)
    plt.tick_params(axis="both", which='major', labelsize=8)

    plt.show()





