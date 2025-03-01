from typing import Dict, List, Optional

class Rule: 
    """
    Represents a rule in Rock-Paper-Scissors style games.
    
    Each rule defines what other rules it can beat and the reason for winning
    (e.g., "Rock crushes Scissors").
    
    Attributes:
        name (str): The name of the rule (e.g., "Rock", "Paper", etc.)
        wins_against (Dict[str, str]): Dictionary mapping opponent rule names to
            winning explanations
    """
    
    def __init__(self, name: str, wins_against: Optional[List[Dict[str, str]]] = None) -> None:
        """
        Initialize a rule with its name and what it wins against.
        
        Args:
            name: The name of the rule (e.g., "Rock", "Paper")
            wins_against: Optional list of dictionaries where each dictionary maps 
                an opponent rule name to a winning reason
                (e.g., [{"Scissors": "Crushes Scissors"}])
        """
        self.name: str = name
        self.wins_against: Dict[str, str] = {}

        if wins_against:
            for win_entry in wins_against:
                for opponent, reason in win_entry.items():
                    self.add_win_condition(opponent, reason)
                    
    def add_win_condition(self, opponent: str, reason: str) -> None:
        """
        Add or update a win condition against an opponent.
        
        Args:
            opponent: The name of the opponent rule
            reason: The explanation of why this rule beats the opponent
        """
        self.wins_against[opponent] = reason
    
    def beats(self, opponent: str) -> bool:
        """
        Check if this rule beats the given opponent.
        
        Args:
            opponent: The name of the opponent rule
            
        Returns:
            True if this rule beats the opponent, False otherwise
        """
        return opponent in self.wins_against
    
    def win_reason(self, opponent: str) -> str:
        """
        Get the reason this rule beats the opponent.
        
        Args:
            opponent: The name of the opponent rule
            
        Returns:
            The winning reason if this rule beats the opponent, empty string otherwise
        """
        if self.beats(opponent):
            return self.wins_against[opponent]
        return ""
    
    def __str__(self) -> str:
        """
        Get a string representation of the rule.
        
        Returns:
            A string showing the rule name and what it wins against with reasons
        """
        wins_str = ", ".join([f"{opponent} ({reason})" for opponent, reason in self.wins_against.items()])
        return f'Rule: {self.name} | Wins against: {wins_str}'