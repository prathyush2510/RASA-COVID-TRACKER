# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import datetime
current_time = datetime.datetime.now()
a = str(int(current_time.day) - 1).zfill(2)
date = str(current_time.month).zfill(2) + "-" + a + "-2020"
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(date)
df = pd.read_csv(url, error_bad_lines=False)
new =  df[['Province_State', 'Country_Region', 'Confirmed','Active','Recovered','Deaths']]
class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_find_and_show_corona_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        state = tracker.get_slot("state")
        for e in entities:
            if e['entity'] == "state":
                state = e['value']
        message = "Please enter valid state"
        for d in new.index:
            if str(new['Province_State'][d]).lower() == str(state).lower():
                message = " State:" + new['Province_State'][d] +"\n" + " Country:" + new['Country_Region'][d] +"\n" + " Active Cases:" + str(new['Active'][d]) +"\n" + " Confirmed Cases:" + str(new['Confirmed'][d]) +"\n" + " Deaths:" + str(new['Deaths'][d])
        dispatcher.utter_message(text=message)
        state = None
        return []
