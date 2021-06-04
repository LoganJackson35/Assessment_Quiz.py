# This Is Where you will edit large portions of the Base Component without breaking the main base component.
import random
import math

#Functions

def choice_checker(question, valid_list, error_txt):


    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through lsit and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
          if response == item[0] or response == item:
              return item

        # output error if item not in list
        print(error_txt)
        print()

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes / no")
       
def statement_generator(statement, decoration):

   sides= decoration * 3

   statement = "{} {} {}".format(sides, statement, sides)
   top_bottom = decoration * len(statement)

   print(top_bottom)
   print(statement)
   print(top_bottom)

   return ""
# Main Routine
# Resets Round counter
questions_given = 0

# Lists:
# List for Yes / No and exit code
yes_no_list = ["yes", "no", "xxx"]
#  List for Math quiz and their arithmetic counterparts
arithmetic_list = ["Addition", "+", "Subtraction", "-", "Multiplication", "x", "Division", "//", "Mixture"]


# Ask User if they have played before, if no, display instructions.
# Otherwise continue
played_before = yes_no("Have you played before? ")
print()

# Display instructions for user and displays error when User doesnt input arithemtic
choose_instruction = ("Pick an Arithmetic ")
choose_error = ("Please choose from Addition, Subtraction, Multiplication, Division or Mixture (or xxx to  quit) ") 
# ask user for choice and check its valid
choose = choice_checker(choose_instruction, arithmetic_list,
choose_error)


question = ("How many questions would you like? :")
# Question counter to display how many questions have been given.
questions = "Question {} of  {}".format(questions_given + 1)
question_decoration = "-"



