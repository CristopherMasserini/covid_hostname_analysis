import requests
from datetime import datetime
import pandas as pd

link = 'https://1984.sh/covid19-domains-feed.txt'
f = requests.get(link)
link_text = f.text.split('\n')

date_of_record = list()  # The date and time of the hostname creation using Epoch time
hostnames = list()  # The hostname
start_index = link_text.index("date,time,hostname")
for record in link_text[start_index + 1:]:
    try:
        # Splits the record into date, time, and hostname
        record_list = record.split(',')
        record_datetime_str = record_list[0] + " " + record_list[1]  # Concatenates the date and time
        hostname = record_list[2]  # The host name
        record_datetime = datetime.strptime(record_datetime_str, '%Y-%m-%d %H:%M:%S.%f')  # Converts to datetime
        if record_datetime_str != "2020-03-14 15:11:20.684411":
            date_of_record.append(datetime.fromtimestamp(date).strftime('%Y-%m-%d')) # Puts the creation time into a list
            hostnames.append(hostname)  # Puts the hostname into a list
    except IndexError:  # Got to the last record in the list
        pass

pd.options.display.float_format = '{:10f}'.format
data = {"Hostname Creation Date": date_of_record, "Hostname": hostnames}
df = pd.DataFrame(data)
df = df.sort_values(by=["Hostname Creation Date"])
df.index = range(len(df))  # Resets the indexing after the the sorting

df.to_csv(r'HostnameData_dates.csv', index=False)

