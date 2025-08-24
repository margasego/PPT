from dataclasses import dataclass
from rules import Result

@dataclass
class Scoreboard:
    usuario: int = 0
    computadora: int = 0
    empates: int = 0

    def update(self, r: Result):
        if r == Result.USUARIO:
            self.usuario += 1
        elif r == Result.COMPUTADORA:
            self.computadora += 1
        else:
            self.empates += 1

    def reset(self):
        self.usuario = self.computadora = self.empates = 0
