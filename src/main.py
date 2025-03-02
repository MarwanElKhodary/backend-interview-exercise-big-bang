from Game import Game

def main() -> None:
    """
    Main entry point for the Rock Paper Scissors game.
    
    This function initializes and starts the game by:
    1. Creating a new Game instance
    2. Starting the command loop
    """
    Game().cmdloop()

if __name__ == "__main__":
    main()