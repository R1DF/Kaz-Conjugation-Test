# Imports
from .base import BaseTense

# Past Continuous Tense class
class PastContinuousTense(BaseTense):
    def __init__(self, pronoun_number, is_negated):
        BaseTense.__init__(self, pronoun_number, is_negated)  # Inheritance
        self.name = "Past Continuous Tense"
        self.description = "Used for past actions that have happened regularly or repeat."

        # Getting data
        self.get_suffixes("pastContinuous")
        self.get_endings("pastContinuous")

    def conjugate(self):
        # Verb must be set for every tense
        if self.infinitive is None:
            return

        # First initializations and suffixes
        stem = self.infinitive[:-1]
        last_letter = stem[-1].upper()
        determinant = {"hard": 0, "soft": 1}[
            self.detect_last_vowel_type()]  # powerful line that gives an index on applied occasions

        # Suffixes don't depend on negation but on whether the last letter is a vowel
        if not self.is_vowel(last_letter):
            suffix = self.suffixes[0][determinant]
        else:
            suffix = self.suffixes[1][determinant]

        # Endings are straightforward.
        ending = self.endings[self.pronoun_number - 1][determinant]
        self.conjugated = stem + suffix + ending

