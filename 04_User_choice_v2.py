# Version 2 - error message included when calling function

#functions go here
def choice_checker(question, error_txt):


    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "+" or response == "addition":
            return response
        elif response == "x" or response == "multiplication":
            return response
        elif response == "-" or response == "subtraction":
            return response
        elif response == "//" or response == "division":
          return response
        elif response == "mixture":
          return response

        # check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error_txt)

# Main routine goes here


# loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # ask user for choice and check its valid
    user_choice = choice_checker("Choose from Addition (+), Subtraction (-), Multiplication (x), Division (//) or Mixture :",
                                 "Please choose from Addition (+), Subtraction (-), Multiplication (x), Division (//) or Mixture "
                                 "(or xxx to quit) ")

    # print out choice for comparison purposes
    print("You chose {}".format(user_choice))