import random
import os

#create function clear screen, copy on internet =))
def clear():
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]

#pick 1 card in cards list
def pick_card():
  card = random.choice(cards)
  return card

#calculate score of card
def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return "bj" #bj = blackjack not blow...

    if 1 in cards and sum(cards) > 21:
        cards.remove(1)
        cards.append(11)
    return sum(cards)

#detect who is winner
def detect_winner(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You and computer went over. Draw"
  if user_score == computer_score:
    return "Draw"
  elif computer_score == "bj":
    return "Computer has BlackJack. You lose"
  elif user_score == "bj":
    return "You has BlackJack. You win"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Computer went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

#main function
def play_game():
    user_card = []
    computer_card = []
    #pick 2 card is card list
    for i in range(2):
        user_card.append(pick_card())
        computer_card.append(pick_card())

    #calculate score
    user_score = cal_score(user_card)
    computer_score = cal_score(computer_card)

    print(f"Your cards is {user_card}, total score = {user_score}")
    print(f"Computer cards is [x, {computer_card[1]}]")

    # withdraw card
    stop_with_draw = False

    while not stop_with_draw:
        with_draw = input("Do you want to withdraw card? Type 'y' or 'n' \n").lower()
        if with_draw == "y":
            user_card.append(pick_card())
            user_score = cal_score(user_card)
            print(f"Your cards is: {user_card}, total score = {user_score}")
        elif with_draw == "n":
            stop_with_draw = True
            while computer_score < 21:
                computer_card.append(pick_card())
                computer_score = cal_score(computer_card)
                print(f"Computer cards is {computer_card}, total score = {computer_score}")
            print(detect_winner(user_score,computer_score))
play_game()

# cont = input("Do you want to play again? Type 'y' or 'n': ")
# while cont == "y":
#   clear()
#   play_game()


