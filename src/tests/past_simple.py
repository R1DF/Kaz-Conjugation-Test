# Imports
from .base import BaseTense

# Past Simple Tense class
class PastSimpleTense(BaseTense):
    def __init__(self, pronoun_number, is_negated):
        BaseTense.__init__(self, pronoun_number, is_negated)  # Inheritance
        self.name = "Past Simple Tense"
        self.description = "The most common past tense. Simply used for actions that have happened in the past without conditions."

        # Getting data
        self.get_suffixes("pastSimple")
        self.get_endings("pastSimple")

    def conjugate(self):
        # Verb must be set for every tense
        if self.infinitive is None:
            return

        # Getting vowel determinant
        determinant = {"hard": 0, "soft": 1}[self.detect_last_vowel_type()]

        # Finding correct suffix (only 2 with an easy rule to follow)
        if self.detect_consonant_type(self.infinitive[-2]) == "voiceless":
            suffix = self.suffixes[1][determinant]
        else:
            suffix = self.suffixes[0][determinant]

        # Finding correct ending
        ending = self.endings[self.pronoun_number - 1][determinant]

        self.conjugated = self.infinitive[:-1] + suffix + ending  # The infinitive's last letter is always removed.
        # LOGIC ERROR: Z BECOMES ZTYQ AND NOT ZDYQ. review consonant types and special rules (e.g. ғ becomes q when conjugated) https://kaz-tili.kz/glag3.htm
