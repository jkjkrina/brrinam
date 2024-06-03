from fastapi import APIRouter
from pydantic import BaseModel
from services.assignment_manager import manager

router = APIRouter()



class Assignments(BaseModel):
    equipment_id: int
    people_id: int


@router.post("/assign")
async def set_assignments(assignment: Assignments):
    manager.assign_task(assignment.equipment_id, assignment.people_id)
    return assignment

@router.get("/assign")
async def get_assignments():
    assigments = manager.show_assignments()

    dtos = []
    for person in assigments.values():
        # dto = {
        #     person.last_name,
        #     person.first_name,
        #     assigments[person]
        # }
        dtos.append(person)

    return dtos

















