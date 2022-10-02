# Imports
from .base import BaseTense
import random

# Future Motivative Tense class
class FutureMotivativeTense(BaseTense):
    def __init__(self, pronoun_number, is_negated):
        BaseTense.__init__(self, pronoun_number, is_negated)  # Inheritance
        self.name = "Future Motivative Tense"
        self.description = "Used for future actions that the subject is planning to do."

        # Getting data
        self.get_suffixes("futureMotivative")
        self.get_endings("futureMotivative")

    def conjugate(self):
        # Verb must be set for every tense
        if self.infinitive is None:
            return

        # First initializations and suffixes
        stem = self.infinitive[:-1]
        last_letter = stem[-1].upper()
        determinant = {"hard": 0, "soft": 1}[
            self.detect_last_vowel_type()]  # powerful line that gives an index on applied occasions
        negation_suffixes = self.conjugation_data["negationSuffixes"]  # Suffix rules are identical to negation rules
        if last_letter in negation_suffixes["M"] or self.is_vowel(last_letter):
            suffix = self.suffixes[2][determinant]
        elif last_letter in negation_suffixes["B"]:
            suffix = self.suffixes[0][determinant]
        else:
            suffix = self.suffixes[1][determinant]

        # Finding correct ending
        match self.detect_letter_type(-2):
            case "hard":
                ending = self.endings[self.pronoun_number - 1][0]
            case "soft":
                ending = self.endings[self.pronoun_number - 1][1]
            case _:
                ending = self.endings[self.pronoun_number - 1][determinant]

        # Checking whether there is negation or not, because negation is so similar to here I can do it without changing everything up.
        if not self.is_negated:
            self.conjugated = self.infinitive[:-1] + suffix + ending  # The infinitive's last letter is always removed.
        else:
            ending = self.endings[self.pronoun_number - 1][1]  # Ending must always be soft for emes
            self.conjugated = self.infinitive[:-1] + suffix + " емес" + ending

    def set_infinitive(self):
        self.infinitive = random.choice(self.verbs_list) # Override because no negation
        self.conjugated = None