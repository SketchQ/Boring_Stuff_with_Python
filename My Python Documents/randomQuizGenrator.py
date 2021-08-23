#! python3

#   Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair.

# Here is what the program does:

# Creates 35 different quizzes
# Creates 50 multiple-choice questions for each quiz, in random order
# Provides the correct answer and three random wrong answers for each question, in random order
# Writes the quizzes to 35 text files
# Writes the answer keys to 35 text files


    ## This means the code will need to do the following:

# Store the states and their capitals in a dictionary
# Call open(), write(), and close() for the quiz and answer key text files
# Use random.shuffle() to randomize the order of the questions and multiple-choice options

## Step 1: Store the Quiz Data in a Dictionary
# randomQuizGenerator.py -- Creates quizzes with questions and answers in random order, along with the answer key.

import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.

for quizNum in range(35):
    #  Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt','w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt','w')
    #  Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((''*20)+f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')
    #  shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    #  Loop though all 50 states,making a question for each.
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #  Write the question and answer options to the quiz file.
        quizFile = open(f'capitalsquiz{quizNum + 1}.txt','a')
        answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt','a')
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"  {'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')    
        #  write the answer key to a file
        answerKeyFile.write(f"{questionNum+1}. {'ABCD'[answerOptions.index(correctAnswer)]}")
        quizFile.close()
        answerKeyFile.close()

## Step 2: Create the Quiz File and Shuffle the question Order

# The code in the loop will be repeated 35 times—once for each quiz—so you have to worry about only one quiz at a time within the loop. First you’ll create the actual quiz file. It needs to have a unique filename and should also have some kind of standard header in it, with places for the student to fill in a name, date, and class period. Then you’ll need to get a list of states in randomized order, which can be used later to create the questions and answers for the quiz.

## Step 3: Create the Answer Options

# Now you need to generate the answer options for each question, which will be multiple choice from A to D. You’ll need to create another for loop—this one to generate the content for each of the 50 questions on the quiz. Then there will be a third for loop nested inside to generate the multiple-choice options for each question

## Step 4: Write Content to the Quiz and Answer key Files

# All that is left is to write the question to the quiz file and the answer to the answer key file.