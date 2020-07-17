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

# Changes the date to a better format
date_list_new = [datetime.strptime(date, '%Y-%m-%d') for date in date_list]

# Creates the bar graphs
plt.bar(date_list_new, date_count)
plt.title('COVID Hostname Creation')
plt.xlabel('Day')
plt.ylabel('Hostnames Registered that Day')
plt.show()
