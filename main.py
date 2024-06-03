from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from routers import equipment, people, assigments

app = FastAPI()

app.include_router(equipment.routers)
app.include_router(people.routers)
app.include_router(assigments.router)


@app.get("/")
def root():
    return "Server is running!!!!!"
