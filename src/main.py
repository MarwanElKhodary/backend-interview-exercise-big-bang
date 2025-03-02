from Game import Game
from utils import clear_screen

def main() -> None:
    """
    Main entry point for the Rock Paper Scissors game.
    
    This function initializes and starts the game by:
    1. Clearing the screen
    2. Creating a new Game instance
    3. Starting the command loop
    """
    clear_screen()
    Game().cmdloop()

if __name__ == "__main__":
    main()