import json
from gamer import  Player, Fight

def read_moves(json_data):
    player1_movs = json_data['player1']['movimientos']
    player1_golpes = json_data['player1']['golpes']
    player2_movs = json_data['player2']['movimientos']
    player2_golpes = json_data['player2']['golpes']
    return (player1_movs, player1_golpes, player2_movs, player2_golpes)

def read_json(file_name = 'moves_gamer.json'):
    with open(file_name, 'r') as f:
      json_data = json.load(f)
      return json_data
    

if __name__ == "__main__":
    file_js = 'move_gamer.json'
    json_data = read_json(file_js)
    player1_moves, player1_punches, player2_moves, player2_punches = read_moves(json_data)

    player1 = Player("Tony", player1_moves, player1_punches)
    player2 = Player("Arnaldor", player2_moves, player2_punches)

    fight = Fight(player1, player2)
    fight.execute()
