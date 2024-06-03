from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Dict

from models.equipment_model import Equipment

class EquipmentManager:
    def __init__(self):
        self.current_id: int = 1
        self.equipment = []

    def add_equipment(self, equipment_name: str):
        equipment = Equipment(self.current_id, equipment_name)
        self.equipment.append(equipment)
        self.current_id += 1
        return f"Обладнання '{equipment.name}' з ідентифікатором '{equipment.id}' додано."

    def show_equipment(self) -> List[Equipment]:
         return self.equipment

    def get_by_id(self, id: int):
        for item in self.equipment:
            if item.id == id:
                return item

equipment_manager = EquipmentManager()