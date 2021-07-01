import art
import random
import replit
import scoreboard

def fill_deck(current_deck, n_cards):
  cards_drawn = random.sample(cards, k=n_cards)
  current_deck += cards_drawn

  score = sum(current_deck)
    
  for card_position in range(len(current_deck)):
      if score > 21:
          if current_deck[card_position] == 11:
              current_deck[card_position] = 1
              score -= 10

  return current_deck

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
  keep_playing = input("Do you want to play a game of blackjack? Type 'y' for yes and 'n' for no: ")
  replit.clear()
  if keep_playing != 'y':
    break
  
  print(art.logo)

  # First 2 cards for the player
  player_cards = fill_deck([], 2) # Passing an empty list, i.e. the empty deck

  # First 2 cards for the dealer
  dealer_cards = fill_deck([], 2) # The same as player_cards, but for the dealer
  
  scoreboard.show_scoreboard(player_cards, dealer_cards)

  player_went_over = False # Boolean to check if player did lose the game
  
  new_card = True
  while new_card:
    player_hits = input("Type 'y' to get another card, type 'n' to pass: ")
    if player_hits == 'y':
      player_cards = fill_deck(player_cards, 1)
      scoreboard.show_scoreboard(player_cards, dealer_cards)
    else:
      new_card = False

    # Checking if player went over
    if sum(player_cards) > 21:
      new_card = False
      player_went_over = True
  
  if not player_went_over:
    while sum(dealer_cards) < 17:
      dealer_cards = fill_deck(dealer_cards, 1)
    
    scoreboard.show_final_scoreboard(player_cards, dealer_cards)

    if sum(dealer_cards) > 21:
      print("Opponent went over. You win")
    elif sum(player_cards) > sum(dealer_cards):
      print("You win")
    elif sum(player_cards) < sum(dealer_cards):
      print("You lose")
    else:
      print("It's a Draw")
  else: # In this case the player went over
    scoreboard.show_final_scoreboard(player_cards, dealer_cards)
    print("You went over. You lost")

  print() # Blank line at the end of the game
