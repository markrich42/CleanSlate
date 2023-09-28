nba_players = {'Lebron James': 6.8, 'Stephen Curry': 6.2, 'Kevin Durant': 6.10, 'Chris Paul': 6.1}

player_name = input("Enter the name of an NBA player: ")

try:
  player_height = nba_players[player_name]
  print(f"{player_name} is {player_height} feet tall.")
except KeyError:
  print(f"{player_name} is not in the NBA players list.")