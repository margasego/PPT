from enum import Enum
import random

class Choice(str, Enum):
    PIEDRA = "piedra"
    PAPEL = "papel"
    TIJERA = "tijera"

class Result(str, Enum):
    USUARIO = "usuario"
    COMPUTADORA = "computadora"
    EMPATE = "empate"

BEATS = {
    Choice.PIEDRA: Choice.TIJERA,
    Choice.TIJERA: Choice.PAPEL,
    Choice.PAPEL: Choice.PIEDRA,
}

def random_choice() -> Choice:
    return random.choice(list(Choice))

def evaluate(user: Choice, pc: Choice) -> Result:
    if user == pc:
        return Result.EMPATE
    if BEATS[user] == pc:
        return Result.USUARIO
    return Result.COMPUTADORA
