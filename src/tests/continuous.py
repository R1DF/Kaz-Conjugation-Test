# Imports
from .base import BaseTense

# Continuous Tense class
class ContinuousTense(BaseTense):
    def __init__(self, pronoun_number, is_negated):
        BaseTense.__init__(self, pronoun_number, is_negated)  # Inheritance
        self.name = "Continuous Tense"
        self.description = "Used for either actions to happen in the future or for actions that happen regularly (similar to English present)."

        # Getting data
        self.get_suffixes("continuous")
        self.get_endings("continuous")

    def conjugate(self):
        # Verb must be set for every tense
        if self.infinitive is None:
            return

        # Finding correct suffix
        penultimate_letter_type = self.detect_letter_type(-2)
        determinant = {"hard": 0, "soft": 1}[self.detect_last_vowel_type()]  # powerful line that gives an index on applied occasions
        match penultimate_letter_type:
            case "consonant":
                suffix_index = determinant
            case _:
                suffix_index = 2
        suffix = self.suffixes[suffix_index]

        # Finding correct ending
        match penultimate_letter_type:
            case "hard":
                ending = self.endings[self.pronoun_number - 1][0]
            case "soft":
                ending = self.endings[self.pronoun_number - 1][1]
            case _:
                ending = self.endings[self.pronoun_number - 1][determinant]

        self.conjugated = self.infinitive[:-1] + suffix + ending  # The infinitive's last letter is always removed.

