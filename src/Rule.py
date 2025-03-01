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
                    self.wins_against[opponent] = reason