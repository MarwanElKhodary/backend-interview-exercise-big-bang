import cmd
import random
import time
from typing import Dict, List, Optional
from Scoreboard import Scoreboard
from Schema import Schema
from Rule import Rule
from utils import clear_screen

# Define the game schema configuration
schema_config: Dict[str, List[Dict[str, str]]] = {
    'Rock': [
        {'Scissors': 'Crushes Scissors'}, 
        {'Lizard': 'Crushes Lizard'}
    ],
    'Paper': [
        {'Rock': 'Covers Rock'}, 
        {'Spock': 'Disproves Spock'}
    ],
    'Scissors': [
        {'Paper': 'Cuts Paper'}, 
        {'Lizard': 'Decapitates Lizard'}
    ],
    'Lizard': [
        {'Paper': 'Eats Paper'}, 
        {'Spock': 'Poisons Spock'}
    ],
    'Spock': [
        {'Rock': 'Vaporizes Rock'}, 
        {'Scissors': 'Smashes Scissors'}
    ]
}

class Game(cmd.Cmd):
    """
    Command-line interface and game logic for Rock-Paper-Scissors-Lizard-Spock.
    
    This class implements the cmd.Cmd interface to provide a command-line interface
    for playing the game. It manages the game flow, player interactions, and scoring.
    
    Attributes:
        intro (str): Welcome message displayed when the game starts
        prompt (str): Command prompt symbol
        schema (Schema): Game schema defining the rules and choices
        rules (Dict[str, Rule]): Dictionary of Rule objects
        valid_choices (List[str]): List of valid player choices
        scoreboard (Scoreboard): Tracks game scores
    """
    
    intro: str = "Welcome to Rock, Paper, Scissors, Lizard, Spock!\n\nType 'start' to play the game or 'help' to list the commands.\n"
    prompt: str = '>>> '

    def __init__(self, arg: Optional[str] = None) -> None:
        """
        Initialize the game with schema, rules, and scoreboard.
        
        Args:
            arg: Optional argument (not used but required by cmd.Cmd)
        """
        super().__init__()
        
        self.schema: Schema = Schema(schema_config)
        self.rules: Dict[str, Rule] = self.schema.rules
        self.valid_choices: List[str] = self.schema.rule_names
        self.scoreboard: Scoreboard = Scoreboard(['player', 'computer'])
        
#**************************CMD COMMANDS***********************************
    def do_start(self, arg: Optional[str] = None) -> None:
        """
        Start playing the game.
        
        This command begins the game loop where the player can make choices
        against the computer.
        """
        self.play_game()
        
    def do_score(self, arg: Optional[str] = None) -> None:
        """
        Display the current score.
        
        Shows the current scores for all players and the number of ties.
        """
        print(self.scoreboard.display_scores())
    
    def do_rules(self, arg: Optional[str] = None) -> None:
        """
        Display the game rules.
        
        Shows all the rules of the game, including what each choice beats.
        """
        print("Rules:")
        for rule in self.rules.values():
            print(f"- {rule}")
    
    def do_reset(self, arg: Optional[str] = None) -> None:
        """
        Reset the scoreboard.
        
        Resets all scores to zero.
        """
        self.scoreboard.reset()
        print("Scores have been reset.")
    
    def do_quit(self, arg: Optional[str] = None) -> bool:
        """
        Stop playing the game, clear the leaderboard, and exit.
        """
        print('Thanks for playing!')
        return True

#**************************FUNCTIONS**************************************
    def play_game(self) -> None:
        """
        Main game loop handling the gameplay flow.
        
        This method runs the main game loop, getting player choices,
        determining the outcome, and updating the scoreboard.
        """
        clear_screen()

        while True:
            player_choice: str = self._get_player_choice()
        
            if player_choice == 'quit':
                clear_screen()
                print("\nType 'start' to play the game or 'help' to list the commands.\n")
                return
            
            self._play_round(player_choice)
            
    def _play_round(self, player_choice: str) -> None:
        """
        Play a single round of the game.
        
        This method handles all aspects of a single game round:
        - Showing the countdown
        - Getting the computer's choice
        - Displaying the matchup
        - Determining the winner
        - Showing the updated score
        
        Args:
            player_choice: The player's choice
        """
        clear_screen()
        self._show_countdown()

        computer_choice: str = random.choice(self.valid_choices)
        self._display_matchup(player_choice, computer_choice)

        self._determine_winner(player_choice, computer_choice)

        print(f"\n{self.scoreboard.display_scores()}")
        print("\nPress Enter to continue...")
        input()
        clear_screen()
    
    def _determine_winner(self, player_choice: str, computer_choice: str) -> None:
        """
        Determine the winner and update the scoreboard.
        
        This method compares the player's and computer's choices,
        determines the winner, and updates the scoreboard accordingly.
        
        Args:
            player_choice: The player's choice
            computer_choice: The computer's choice
        """
        if player_choice == computer_choice:
            print("\nIt's a tie!")
            self.scoreboard.add_tie()
        elif self.rules[player_choice].beats(computer_choice):
            print(f"\nYou WON! because {player_choice} {self.rules[player_choice].win_reason(computer_choice)}")
            self.scoreboard.add_win('player')
        else:
            print(f"\nComputer WON! because {computer_choice} {self.rules[computer_choice].win_reason(player_choice)}")
            self.scoreboard.add_win('computer')

    def _display_matchup(self, player_choice: str, computer_choice: str) -> None:
        """
        Display the player vs computer matchup.
        
        This method formats and displays the choices made by both
        the player and the computer.
        
        Args:
            player_choice: The player's choice
            computer_choice: The computer's choice
        """
        print(f"{'You':<10} | {'Computer':<10}")
        print("-" * 23)
        print(f"{player_choice:<10} vs {computer_choice:<10}")
    
    def _show_countdown(self) -> None:
        """
        Display the countdown animation.
        
        This method shows a dramatic countdown animation before
        revealing the game outcome, mimicking the real-world ritual
        of "Rock, Paper, Scissors, Shoot!"
        """
        print("Ready???\n")
        time.sleep(0.7)
        print("Rock...")
        time.sleep(0.4)
        print("Paper...")
        time.sleep(0.4)
        print("Scissors...")
        time.sleep(0.4)
        print("SHOOT!\n")
        time.sleep(0.3)
    
    def _get_player_choice(self) -> str:
        """
        Display the choices and get the player's selection.
        
        This method shows the available choices to the player,
        gets their input, and validates it.
        
        Returns:
            The player's choice or 'quit'
        """
        print("\nPick your choice by entering the number:\n")
        for i, choice in enumerate(self.valid_choices, 1):
            print(f"  [{i}] {choice}")
        print("\nOr type 'quit' to exit back to the main page.")
        
        while True:
            player_input: str = input("\nchoice >>> ").strip().lower()
            
            if player_input == 'quit':
                return 'quit'
            
            try:
                choice_index: int = int(player_input) - 1
                if 0 <= choice_index < len(self.valid_choices):
                    return self.valid_choices[choice_index]
                else:
                    clear_screen()
                    print(f"\nInvalid number!")
                    return self._get_player_choice()  # Recursive call to try again
            except ValueError:
                player_choice: str = player_input.capitalize()
                if player_choice in self.valid_choices:
                    return player_choice
                else:
                    clear_screen()
                    print(f"\nInvalid choice!")
                    return self._get_player_choice()  # Recursive call to try again