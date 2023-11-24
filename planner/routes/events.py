from fastapi import APIRouter, HTTPException, status, Body
from models.events import Events, Location
from datetime import datetime, date
from typing import List

events_router = APIRouter(tags=["Events"])

events = []


@events_router.get("/events")
async def get_all():
    events = await Events.find_all().to_list()
    return events


@events_router.post("/event")
async def register_event() -> dict:
    try:
        events = Events(
            title="machine learning with pytorch",
            description="introduction guide",
            image="robot.png",
            location=Location(
                address=9.38,
                altitude=08747.8388,
                latitude=938.3883,
                longitude=47.46647,
                name="kabuo",
            ),
            tags=["tansorflow", "openai"],
            attending=["tetetetgga"],
            createdBy="hhdhdhdh",
            event_date="sysggsg",
        )
        await events.create()
        return {"msg": "event added successfully"}
    except Exception as e:
        print(e)


@events_router.delete("/events")
def delete_events() -> str:
    return "delete all events"
    pass


@events_router.get("/events/{id}")
def get_event(id):
    item = [item for item in events if item.id == id]
    if not item:
        raise HTTPException(
            detail="event not found", status_code=status.HTTP_404_NOT_FOUND
        )
    return item


@events_router.delete("/events/{id}")
def delete_event() -> str:
    return "delete single event"
    pass
