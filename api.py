from fastapi import FastAPI
import uvicorn
import epiasParser
import datetime


app = FastAPI()


@app.get("/market/mcp")
def get_mcp():
    try:
        dp = epiasParser.Querys()

        engine = dp.createEngine()

        days = 1
        today = datetime.datetime.today()
        nextday = today + datetime.timedelta(days=days)
        today = today.strftime('%Y-%m-%d')
        nextday = nextday.strftime('%Y-%m-%d')

        df = dp.getDate(nextday, today)

        dp.insertDB(df, engine)

        return {"message": "success"}

    except Exception as e:
        return {"message": f"error: {e}"}
