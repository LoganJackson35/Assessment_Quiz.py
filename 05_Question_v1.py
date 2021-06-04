# Reset Questions given
questions_given = 0

# Ask user how many Questions
question = ("How many questions would you like? :", 0, 20, questions_given)

if questions_given == 1:
  print ("You have chosen {} question")
else:
  print("You have chosen {} questions ")
question_error = "Pick from 1 - 20  number of questions"

questions = "Question {} of  {}".format(questions_given + 1)
question_decoration = "-"