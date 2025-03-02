import pytest
from src.Game import Game, schema_config

def test_game_init():
    """Test Game initialization"""
    game = Game()
    
    assert len(game.valid_choices) == 5
    assert set(game.valid_choices) == {'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'}
    assert len(game.rules) == 5
    
    assert game.scoreboard.scores == {'player': 0, 'computer': 0}
    assert game.scoreboard.ties == 0

def test_schema_setup():
    """Test that the schema is set up with the correct rules"""
    game = Game()
    
    rock_rule = game.rules['Rock']
    assert rock_rule.beats('Scissors')
    assert rock_rule.beats('Lizard')
    assert not rock_rule.beats('Paper')
    assert not rock_rule.beats('Spock')
    
    paper_rule = game.rules['Paper']
    assert paper_rule.beats('Rock')
    assert paper_rule.beats('Spock')
    assert not paper_rule.beats('Scissors')
    assert not paper_rule.beats('Lizard')
    
    assert rock_rule.win_reason('Scissors') == 'Crushes Scissors'
    assert paper_rule.win_reason('Rock') == 'Covers Rock'

def test_scoreboard_integration():
    """Test that the game correctly tracks scores"""
    game = Game()
    
    assert game.scoreboard.scores['player'] == 0
    assert game.scoreboard.scores['computer'] == 0
    assert game.scoreboard.ties == 0
    
    game.scoreboard.add_win('player')
    assert game.scoreboard.scores['player'] == 1
    
    game.scoreboard.add_win('computer')
    game.scoreboard.add_win('computer')
    assert game.scoreboard.scores['computer'] == 2
    
    game.scoreboard.add_tie()
    assert game.scoreboard.ties == 1
    
    game.scoreboard.reset()
    assert game.scoreboard.scores['player'] == 0
    assert game.scoreboard.scores['computer'] == 0
    assert game.scoreboard.ties == 0

def test_determine_winner_logic():
    """Test the core winner determination logic"""
    game = Game()
    
    game._determine_winner('Rock', 'Rock')
    assert game.scoreboard.ties == 1
    assert game.scoreboard.scores['player'] == 0
    assert game.scoreboard.scores['computer'] == 0
    
    game.scoreboard.reset()
    
    game._determine_winner('Rock', 'Scissors')
    assert game.scoreboard.scores['player'] == 1
    assert game.scoreboard.scores['computer'] == 0
    assert game.scoreboard.ties == 0
    
    game.scoreboard.reset()
    
    game._determine_winner('Scissors', 'Rock')
    assert game.scoreboard.scores['player'] == 0
    assert game.scoreboard.scores['computer'] == 1
    assert game.scoreboard.ties == 0

def test_rule_win_reasons():
    """Test that all win reasons match what's in the schema config"""
    game = Game()
    
    for winner, win_entries in schema_config.items():
        for win_entry in win_entries:
            for loser, reason in win_entry.items():
                assert game.rules[winner].beats(loser)
                assert game.rules[winner].win_reason(loser) == reason