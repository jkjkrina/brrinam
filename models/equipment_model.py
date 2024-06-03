from fastapi import FastAPI
from dataclasses import dataclass


@dataclass
class Equipment:
    id: int
    name: str

    def __hash__(self):
        return hash(self.id)
