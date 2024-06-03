from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Dict
from dataclasses import dataclass
from models.people_model import People


class PeopleManager:
    def __init__(self):
        self.current_id: int = 1
        self.people = []

    def add_people(self, first_name: str, last_name: str):
        people = People(self.current_id, first_name, last_name)
        self.people.append(people)
        self.current_id += 1
        return f"Користувача '{first_name, last_name}' з ідентифікатором '{people.id}' додано."

    def show_people(self) -> List[str]:
        return self.people

    def get_by_id(self, id: int):
        for item in self.people:
            if item.id == id:
                return item


people_manager = PeopleManager()