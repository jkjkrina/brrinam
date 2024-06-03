from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Dict

from services.equipment_manager import equipment_manager

routers = APIRouter()

equipment_manager.add_equipment("test equipment")

class EquipmentDto(BaseModel):
    equipment: str

@routers.post("/equipment/")
def add_equipment(equipment: EquipmentDto):
    return equipment_manager.add_equipment(equipment.equipment)

@routers.get("/equipment/")
def get_equipment():
    return equipment_manager.show_equipment()
