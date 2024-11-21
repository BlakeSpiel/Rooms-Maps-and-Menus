import json
import glob
from fileinput import filename

game_state = {
    'player name' : '',
    'location': 'start',
    'inventory': []
}

def pick_up_item(item):
    if item not in game_state['inventory']:
        game_state['inventory'].append(item)
        print(f"You picked up {item}.")
    else:
        print("You already have this item.")




def cemetery():

def small_church():

def entrance_catacombs():

def catacombs():

def bob_lair():

def start():
    if game_state['location'] == start:
        print(f'''Welcome you are in the a cemetery, your friend bob.....''')
        cemetery()
    elif game_state['location'] == 'Small Church':
        small_church()
    elif game_state['location'] == 'Entrance of the Catacombs'
        entrance_catacombs()
    elif game_state['location'] == 'Catacombs'
        catacombs()
    elif game_state['location'] == 'Bob’s Lair'
        bob_lair()

def instructions():
    print('''''')

def exit():
    print('Thanks for playing')


def start_menu():
    print('''
    Welcome to Finding Bob
    Start Menu
    1. Start Game
    2. Instructions
    3. Exit
    ''')
    menu_selection = input('Select an option above(1 or 2): ')
    if menu_selection == 1:
        start()
    if menu_selection == 2:
        instructions()
    if menu_selection == 2:
        exit()

def save_game(filename):
    with open(filename, 'w') as f:
        json.dump(game_state, f)
    print("Game saved.")

def new_game():
    players_name = input('Whats your name?: ')
    save_game(players_name)

    start_menu()

def load_saved_game():
    global game_state
    # Search for all CSV files in the current directory
    game_saves = glob.glob('*.json')
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
            else:
                print("Invalid number, please select a number from the list.")
        except ValueError:
            print("Invalid input, please enter a valid number.")
    else:
        print('No game saves available')

    with open(selected_file, 'r') as f:
         game_state = json.load(f)

    start_menu()


def main_menu():
    print('1. Start New Game')
    print('2. Load Game Save')
    menu_selection = input('Select an option above(1 or 2): ')
    if menu_selection == 1:
        new_game()
    if menu_selection == 2:
        load_saved_game()


main_menu()
