from fastapi import FastAPI
from routes.users import user_router
from routes.events import events_router

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "hello buddy"}


app.include_router(user_router)
app.include_router(events_router)
