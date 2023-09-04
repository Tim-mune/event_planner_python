from fastapi import APIRouter, HTTPException, status, Body
from models.events import Events
from typing import List

events_router = APIRouter(tags=["Events"])

events = []


@events_router.get("/events")
def get_all() -> list:
    return events


@events_router.post("/event")
def register_event(event: Events = Body(...)) -> dict:
    events.append(event)

    return {"msg": "event added successfully"}


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
