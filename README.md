# COVID hostname malware detection project


## Overview
A project that takes a file of hostnames that have a reference to COVID-19 and attempts to separate the malicious from the valid. The goal here was to get a viable package available as quickly as possible to help mitigate the affect of opportunistic attackers. This is still a work in process and should be used as a base for a business to build off of. Some of the cutoff variables for scoring were picked in a good but relatively arbitrary manner. You can adjust the cutoffs to be more or less stringent based off of your needs.


## Data and libraries used
This project collects the information published by a researcher at: https://1984.sh/covid19-domains-feed.txt

Because this project, written in python, is dependent on the library python-whois (https://github.com/DannyCork/python-whois) to access a DNS, there are some issues that can only be worked out in that library. For instance, the country code TLD for Portugal, .pt, is not recognized in that library as valid. 


## Details
The overall project is as follows:
- First, access the information on the website. 
- Next, look at how quickly the hostnames were created with respect to the previous one.
  - The logic here is that hostnames created in very quick succession were more likely to be malicious. This can be seen when you see hostnames like coronavirusprevention, coronavirusfreevaccine, coronaviruswellnesskit, etc. all created very quickly (well inside one second). These hostnames then get a score based off of how quickly they were created.
- Then, the base domains are looked at to see when they were created. If a base domain was created within a month, it would be more likely to be malicious than a base domain created a few years ago. The score gets adjusted to account for the base domain age.
- Finally, the IP Addresses are put into the data frame. This is done so that the IPs can be analyzed and also given a score (coming soon). This score would look at which IP Addresses come up a large number of times, as registering multiple base domains to one IP Address is a known phishing technique. 
- This all comes together into a final score out of 100, with the closest to 100 being the most likely to be a malicious hostname

#### Example
As an example for the age of the base domain, a couple of hostnames are shown below

```
good_link = 'covid19.medschool.duke.edu'
good_link2 = 'coronavirus.duke.edu'
possible_bad_link = 'www.isurvivedcoronavirusshop.com'

good_link_creation_date = whois.query(good_link).creation_date
good_link2_creation_date = whois.query(good_link2).creation_date
possible_bad_link_creation_date = whois.query(possible_bad_link).creation_date
```

If you look print out these creation dates, you see the ones for Duke are 1986-06-02 00:00:00, compared to the date time given in the files, which are: 2020-3-16 17:46:29.296049 for good_link and 2020-3-21 13:54:32.454261 for good_link2. 

Whereas the creation date for possible_bad_link is 2020-03-13 05:03:41 compared to 2020-3-15 21:04:09.095935 on the file, which is inside one year. 

The assumption here is that the older the base domain name, the more likely it is to be valid.

We also look at the IP adress registered to each hostname. The assumption here is the more hostnames registered to one IP, the higher the likelihood of those hostnames being malicious

## Scoring Details
Each hostname gets a few different scores and an ultimate final score. For the time between creation, age of the base domain, and number of occurances of the IP address, each hostname is given a score between with 1 being the more risky and the higher the score being less risky. In the ultimate final score, all these previous scores are added together and subtracted from 100.

Scoring is done in this way so that the final score is in line with industry standards of the larger score being the riskiest.

#### Example
If a hostname was created within a second of the previous one (score of 1), had been created inside a year (score of 1), and the IP address was seen more than 3 times (score of 1), the final score qould be: 100 - 1 - 1 - 1 = 97 which is highly risky.

If a hostname was created after 4 seconds of the previous one (score of 5), had been created 3 years from today (score of 10), and the IP address was seen 1 time (score of 10), the final score qould be: 100 - 5 - 10 - 10 = 75 which is a moderate to low risk score.
