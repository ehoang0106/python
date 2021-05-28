import random

while True:
	user_action = input("keo, bua, bao: ")
	possbile_actions = ["keo", "bua", "bao"]
	computer_action = random.choice(possbile_actions)
	print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

	if user_action == computer_action:
		print(f"Both player selected {user_action}. It's a tie!")
	elif user_action == "bua":
		if(computer_action) == "keo":
			print("Bua an Keo! You WIN")
		else:
			print("Bao an Bua! You LOSE")
	elif user_action == "keo":
		if(computer_action) == "bao":
			print("Keo an Bao! You WIN")
		else:
			print("Bao an Keo! You LOSE")
	elif user_action == "bao":
		if(computer_action) == "bua":
			print("Bao an Bua! You WIN")
		else:
			print("Keo an Bao! You LOSE")

	play_again = input("Do you want to play again? (y/n)")
	if play_again.lower() != "y":
		break