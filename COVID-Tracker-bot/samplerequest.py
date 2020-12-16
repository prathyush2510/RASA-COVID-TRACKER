from typing import Any, Text, Dict, List
#import requests,csv
import pandas as pd
import datetime
current_time = datetime.datetime.now()
a = str(int(current_time.day) - 1).zfill(2)
date = str(current_time.month).zfill(2) + "-" + a + "-2020"
print(date)
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(date)
df = pd.read_csv(url, error_bad_lines=False)
#response = requests.get("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/07-03-2020.csv")
#new = pd.DataFrame(zip(df.Province_State, df.Country_Region, df.Confirmed,df.Active,df.Recovered,df.Deaths) )
new =  df[['Province_State', 'Country_Region', 'Confirmed','Active','Recovered','Deaths']]
print(new['Province_State'])