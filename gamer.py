
class Player:
    def __init__(self, name, moves, punches, energy=6):
        self.name = name
        self.moves = moves
        self.punches = punches
        self.energy = energy

    def make_move(self):
        return self.moves.pop(0) if self.moves else ""

    def make_punch(self):
        return self.punches.pop(0) if self.punches else ""

    def is_alive(self):
        return self.energy > 0


class Fight:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def execute(self):
        attacker = self.player1
        defender = self.player2

        while attacker.is_alive() and defender.is_alive():
            attacker_move = attacker.make_move()
            attacker_punch = attacker.make_punch()

            defender_move = defender.make_move()
            defender_punch = defender.make_punch()

            if attacker_move + attacker_punch < defender_move + defender_punch:
                defender.energy -= 1
                print(f"{attacker.name} conecta un golpe en {defender.name}")
            elif attacker_move + attacker_punch > defender_move + defender_punch:
                attacker.energy -= 1
                print(f"{defender.name} recibe un golpe de {attacker.name}")
            elif len(attacker_move) + len(attacker_punch) < len(defender_move) + len(defender_punch):
                defender.energy -= 1
                print(f"{attacker.name} conecta un golpe en {defender.name}")
            else:
                attacker.energy -= 1
                print(f"{defender.name} recibe un golpe de {attacker.name}")

            attacker, defender = defender, attacker

        winner = self.player1 if self.player1.is_alive() else self.player2
        print(f"{winner.name} gana la pelea y aun le queda {winner.energy} de energia")


    
