from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Dict

routers = APIRouter()

class PeopleManager:
    def __init__(self):
        self.people = []

    def add_people(self, people: str):
        self.equipment.append(people)
        return f"Людину '{people}' додано."

    def show_people(self) -> List[str]:
        return self.people

manager = PeopleManager()


class People(BaseModel):
    equipment: str


@routers.post("/people/")
def add_people(people: People):
    return manager.add_people(people.equipment)

@routers.get("/people/")
def add_people():
    return manager.show_people()


