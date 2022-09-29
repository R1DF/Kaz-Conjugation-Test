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
        self.suffixes = []
        self.endings = []

        # JSON data
        self.conjugation_data = conjugation_data
        self.verbs_list = verbs_list

        # Finding pronoun
        self.pronoun = self.conjugation_data["pronounsList"][self.pronoun_number - 1]

    def set_infinitive(self):
        """This function grabs a random infinitive from the verbs.json file in /src/."""
        self.infinitive = random.choice(self.verbs_list)
        self.conjugated = None  # always gets reset even after the verb changes

    def get_suffixes(self, tense_name):
        """Sets suffixes depending on the tense name."""
        self.suffixes = self.conjugation_data["tensesConjugations"][tense_name]["suffixes"]

    def get_endings(self, tense_name):
        """Sets endings depending on the tense name."""
        self.endings = self.conjugation_data["tensesConjugations"][tense_name]["endings"]

    def detect_vowel_type(self, vowel):
        """Returns the type of the vowel. Simplest detector."""
        soft_vowels = self.conjugation_data["vowels"]["soft"]
        return "soft" if vowel.upper() in soft_vowels else "hard"

    def negate(self):
        """Will negate the verb inside."""
        # if self.detect_letter_type(len(self.infinitive) - 1) != "consonant":
            # self.infinitive = self.infinitive[:-1] +

    def is_vowel(self, letter):
        """Returns if the letter given is a vowel or not."""
        return letter.upper() in self.conjugation_data["vowels"]["soft"] + self.conjugation_data["vowels"]["hard"]

    def detect_letter_type(self, letter_index):
        """If the letter of the verb is a vowel, it returns the vowel type: "soft" or "hard".
        If it's a consonant, it returns "consonant".
        If the infinitive isn't set, it returns None."""
        if self.infinitive is None:
            return

        letter = self.infinitive[letter_index]
        if self.is_vowel(letter):
            return self.detect_vowel_type(letter)
        return "consonant"

    def detect_last_vowel_type(self):
        """
        Returns the type of the last vowel in the infinitive. if the infinitive is None, None is returned.
        """
        if self.infinitive is None:
            return

        for letter_index in range(len(self.infinitive) - 2, 0, -1):
            if self.is_vowel(self.infinitive[letter_index]):
                return self.detect_letter_type(letter_index)

    def print_sentence(self):
        """This function will print out the sentence to the screen that contains the pronoun and conjugated verb.
        if the verb hasn't been set or conjugated, nothing happens."""
        if self.infinitive is None or self.conjugated is None:
            return
        print(self.pronoun.capitalize() + " " + self.conjugated + ".")

    def conjugate(self):
        """This function must be overridden by child classes."""
        return None

