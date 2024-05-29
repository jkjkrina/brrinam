from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Dict

routers = APIRouter()
class EquipmentManager:
    def __init__(self):
        self.equipment = []

    def add_equipment(self, equipment: str):
        self.equipment.append(equipment)
        return f"Обладнання '{equipment}' додано."

    def show_equipment(self) -> List[str]:
        return self.equipment

manager = EquipmentManager()


class Equipment(BaseModel):
    equipment: str

@routers.post("/equipment/")
def add_equipment(equipment: Equipment):
    return manager.add_equipment(equipment.equipment)

@routers.get("/equipment/")
def get_equipment():
    return manager.show_equipment()
