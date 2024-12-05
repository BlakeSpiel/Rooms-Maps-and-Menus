import glob
import pickle

""" Game State """
player_name = ""
game_state = {
    'location': "cemetery",
    'inventory': [],
    'small church door locked': 'Locked',
    'mausoleum door locked': 'Locked',
    'bobs lair locked': 'Locked'
  # Or what every that game state varables are
}

""" Save Game """
def save_game(filename):
    try:
        with open(f"{filename}.pkl", 'wb') as file:
            pickle.dump(game_state, file)
        print("Game state saved successfully using pickle.")
    except Exception as e:
        print(f"Error saving game state: {e}")

""" Load Game Save """
def load_saved_game():
    global game_state
    selected_file = None
    # Search for all CSV files in the current directory
    game_saves = glob.glob('*.pkl')
    if game_saves:
        file_names = game_saves
        for idx, file in enumerate(file_names, start=1):
            print(f"{idx}. {file}")
        # Ask the user to select a file by number
        try:
            user_choice = int(input("Enter the number of the game save you want to select: "))

            # Check if the user's choice is within the valid range
            if 1 <= user_choice <= len(file_names):
                selected_file = file_names[user_choice - 1]
                print(f"You selected: {selected_file}")
                try:
                    with open(selected_file, 'rb') as file:
                        game_state = pickle.load(file)
                    print("Game state loaded successfully.")
                except Exception as e:
                    print(f"Error loading game state: {e}")
            else:
                print("Invalid number, please select a number from the list.")
        except ValueError:
            print("Invalid input, please enter a valid number.")
    else:
        print('No game saves available')
        main_menu()

def main_menu():
    global player_name
    print('1. Start New Game')
    print('2. Load Game Save')
    menu_selection = int(input('Select an option above(1 or 2): '))
    if menu_selection == 1:
        player_name = input('What your name?: ')
        save_game(player_name)
    if menu_selection == 2:
        load_saved_game()

main_menu()
