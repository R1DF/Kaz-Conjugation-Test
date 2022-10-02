# Imports
from .base import BaseTense
import random

# Past Obvious Tense class
class PastObviousTense(BaseTense):
    def __init__(self, pronoun_number, is_negated):
        BaseTense.__init__(self, pronoun_number, is_negated)  # Inheritance
        self.name = "Past Obvious Tense"
        self.description = "Used for past actions that the speaker is definitely user happened or " \
                           "was a witness to. Can be used with another past tense to signify an " \
                           "action which happened before the other."

        # Getting data
        self.get_suffixes("pastObvious")
        self.get_endings("pastObvious")

    def set_infinitive(self):  # Override because negation is different
        self.infinitive = random.choice(self.verbs_list)
        self.conjugated = None

    def conjugate_affirmative(self):
        # First initializations and suffixes
        stem = self.infinitive[:-1]
        last_letter = stem[-1].upper()
        determinant = {"hard": 0, "soft": 1}[
            self.detect_last_vowel_type()]  # powerful line that gives an index on applied occasions

        # Suffixes depend on whether the last letter is a voiceless consonant
        if self.detect_consonant_type(last_letter) == "voiceless":
            suffix = self.suffixes[1][determinant]
        else:
            suffix = self.suffixes[0][determinant]

        # Ending is easy
        ending = self.endings["affirmative"][self.pronoun_number - 1][determinant]
        self.conjugated = stem + suffix + ending

    def conjugate_negative(self):
        self.conjugated = [] # List is being used for 2 variants
        # First variant. Joq/emes is used and the infinitive isn't negated.
        stem = self.infinitive[:-1]
        last_letter = stem[-1].upper()
        determinant = {"hard": 0, "soft": 1}[
            self.detect_last_vowel_type()]  # powerful line that gives an index on applied occasions

        # Suffixes are obtained exactly the same
        if self.detect_consonant_type(last_letter) == "voiceless":
            suffix = self.suffixes[1][determinant]
        else:
            suffix = self.suffixes[0][determinant]

        # Getting the ending and its part
        negative_part = random.choice(["емес", "жоқ"])
        determinant_negative = {"hard": 0, "soft": 1}[self.detect_vowel_type(negative_part[-2])]
        ending = self.endings["negative"][self.pronoun_number - 1][determinant_negative]
        self.conjugated.append(f"{stem}{suffix} {negative_part}{ending}")

        # Second variant which is way easier
        self.negate(False)
        stem = self.infinitive[:-1]
        last_letter = stem[-1].upper()

        # Suffixes are still obtained the same
        if self.detect_consonant_type(last_letter) == "voiceless":
            suffix = self.suffixes[1][determinant]
        else:
            suffix = self.suffixes[0][determinant]

        ending = self.endings["affirmative"][self.pronoun_number - 1][determinant]  # Affirmative is still used here as an exception
        self.conjugated.append(f"{stem}{suffix}{ending}")


    def conjugate(self):
        # Verb must be set for every tense
        if self.infinitive is None:
            return

        # Affirmative form only has 1 variant. Negative has 2, so we need to split them.
        if not self.is_negated:
            self.conjugate_affirmative()
        else:
            self.conjugate_negative()

    def print_sentence(self):  # Override again
        if not self.is_negated:
            print(self.pronoun.capitalize() + " " + self.conjugated + ".")
        else:
            for conjugated_index in range(len(self.conjugated)):
                print(f"Variant {conjugated_index+1}: {self.pronoun.capitalize()} {self.conjugated[conjugated_index]}.")

