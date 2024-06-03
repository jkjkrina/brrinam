from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Dict
# from services.equipment_manager import manager
from services.people_manager import people_manager

routers = APIRouter()

people_manager.add_people("Alice", "Bob")

class People(BaseModel):
    first_name: str
    last_name: str


@routers.post("/people/")
def add_people(person: People):
    return people_manager.add_people(person.first_name, person.last_name)

@routers.get("/people/")
def add_people():
    return people_manager.show_people()


