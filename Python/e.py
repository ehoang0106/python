import random
possible_choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choice)
user_choice = input("rock, paper or scissors: ").lower()

print(f"You chose {user_choice}")		
print(f"Computer chose {computer_choice}")

if computer_choice == user_choice:
	print(f"Both chose {user_choice}. It's a tie!")
elif user_choice == "rock":
	if computer_choice == "scissors":
		print("Rock smash scissors. YouW IN!")
	else:
		print("Paper wrap rock. You LOSE!")
elif user_choice == "paper":
	if computer_choice == "rock":
		print("Paper wrap rock. You WIN!")
	else:
		print("Scissors cut paper. You LOSE!")
elif user_choice == "scissors":
	if computer_choice == "paper":
		print("Scissors cut paper. You WIN!")
	else:
		print("Rock smash scissors. You LOSE!")
