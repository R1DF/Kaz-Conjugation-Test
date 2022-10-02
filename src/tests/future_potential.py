# Imports
from .base import BaseTense

# Future Potential Tense class
class FuturePotentialTense(BaseTense):
    def __init__(self, pronoun_number, is_negated):
        BaseTense.__init__(self, pronoun_number, is_negated)  # Inheritance
        self.name = "Future Potential Tense"
        self.description = "Used for future actions that might or might not happen.."

        # Getting data
        self.get_suffixes("futurePotential")
        self.get_endings("futurePotential")

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
        if self.is_negated:
            suffix = self.suffixes[3]
        else:
            if not self.is_vowel(last_letter):
                suffix = self.suffixes[determinant]
            else:
                suffix = self.suffixes[2]

        # Endings also depend on negation.
        ending = self.endings["affirmative" if not self.is_negated else "negative"][self.pronoun_number - 1][determinant]
        self.conjugated = stem + suffix + ending

