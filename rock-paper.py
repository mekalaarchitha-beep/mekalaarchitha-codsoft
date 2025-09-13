import random
print("Welcome to Rock-Paper-Scissors!")
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice, try again.")
        continue
        computer = random.choice(choices)
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("\nFinal Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing! Goodbye ")
        break
