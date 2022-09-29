# Imports
from .base import BaseTense

# Continuous Tense class
class ContinuousTense(BaseTense):
    def __init__(self, pronoun_number):
        BaseTense.__init__(self, pronoun_number)  # Inheritance
        self.name = "Continuous Tense"
        self.description = "Used for either actions to happen in the future or for actions that happen regularly (similar to English present)."

