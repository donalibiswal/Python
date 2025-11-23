def rock_paper_scissors():
    print("Welcome to 'Rock, Paper, Scissors'!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose. Try again!")

if __name__ == "__main__":
    print("Choose a game to play:")
    print("1. Guess the Number")
    print("2. Rock, Paper, Scissors")

    while True:
        choice = input("Enter 1 or 2 (or 'quit' to exit): ")
        if choice == "1":
            guess_the_number()
        elif choice == "2":
            rock_paper_scissors()
        elif choice.lower() == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 'quit'.")
