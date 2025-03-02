import pytest
from src.Schema import Schema

# Test configuration for schema
test_schema_config = {
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

# Invalid schema (even number of choices)
invalid_schema_config = {
    'Rock': [{'Scissors': 'Crushes Scissors'}],
    'Paper': [{'Rock': 'Covers Rock'}],
    'Scissors': [{'Paper': 'Cuts Paper'}],
    'Lizard': [{'Paper': 'Eats Paper'}]
}

def test_schema_init():
    """Test Schema initialization with valid configuration"""
    schema = Schema(test_schema_config)
    assert schema.rules_config == test_schema_config
    assert set(schema.rule_names) == {'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'}
    
def test_schema_init_invalid():
    """Test Schema raises exception with even number of rules"""
    with pytest.raises(Exception) as excinfo:
        Schema(invalid_schema_config)
    assert "Number of rules must be odd" in str(excinfo.value)

def test_create_rules():
    """Test rules creation from configuration"""
    schema = Schema(test_schema_config)
    rules = schema._create_rules()
    
    assert len(rules) == 5
    assert all(rule_name in rules for rule_name in test_schema_config.keys())
    
    rock_rule = rules['Rock']
    assert rock_rule.name == 'Rock'
    assert rock_rule.beats('Scissors')
    assert rock_rule.beats('Lizard')
    assert not rock_rule.beats('Paper')