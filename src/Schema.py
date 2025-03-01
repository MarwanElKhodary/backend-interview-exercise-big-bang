from typing import Dict, List
from Rule import Rule

class Schema:
    """
    Schema defines the rules and relationships for a Rock-Paper-Scissors style game.
    
    It validates the fairness of rules (must be odd number) and manages Rule objects.
    
    Attributes:
        rules_config (Dict[str, List[Dict[str, str]]]): Configuration dictionary defining
            all rules and their winning relationships
        rule_names (List[str]): List of all rule names
        rules (Dict[str, Rule]): Dictionary mapping rule names to Rule objects
    """
    
    def __init__(self, rules_config: Dict[str, List[Dict[str, str]]]) -> None:
        """
        Initialize a game schema with rules configuration.
        
        Args:
            rules_config: Dictionary mapping rule names to lists of dictionaries.
                Each inner dictionary maps an opponent rule name to a winning reason.
                Example: {'Rock': [{'Scissors': 'Crushes Scissors'}]}
        
        Raises:
            Exception: If the number of rules is even (unfair game)
        """
        self.rules_config: Dict[str, List[Dict[str, str]]] = rules_config
        self.rule_names: List[str] = list(rules_config.keys())

        if len(self.rule_names) % 2 == 0:
            raise Exception('Number of rules must be odd to ensure a fair game!')
        
        self.rules: Dict[str, Rule] = self._create_rules()
        
    def _create_rules(self) -> Dict[str, Rule]:
        """
        Create Rule objects from the configuration.
        
        Returns:
            Dictionary mapping rule names to Rule objects
        """
        rules: Dict[str, Rule] = {}
        for rule_name, wins_against in self.rules_config.items():
            rules[rule_name] = Rule(rule_name, wins_against)
        return rules