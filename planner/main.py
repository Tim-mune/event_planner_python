from fastapi import FastAPI
from routes.users import user_router
from routes.events import events_router
from db.connect import connect

app = FastAPI()


@app.on_event("startup")
async def start_db():
    db = await connect()
    col = db["users"]


@app.get("/")
def home():
    return {"msg": "hello buddy"}


app.include_router(user_router)
app.include_router(events_router)
