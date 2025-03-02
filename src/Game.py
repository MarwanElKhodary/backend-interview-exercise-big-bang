import cmd
from typing import Dict, List, Optional
from Scoreboard import Scoreboard
from Schema import Schema
from Rule import Rule

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