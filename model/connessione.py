from dataclasses import dataclass
@dataclass
class Connessione:
    state1: str
    state2: str
    peso: int

    def __str__(self):
        return f"({self.state1}, {self.state2}, {self.peso}"
    def __repr__(self):
        return f"({self.state1}, {self.state2}, {self.peso}"
    def __hash__(self):
        return hash((self.state1, self.state2, self.peso))