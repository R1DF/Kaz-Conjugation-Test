# Imports
from .base import BaseTense

# Past Simple Tense class
class PastSimpleTense(BaseTense):
    def __init__(self, pronoun_number):
        BaseTense.__init__(self, pronoun_number)  # Inheritance
        self.name = "Past Simple Tense"
        self.description = "The most common past tense. Simply used for actions that have happened in the past without conditions."

        # Getting data
        self.get_suffixes("pastSimple")
        self.get_endings("pastSimple")