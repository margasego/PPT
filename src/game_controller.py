from rules import Choice, Result, random_choice, evaluate
from scoreboard import Scoreboard

class GameController:
    def __init__(self):
        self.score = Scoreboard()

    def banner(self):
        print("="*46)
        print("        JUEGO: PIEDRA - PAPEL - TIJERA")
        print("="*46)
        print("Comandos: piedra | papel | tijera | reglas | reiniciar | salir")
        print()

    def show_rules(self):
        print("REGLAS: Piedra gana a Tijera, Tijera gana a Papel, Papel gana a Piedra.")

    def run(self):
        self.banner()
        while True:
            cmd = input("Tu elección: ").strip().lower()
            if cmd == "salir":
                print("¡Gracias por jugar!"); break
            if cmd == "reglas":
                self.show_rules(); continue
            if cmd == "reiniciar":
                self.score.reset(); print("Marcador reiniciado."); continue
            if cmd not in [c.value for c in Choice]:
                print("Entrada no válida."); continue

            user = Choice(cmd)
            pc = random_choice()
            r = evaluate(user, pc)

            self.score.update(r)

            print(f"Computadora eligió: {pc.value}")
            if r == Result.EMPATE:
                print("Resultado: EMPATE")
            elif r == Result.USUARIO:
                print("Resultado: ¡GANASTE!")
            else:
                print("Resultado: PERDISTE")

            print(f"Marcador -> Tú: {self.score.usuario} | PC: {self.score.computadora} | Empates: {self.score.empates}")
            print("-"*46)
