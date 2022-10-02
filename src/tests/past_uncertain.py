# Imports
from .base import BaseTense

# Past Uncertain Tense class
class PastUncertainTense(BaseTense):
    def __init__(self, pronoun_number, is_negated):
        BaseTense.__init__(self, pronoun_number, is_negated)  # Inheritance
        self.name = "Past Uncertain Tense"
        self.description = "Used for past actions that the speaker is unsure happened. Can be used with another past tense to signify an action which happened before the other."

        # Getting data
        self.get_suffixes("pastUncertain")
        self.get_endings("pastUncertain")

    def conjugate(self):
        # Verb must be set for every tense
        if self.infinitive is None:
            return

        # First initializations and suffixes
        stem = self.infinitive[:-1]
        last_letter = stem[-1].upper()
        determinant = {"hard": 0, "soft": 1}[
            self.detect_last_vowel_type()]  # powerful line that gives an index on applied occasions

        # Suffixes depend on negation!
        if not self.is_vowel(last_letter):
            suffix = self.suffixes[determinant]
        else:
            suffix = self.suffixes[2]

        # Endings as a one-liner.
        ending = self.endings[self.pronoun_number - 1][determinant]
        self.conjugated = stem + suffix + ending

