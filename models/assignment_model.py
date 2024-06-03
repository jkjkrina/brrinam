from dataclasses import dataclass

from models.equipment_model import Equipment
from models.people_model import People


@dataclass
class Assignment:
    person: People
    equipment: Equipment
