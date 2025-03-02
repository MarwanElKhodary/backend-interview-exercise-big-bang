import pytest
from src.Scoreboard import Scoreboard

def test_scoreboard_init():
    """Test Scoreboard initialization"""
    players = ['player1', 'player2', 'computer']
    scoreboard = Scoreboard(players)
    
    assert scoreboard.scores == {'player1': 0, 'player2': 0, 'computer': 0}
    assert scoreboard.ties == 0

def test_add_win():
    """Test adding wins to players"""
    scoreboard = Scoreboard(['player', 'computer'])
    
    scoreboard.add_win('player')
    assert scoreboard.scores['player'] == 1
    assert scoreboard.scores['computer'] == 0
    
    scoreboard.add_win('computer')
    scoreboard.add_win('computer')
    assert scoreboard.scores['player'] == 1
    assert scoreboard.scores['computer'] == 2
    
    scoreboard.add_win('nonexistent')
    assert 'nonexistent' not in scoreboard.scores

def test_add_tie():
    """Test adding ties"""
    scoreboard = Scoreboard(['player', 'computer'])
    
    scoreboard.add_tie()
    assert scoreboard.ties == 1
    
    scoreboard.add_tie()
    scoreboard.add_tie()
    assert scoreboard.ties == 3

def test_reset():
    """Test resetting the scoreboard"""
    scoreboard = Scoreboard(['player', 'computer'])
    
    scoreboard.add_win('player')
    scoreboard.add_win('player')
    scoreboard.add_win('computer')
    scoreboard.add_tie()
    scoreboard.add_tie()
    
    scoreboard.reset()
    assert scoreboard.scores == {'player': 0, 'computer': 0}
    assert scoreboard.ties == 0

def test_display_scores():
    """Test score display formatting"""
    scoreboard = Scoreboard(['player', 'computer'])
    
    scoreboard.add_win('player')
    scoreboard.add_win('player')
    scoreboard.add_win('computer')
    scoreboard.add_tie()
    
    score_display = scoreboard.display_scores()
    assert "Player: 2 pts" in score_display
    assert "Computer: 1 pts" in score_display
    assert "Ties: 1" in score_display
    
    assert str(scoreboard) == score_display