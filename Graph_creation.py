# Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

# Loads the data and creates lists for the graphs
df = pd.read_csv('HostnameData_dates.csv')
dates = df.loc[:, "Hostname Creation Date"]
date_list = list(np.unique(dates))
date_count = [0 for date in date_list]
for i in range(0, len(dates)):
    rec_date = df.iloc[i, 0]
    _ = date_list.index(rec_date)
    num = date_count[_]
    date_count[_] = num + 1
    
# Creates the 7 day averages. If first 6 days, the average just comes from the days before.
# Ex. 4th day would be a 4 day average, 5th day would be a 5 day average, etc.
seven_day_averages = list()
for i in range(0, len(date_count)):

    count = date_count[i]
    ave = 0
    if i == 0:
        ave = count
    elif 0 < i < 7:
        for j in range(1, i + 1):
            count += date_count[i - j]
        ave = count / (i + 1)
    else:
        for j in range(1, 7):
            count += date_count[i - j]
        ave = count / 7

    seven_day_averages.append(ave)

# Changes the date to a better format
date_list_new = [datetime.strptime(date, '%Y-%m-%d') for date in date_list]

# Creates the bar graphs
plt.bar(date_list_new, date_count)
plt.title('COVID Hostname Creation')
plt.xlabel('Day')
plt.ylabel('Hostnames Registered that Day')

# Creates the 7 day average line graph on the bar chart
plt.plot(date_list_new, seven_day_averages, color='r')

plt.show()
