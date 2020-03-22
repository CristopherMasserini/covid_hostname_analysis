# covid_malware
A project that takes a file of hostnames that have a reference to COVID-19 and attempts to separate the malicious from the valid. The goal here was to get a viable package available as quickly as possible to help mitigate the affect of opportunistic attackers. This is still a work in process and should be used as a base for a business to build off of. Some of the cutoff variables for scoring were picked in a good but relatively arbitrary manner. You can adjust the cutoffs to be more or less stringent based off of your needs.

This project collects the information published by a researcher at: https://1984.sh/covid19-domains-feed.txt

Because this project, written in python, is dependent on the library python-who is (https://github.com/DannyCork/python-whois) to access a DNS, there are some issues that can only be worked out in that library. For instance, the country code TLD for Portugal, .pt, is not recognized in that library as valid. 

The overall project is as follows:
- First, access the information on the website. 
- Next, look at how quickly the hostnames were created with respect to the previous one.
  - The logic here is that hostnames created in very quick succession were more likely to be malicious. This can be seen when you see hostnames like coronavirusprevention, coronavirusfreevaccine, coronaviruswellnesskit, etc. all created very quickly. These hostnames then get a score based off of how quickly they were created.
- Then, the base domains are looked at to see when they were created. If a base domain was created within a month, it would be more likely to be malicious than a base domain created a few years ago. The score gets adjusted to account for the base domain age.
- Finally, two cutoff scores are set. Under the first, is when a hostname is most likely malicious. Between the first and second is when further analysis should be be done, or just take basic precaution. Above the second cutoff is most likely a valid hostname.
