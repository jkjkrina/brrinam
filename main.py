from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

from routers import equipment, people

app = FastAPI()

app.include_router(equipment.routers)
app.include_router(people.routers)


class AssetsManager:
    def init(self):
        self.equipment = []
        self.people = []
        self.assignments = {}
class PeopleManager:
    def __init__(self):
            self.person = []

    def add_person(self, person: str):
            self.people.append(person)
            return f"Людину '{person}' додано."

    def assign_task(self, equipment_index: int, person_index: int):
        if not self.equipment:
            raise HTTPException(status_code=400, detail="Немає доступного обладнання для призначення.")
        if not self.people:
            raise HTTPException(status_code=400, detail="Немає доступних людей для призначення завдань.")

        if equipment_index < 0 or equipment_index >= len(self.equipment):
            raise HTTPException(status_code=400, detail="Невірний вибір обладнання.")
        if person_index < 0 or person_index >= len(self.people):
            raise HTTPException(status_code=400, detail="Невірний вибір людини.")

        equipment = self.equipment[equipment_index]
        person = self.people[person_index]

        if person in self.assignments:
            self.assignments[person].append(equipment)
        else:
            self.assignments[person] = [equipment]

        return f"Обладнання '{equipment}' призначено для {person}."

    def show_assignments(self) -> Dict[str, List[str]]:
        return self.assignments


class People(BaseModel):
    person: str


class Assignment(BaseModel):
    equipment_index: int
    person_index: int

manager = PeopleManager()


# @app.post("/people/")
# def add_person(person: Person):
#     return manager.add_person(person.person)

# @app.post("/assign/")
# def assign_task(assignment: Assignment):
#     return manager.assign_equipment(assignment.equipment_index, assignment.person_index)
#
# @app.get("/assignments/")
# def get_assignments():
#     return "h"

@app.get("/")
def root():
    return "Server is running!!!!!"
