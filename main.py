import random

choices = ["rock", "paper", "scissors"]

print("====================================")
print("      ROCK PAPER SCISSORS GAME")
print("====================================")

while True:
    user_choice = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose      : {user_choice}")
    print(f"Computer chose : {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 Congratulations! You Win!")

    else:
        print("😔 Computer Wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break