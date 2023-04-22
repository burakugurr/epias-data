import pandas as pd
from requests import get
import sqlite3


class Querys:

    def createEngine(self):
        # create engine
        engine = sqlite3.connect('epias.db')
        return engine

    def getQuery(self, endpoint):
        BASE_URL = "https://seffaflik.epias.com.tr/transparency/service/"
        url = BASE_URL + endpoint
        response_data = get(url).json()
        return response_data

    def getDate(self, endDate, startDate):
        endpoint = f"market/day-ahead-mcp?endDate={endDate}&startDate={startDate}"
        response_data = self.getQuery(endpoint)
        df = pd.DataFrame.from_dict(response_data['body']['dayAheadMCPList'])
        df['date'] = pd.to_datetime(df['date'])
        df['hours'] = df.date.dt.hour

        return df

    def insertDB(self, df, engine):
        # insert to DB
        # uzun uzun yazmak yerine df.to_sql() yazabiliriz.
        df.to_sql('epias', con=engine, if_exists='append', index=False)
        """
        INSERT INTO epias (
            price	,priceUsd	,priceEur	,hours

        ) VALUES (
            1	,2	,3	,4
        )


        """
