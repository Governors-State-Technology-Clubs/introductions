# Sample data: A list of player dictionaries with their data
players = [
    {"first_name": "Thomas", "last_name": "Daily", "age": 20, "team": "Jaguars", "batting_average": 0.290},
    {"first_name": "Nathan", "last_name": "Rodriguez", "age": 24, "team": "Jaguars", "batting_average": 0.260},
    {"first_name": "Jacob", "last_name": "Abrams", "age": 22, "team": "Jaguars", "batting_average": 0.250},
    {"first_name": "Brett", "last_name": "Porter", "age": 36, "team": "Jaguars", "batting_average": 0.333},
    {"first_name": "Harsha", "last_name": "Dalta", "age": 22, "team": "Jaguars", "batting_average": 0.230},
    {"first_name": "Alex", "last_name": "Liu", "age": 50, "team": "Jaguars", "batting_average": 0.210},
    {"first_name": "Andrew", "last_name": "Krol", "age": 30, "team": "Jaguars", "batting_average": 0.222},
    {"first_name": "Lisette", "last_name": "Casas", "age": 20, "team": "Jaguars", "batting_average": 0.234},
    {"first_name": "Natalia", "last_name": "Chowiniec", "age": 21, "team": "Jaguars", "batting_average": 0.202},
    {"first_name": "Joe", "last_name": "Udani", "age": 20, "team": "Jaguars", "batting_average": 0.246},
    {"first_name": "Ahmad", "last_name": "IDK", "age": 21, "team": "Jaguars", "batting_average": 0.200},
]

def find_players_by_last_name_contains(name_part):
    # Find players whose last name contains the given part (case-insensitive)
    return [player for player in players if name_part.lower() in player["last_name"].lower()]

def display_player_data(player):
    # Ask the user to choose the type of player data to display
    print("\nWhat information would you like to see?")
    print("1. Age")
    print("2. Team")
    print("3. Batting Average")

    choice = input("Enter a number (1-3): ")

    if choice == "1":
        print(f"Age: {player['age']}")
    elif choice == "2":
        print(f"Team: {player['team']}")
    elif choice == "3":
        print(f"Batting Average: {player['batting_average']}")
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

def main():
    while True:
        # Ask the user for part of the last name
        name_part = input("Enter part of the player's last name (or type 'exit' to quit): ")

        if name_part.lower() == 'exit':
            print("Exiting the program.")
            break

        # Find matching players
        matching_players = find_players_by_last_name_contains(name_part)

        if not matching_players:
            print(f"No players found with last names containing '{name_part}'.")
            continue

        # Display matching players
        print("\nMatching players:")
        for idx, player in enumerate(matching_players, 1):
            print(f"{idx}. {player['first_name']} {player['last_name']}")

        # Ask the user to select a player
        try:
            player_choice = int(input("\nEnter the number of the player you want to select or 0 to exit: "))
            if player_choice == 0:
                print("Exiting the program.")
                break  # Exit the loop
            selected_player = matching_players[player_choice - 1]  # Select the player based on user input
            
            while True:  # Start a loop to show more data for the selected player
                display_player_data(selected_player)  # Show the player data
                
                more_data = input("\nDo you want to see more data for this player? (y/n): ").lower()
                if more_data != 'y':
                    break  # Exit the loop if the user doesn't want more data

        except (ValueError, IndexError):
            print("Invalid selection. Please select a valid player number.")

        # Ask if the user wants to continue selecting players
        continue_choice = input("\nDo you want to select another player's last name? (y/n): ").lower()
        if continue_choice != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
