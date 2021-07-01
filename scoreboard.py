def show_scoreboard(player_deck, computer_deck):
  print(f"\tYour cards: {player_deck}. current score: {sum(player_deck)}")
  print(f"\tComputer's first card: {computer_deck[0]}")

def show_final_scoreboard(player_deck, computer_deck):
  print(f"\tYour final hand: {player_deck}, final score: {sum(player_deck)}")
  print(f"\tComputer's final hand: {computer_deck}, final score: {sum(computer_deck)}")
