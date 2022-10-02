"""
Kazakh Conjugation Test
A program that will conjugate a verb for you with any pronoun and tense.

Contains code similar to Kazakh Declension Test with some improvements.
https://github.com/R1DF/Kaz-Declension-Test/
"""

# Imports
import os
from data_getter import tenses_file_data
from tests.continuous import ContinuousTense
from tests.present import PresentTense
from tests.past_simple import PastSimpleTense
from tests.future_motivative import FutureMotivativeTense
from tests.future_potential import FuturePotentialTense
from tests.past_obvious import PastObviousTense
from tests.past_uncertain import PastUncertainTense
from tests.past_continuous import PastContinuousTense

# Predefined functions
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def try_input(message, num_range):
    while True:
        user_input = input(f"{message}: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input < num_range[0]:
                print("The number is too low.\n")
            elif user_input > num_range[1]:
                print("The number is too high.\n")
            else:
                return user_input
        else:
            print("Please enter a number.\n")

def try_yn_input(message):
    while True:
        user_input = input(f"{message} (Y/N): ").upper().strip()
        if user_input == "Y":
            return True
        elif user_input == "N":
            return False
        print("Please enter either Y or N.\n")

def make(tense_number, pronoun_number, is_negated):
    match tense_number:
        case 1:
            tense = ContinuousTense(pronoun_number, is_negated)
        case 2:
            print("\n\nThis tense takes 2 forms! Select one.\n1. Simple present tense\n2. Complex present tense")
            form = "simple" if try_input("Select tense", (1, 2)) == 1 else "complex"
            tense = PresentTense(pronoun_number, is_negated, form)
        case 3:
            tense = PastSimpleTense(pronoun_number, is_negated)
        case 4:
            tense = FutureMotivativeTense(pronoun_number, is_negated)
        case 5:
            tense = FuturePotentialTense(pronoun_number, is_negated)
        case 6:
            tense = PastObviousTense(pronoun_number, is_negated)
        case 7:
            tense = PastUncertainTense(pronoun_number, is_negated)
        case 8:
            tense = PastContinuousTense(pronoun_number, is_negated)
        case _:
            return

    clear()
    tense.set_infinitive()
    tense.conjugate()
    print(f"{tense.name.upper()}\n{tense.description}\n\nSENTENCE:")
    tense.print_sentence()
    print(f"\nPronoun: {tense.pronoun}\nInfinitive: {tense.infinitive}\nConjugated: {tense.conjugated}\n\n")
    if tense.is_negated:
        print("The infinitive is in its negative form.\n")
    input("Press Enter to Exit.\n")

# Main function
def main():
    os.system("title Kazakh Conjugation Test")
    # System loop
    while True:
        clear()
        print("Kazakh Conjugation Test\nPlease enter a random tense you would like to conjugate in. The verb will be assigned randomly.\n")
        for tense_index in range(len(tenses_file_data["tensesList"])):
            print(f"{tense_index + 1}. {tenses_file_data['tensesList'][tense_index]}")
        print("9. Quit")
        selected_tense = try_input("Enter tense by number", (1, 9))
        print("\n")  # line breaks

        # Checking if the user wanted to quit
        if selected_tense == 9:
            clear()
            quit()

        # Continuing otherwise, asks for selected pronoun
        for pronoun_index in range(len(tenses_file_data["pronounsList"])):
            pronoun = tenses_file_data['pronounsList'][pronoun_index]
            description = tenses_file_data["pronounsDescriptions"][pronoun_index]
            print(f"{pronoun_index + 1}. {pronoun} ({description})")
        selected_pronoun = try_input("Enter desired pronoun to conjugate", (1, 8))

        # Running test maker
        print("\n")  # another line break
        make(selected_tense, selected_pronoun, try_yn_input("Negate the verb?"))

# Running
if __name__ == "__main__":
    main()
