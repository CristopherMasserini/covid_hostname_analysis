# ----Imports----
import matplotlib.pyplot as plt
from matplotlib import dates
import pandas as pd
import numpy as np
from datetime import datetime

# ----Data manipulation----
# Loads the data and creates lists for the graphs
df = pd.read_csv('HostnameData_dates.csv')


dates_rec = df.loc[:, "Hostname Creation Date"]
date_list = list(np.unique(dates_rec))
date_count = [0 for date in date_list]
for i in range(0, len(dates_rec)):
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

# ----Plots----
# Changes the date to a better format
date_list_new = [datetime.strptime(date, '%Y-%m-%d') for date in date_list]

# Creates the bar graphs
plt.bar(date_list_new, date_count, label='Daily Hostnames Created')

# Creates the 7 day average line graph on the bar chart
ave_line, = plt.plot(date_list_new, seven_day_averages, color='r', label='7 Day Average')

# Better formatting for the graph
ax = plt.gca()
xaxis = dates.date2num(date_list_new)
hfmt = dates.DateFormatter('%m\n%d')
ax.xaxis.set_major_formatter(hfmt)

plt.title('COVID Hostname Creation')
plt.xlabel('Month\nDay')
plt.ylabel('Hostnames Registered that Day')
plt.legend(handles=[ave_line])

plt.show()
