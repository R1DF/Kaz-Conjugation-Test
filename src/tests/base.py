"""
Base class for a tense of the Kazakh language.
"""
# Imports
import random
from data_getter import tenses_file_data as conjugation_data
from data_getter import verbs_list

# Base for every Tense class
class BaseTense:
    def __init__(self, pronoun_number, is_negated=False):
        # Metadata
        self.name = None
        self.description = None
        self.is_negated = is_negated

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
        """This function grabs a random infinitive from the verbs.json file in /src/.
         will negate the infinitive automatically if the is_negated boolean is True."""
        self.infinitive = random.choice(self.verbs_list)
        if self.is_negated:
            self.negate()
        self.conjugated = None  # always gets reset even after the verb changes

    def get_suffixes(self, tense_name):
        """Sets suffixes depending on the tense name."""
        self.suffixes = self.conjugation_data["tensesConjugations"][tense_name]["suffixes"]

    def get_endings(self, tense_name):
        """Sets endings depending on the tense name."""
        self.endings = self.conjugation_data["tensesConjugations"][tense_name]["endings"]

    def detect_vowel_type(self, vowel):
        """Returns the type of the vowel. Simplest detector."""
        if not self.is_vowel(vowel):
            return  # Checking if the consonant is actually a vowel

        soft_vowels = self.conjugation_data["vowels"]["soft"]
        return "soft" if vowel.upper() in soft_vowels else "hard"

    def detect_consonant_type(self, consonant):
        """Returns the type of the consonant. Similar to self.detect_vowel_type."""
        if self.is_vowel(consonant):
            return  # Checking if the consonant is actually a consonant

        consonants = self.conjugation_data["consonants"]
        if consonant in consonants["sonorant"]:
            return "sonorant"
        elif consonant in consonants["voiced"]:
            return "voiced"
        else:
            return "voiceless"

    def negate(self, reset=True):
        """Will negate the verb inside."""

        # First we must check if the penultimate letter is a vowel or not
        if self.is_vowel(self.infinitive[-2]):
            ending_index = 0
        else:
            if self.infinitive[-2].upper() in self.conjugation_data["negationSuffixes"]["M"]:
                ending_index = 0
            elif self.infinitive[-2].upper() in self.conjugation_data["negationSuffixes"]["P"]:
                ending_index = 1
            else:
                ending_index = 2

        # Using string properties to transform the infinitive
        self.infinitive = self.infinitive[:-1] + self.conjugation_data["negationEndings"][ending_index][{"hard": 0, "soft": 1}[self.detect_last_vowel_type()]] + "у"

        # Checking if the conjugated form is outdated, becomes None if it is
        if self.conjugated is not None and reset:
            self.conjugated = None

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

