from typing import Dict, List

class Scoreboard:
    """
    Tracks scores for all players in the game and the number of ties.
    
    The scoreboard maintains a dictionary of scores for each player and
    provides methods to update and display the scores.
    
    Attributes:
        scores (Dict[str, int]): Dictionary mapping player identifiers to their scores
        ties (int): Number of tie games
    """
    
    def __init__(self, players: List[str]) -> None:
        """
        Initialize a scoreboard for tracking game scores.
        
        Args:
            players: List of player identifiers
        """
        self.scores: Dict[str, int] = {player: 0 for player in players}
        self.ties: int = 0
    
    def add_win(self, player: str) -> None:
        """
        Add a win to a player's score.
        
        Args:
            player: The identifier of the player who won
        """
        if player in self.scores:
            self.scores[player] += 1
    
    def add_tie(self) -> None:
        """
        Add a tie to the scoreboard.
        """
        self.ties += 1
    
    def reset(self) -> None:
        """
        Reset all scores to zero.
        """
        for player in self.scores:
            self.scores[player] = 0
        self.ties = 0
    
    def display_scores(self) -> str:
        """
        Display the current scores in a formatted string.
        
        Returns:
            Formatted string showing all scores
        """
        score_strings: List[str] = [f"{player.capitalize()}: {score} pts" for player, score in self.scores.items()]
        score_strings.append(f"Ties: {self.ties}")
        return " | ".join(score_strings)
    
    def __str__(self) -> str:
        """
        Get a string representation of the scoreboard.
        
        Returns:
            String representation of the scoreboard
        """
        return self.display_scores()