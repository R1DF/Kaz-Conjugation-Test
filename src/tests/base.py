"""
Base class for a tense of the Kazakh language.
"""
# Imports
import random
from data_getter import tenses_file_data as conjugation_data
from data_getter import verbs_list

# Base for every Tense class
class BaseTense:
    def __init__(self, pronoun_number):
        # Metadata
        self.name = None
        self.description = None

        # Grammatical structure
        self.infinitive = None  # Must be set separately
        self.conjugated = None  # Is changed internally
        self.pronoun_number = pronoun_number  # varies by pronoun

        # JSON data
        self.conjugation_data = conjugation_data
        self.verbs_list = verbs_list

        # Finding pronoun
        self.pronoun = self.conjugation_data["pronounsList"][self.pronoun_number - 1]

    def set_infinitive(self):
        """This function grabs a random infinitive from the verbs.json file in /src/."""
        self.infinitive = random.choice(self.verbs_list)
        self.conjugated = None  # always gets reset even after the verb changes

    def set_pronoun(self, number, singular_or_plural):
        # 1 for first person, 2 for second person informal, 3 for second person formal, and 4 for third person
        pass

    def detect_verb_type(self):
        """This function will detect whether a verb is soft or hard based on its last vowel."""
        pass

    def conjugate(self):
        """This function must be overridden by child classes."""
        return None

