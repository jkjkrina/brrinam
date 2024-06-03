from typing import List, Dict

from fastapi import FastAPI, HTTPException

from models.assignment_model import Assignment
from models.equipment_model import Equipment
from models.people_model import People

from services.people_manager import people_manager, PeopleManager
from services.equipment_manager import equipment_manager, EquipmentManager


class AssignmentManager:
    def __init__(self, people_manager: PeopleManager, equipment_manager: EquipmentManager):
        self.assignments: Dict[People, List[Equipment]] = {}
        self.people_manager = people_manager
        self.equipment_manager = equipment_manager

    def assign_task(self, equipment_id: int, person_id: int):
        equipment = self.equipment_manager.get_by_id(equipment_id)
        if not equipment:
            raise HTTPException(status_code=404, detail="Немає доступного обладнання для призначення.")

        person = self.people_manager.get_by_id(person_id)
        if not person:
            raise HTTPException(status_code=404, detail="Немає доступних людей для призначення завдань.")
        #
        # equipment.id = self.equipment.id(equipment)
        # person.id = self.people.id(person)
        #
        # if equipment_id
        #     self.assignments.
        # if equipment_index < 0 or equipment_index >= len(self.equipment):
        #     raise HTTPException(status_code=400, detail="Невірний вибір обладнання.")
        # if person_index < 0 or person_index >= len(self.people):
        #     raise HTTPException(status_code=400, detail="Невірний вибір людини.")
        #
        # equipment = self.equipment[equipment_index]
        # person = self.people[person_index]

        if person in self.assignments:
            self.assignments[person].append(equipment)
        else:
            self.assignments[person] = [equipment]

        return f"Обладнання '{equipment}' призначено для {person}."

    def show_assignments(self) -> Dict[People, List[Equipment]]:
        return self.assignments


manager = AssignmentManager(equipment_manager, people_manager)