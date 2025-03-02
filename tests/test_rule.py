import pytest
from src.Rule import Rule

def test_rule_init():
    """Test Rule initialization with and without win conditions"""
    rule = Rule("Rock")
    assert rule.name == "Rock"
    assert rule.wins_against == {}
    
    rule = Rule("Rock", [{"Scissors": "Crushes Scissors"}, {"Lizard": "Crushes Lizard"}])
    assert rule.name == "Rock"
    assert rule.wins_against == {"Scissors": "Crushes Scissors", "Lizard": "Crushes Lizard"}

def test_add_win_condition():
    """Test adding win conditions to a rule"""
    rule = Rule("Paper")
    rule.add_win_condition("Rock", "Covers Rock")
    assert rule.wins_against == {"Rock": "Covers Rock"}
    
    rule.add_win_condition("Rock", "Wraps Rock")
    assert rule.wins_against == {"Rock": "Wraps Rock"}

def test_beats():
    """Test the beats method"""
    rule = Rule("Spock", [{"Rock": "Vaporizes Rock"}, {"Scissors": "Smashes Scissors"}])
    
    assert rule.beats("Rock") is True
    assert rule.beats("Scissors") is True
    assert rule.beats("Paper") is False
    assert rule.beats("Lizard") is False
    assert rule.beats("Spock") is False

def test_win_reason():
    """Test getting win reasons"""
    rule = Rule("Lizard", [{"Paper": "Eats Paper"}, {"Spock": "Poisons Spock"}])
    
    assert rule.win_reason("Paper") == "Eats Paper"
    assert rule.win_reason("Spock") == "Poisons Spock"
    assert rule.win_reason("Rock") == ""

def test_str_representation():
    """Test string representation of a rule"""
    rule = Rule("Scissors", [{"Paper": "Cuts Paper"}, {"Lizard": "Decapitates Lizard"}])
    str_rep = str(rule)
    
    assert "Rule: Scissors" in str_rep
    assert "Wins against:" in str_rep
    assert "Paper (Cuts Paper)" in str_rep
    assert "Lizard (Decapitates Lizard)" in str_rep