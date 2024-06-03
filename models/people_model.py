from dataclasses import dataclass

@dataclass
class People:
    id: int
    first_name: str
    last_name: str

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
