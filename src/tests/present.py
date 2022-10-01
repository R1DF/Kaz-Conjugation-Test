# Imports
from .base import BaseTense
import random

# Present Tense class
class PresentTense(BaseTense):
    """
    The Present Tense class is special. This is because the present tense as a whole in Kazakh comes in two forms.
    Simple present: Men turmyn.
    The simple present can only be used for 4 verbs. turu - to stand, zhuru - to walk, otyru - to sit, zhatu - to lie [down]

    Complex present: Men oqyp zhatyrmyn.
    This uses one of the previously said 4 verbs as auxiliaries to make conjugating all others possible.
    Determining which auxiliary verb depends either on the duration of the activity or what the subject is doing.
    
    Time:
    turu - very short duration
    zhuru - short duration
    otyru - quite long duration
    zhatu - longest duration
    
    Subject activity:
    turu - whilst standing
    zhuru - whilst walking or running (moving)
    otyru - whilst sitting
    zhatu - whilst lying [down]

    Negation is also taking 2 forms. If there's negation involved, the class will just generate 2 sentences.
    """
    def __init__(self, pronoun_number, is_negated, form="simple"):
        BaseTense.__init__(self, pronoun_number, is_negated)  # Inheritance
        self.name = "Present Tense"
        self.description = "The tense used to indicate something that happens right as it's being said. It comes in 2 forms."
        self.form = form  # Either simple or complex
        self.auxiliary_verbs = self.conjugation_data["tensesConjugations"]["present"]["auxiliaryVerbs"]
        self.form_specific = f"{self.form[0].upper()}{'A' if not self.is_negated else 'N'}"

    def check_special_verb(self):  # I HATE ZHATU
        if self.infinitive == "жату":
            self.infinitive_used = "жатыру"
        else:
            self.infinitive_used = self.infinitive


    def check_special_verb_stem_negated(self):
        if self.infinitive_used == "жатпау":
            return "жат"
        else:
            return self.infinitive[:-3]

    def set_infinitive(self):  # Override
        if self.form == "simple":
            self.infinitive = random.choice(self.auxiliary_verbs)
        else:
            self.infinitive = random.choice(self.verbs_list)

        if self.is_negated and self.form != "complex": # The 2nd check is there because the first variant has its own negation
            self.negate()
        self.check_special_verb()
        self.conjugated = None

    def conjugate_affirmated(self):
        determinant = {"hard": 0, "soft": 1}[self.detect_last_vowel_type()]
        if self.form == "simple":
            self.conjugated = self.infinitive_used[:-1] + self.conjugation_data["tensesConjugations"]["present"]["affirmativeEndings"][self.pronoun_number - 1][determinant]
        else:
            # Getting infinitive's stem (e.g. jep as an example)
            match self.detect_letter_type(-2):
                case "hard" | "soft":
                    stem = self.conjugation_data["tensesConjugations"]["present"]["stemSuffixes"][2]
                case _:
                    stem = self.conjugation_data["tensesConjugations"]["present"]["stemSuffixes"][determinant]

            # Getting auxiliary verb to use
            auxiliary_verb = random.choice(self.auxiliary_verbs)
            auxiliary_verb = "жатыру" if auxiliary_verb == "жату" else auxiliary_verb
            auxiliary_determinant = {"hard": 0, "soft": 1}[self.detect_vowel_type(auxiliary_verb[-3])]

            self.conjugated = self.infinitive_used[:-1] + stem + " " + auxiliary_verb[:-1] + self.conjugation_data["tensesConjugations"]["present"]["affirmativeEndings"][self.pronoun_number - 1][auxiliary_determinant]

    def conjugate_negated(self):
        if self.form == "simple":
            # Getting stem suffix
            stem = self.check_special_verb_stem_negated()
            match stem:
                case "жат":
                    negative_suffix = self.conjugation_data["tensesConjugations"]["present"]["negativeSuffixes"][1][0]
                case "отыр" | "тұр":
                    negative_suffix = self.conjugation_data["tensesConjugations"]["present"]["negativeSuffixes"][0][0]
                case _:
                    negative_suffix = self.conjugation_data["tensesConjugations"]["present"]["negativeSuffixes"][0][1]

            # Getting ending
            ending = self.conjugation_data["tensesConjugations"]["present"]["negativeEndings"][self.pronoun_number - 1]
            self.conjugated = stem + negative_suffix + " жоқ" + ending
        else:
            # There's 2 ways so the conjugated variable will be a list of 2.
            self.conjugated = []

            # First variant: (long version)
            # Getting the stem is the same.
            stem = self.infinitive_used[:-1]
            determinant = {"hard": 0, "soft": 0}[self.detect_last_vowel_type()]
            match self.detect_letter_type(-2):
                case "hard" | "soft":
                    stem_suffix = self.conjugation_data["tensesConjugations"]["present"]["stemSuffixes"][2]
                case _:
                    stem_suffix = self.conjugation_data["tensesConjugations"]["present"]["stemSuffixes"][determinant]

            # Next we have to get the auxiliary verb and add its negative suffix.
            auxiliary_verb = random.choice(self.auxiliary_verbs)
            match auxiliary_verb:
                case "жату":
                    negative_suffix = self.conjugation_data["tensesConjugations"]["present"]["negativeSuffixes"][1][0]
                case "отыру" | "тұру":
                    negative_suffix = self.conjugation_data["tensesConjugations"]["present"]["negativeSuffixes"][0][0]
                case _:
                    negative_suffix = self.conjugation_data["tensesConjugations"]["present"]["negativeSuffixes"][0][1]

            # Then we need the joq part. Ugh.
            ending = self.conjugation_data["tensesConjugations"]["present"]["negativeEndings"][self.pronoun_number - 1]
            self.conjugated.append(
                stem + stem_suffix + " " + auxiliary_verb[:-1] + negative_suffix + " жоқ" + ending
            )

            # Shorter variant. This one's gonna be easier.
            self.negate(False) # Negation is involved here
            stem = self.infinitive[:-1]  # Not the "_used" one because we need it to be raw this time.

            # Auxiliary verb must be rewritten since it's not negated.
            auxiliary_verb = "жатыру" if auxiliary_verb == "жату" else auxiliary_verb
            determinant = {"hard": 0, "soft": 1}[self.detect_vowel_type(auxiliary_verb[-3])]
            ending = self.conjugation_data["tensesConjugations"]["present"]["affirmativeEndings"][self.pronoun_number - 1][determinant]

            # Finalizing
            self.conjugated.append(
                stem + self.conjugation_data["tensesConjugations"]["present"]["stemSuffixes"][3] + " " + auxiliary_verb[:-1] + ending
            )

    def conjugate(self):
        if not self.is_negated:
            self.conjugate_affirmated()
        else:
            self.conjugate_negated()

    def print_sentence(self):  # Override due to various forms
        match self.form_specific:
            case "SA" | "SN" | "CA":
                print(self.pronoun.capitalize() + " " + self.conjugated + ".")
            case _:
                for conjugated_index in range(len(self.conjugated)):
                    print(f"Variant {conjugated_index+1}: {self.pronoun.capitalize()} {self.conjugated[conjugated_index]}.")