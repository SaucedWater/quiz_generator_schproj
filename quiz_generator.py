import random #imports the random module

questions_list = [] #used to later store a dictionary for the questions and answers
score = 0 #sets user scores to 0

def access_file(files): #function to access the file
    with open(files, "r") as quiz:
        quiz = quiz.readlines()
        
    return quiz
        
def num_remover(string): #function to remove numbers fromm qn lines (e.g. remove "1." from "1. Sample Text")
    new_str = ''  # creates an empty string
    for i in range(len(string)): # loops through each character of string
                
        #1st part: Checks if character is a digit
        #2nd part: checks if current index is 0 OR if the character before current character is not digit
        if string[i].isdigit() and (i == 0 or not string[i - 1].isdigit()):

            continue
        # for when character does not contain a digit and not a dot
        elif not string[i].isdigit() and string[i] != '.': 
            new_str += string[i]  # append the character to the new string
    return new_str

def is_question(line):
    line = line.split('.') #splits line using '.', each qn contains '.'
    
    if len(line) > 1: # checks if there is more than 1 element in the line list
        if line[0].isnumeric() and line[1].startswith(' '): #checks if the line starts with an int and space
            return True

        else: #returns false if line does not start with an int and a space 
            return False
    return False #returns false if after splitting line has only 1 or 0 elements

def maintest(quiz_path): #main function to assign qn n ans respectively
    quiz = access_file(quiz_path) #accesses he file
    for line in quiz:  # runs through the whole file
        new_q = line.strip() #removes leading spaces

        if is_question(new_q):  # checks if the line is a qn
            questions_list.append({'Question': num_remover(new_q), 'options': []}) #appends line if it returns true
        else:  # options and answers will go here
            options = new_q
            questions_list[-1]['options'].append(options) #append options/answers 
            
    return questions_list

questionz = maintest(r"quiz_questions.txt") #assign the entire question_list to questionz 
#At this point, the file should have each qn and its ans in the same list, to prepare to randomise if user wants to

quizlet = True

while quizlet:
    print('\t\t\t Welcome to my quiz generator')
    
    while True: #ask how many qn the user wants/randomize qn/options
        num_qn = input("How many questions do you need? ")
        
        if num_qn.isdigit(): #checks if num_qn is a digit
            num_qn = int(num_qn)
            
            if num_qn > 50: #list only has 50qn, hence if more than 50 is input it returnd invalid input
                print('Invalid Input. Please enter a number 1-50.')
                continue
            
        else:
            print('Invalid Input. Please enter a number 1-50.')
            continue
        
        choiceqn = input("Do you want to randomize the questions? (y/n) ").lower()
        
        if choiceqn == 'y': 
            random.shuffle(questionz) #randomizes and shuffles the qn
            
        elif choiceqn != 'n':
            print('Invalid Input. Please enter either y or n.')
            continue
            
            
        choiceans = input("Do you want to randomize the answers? (y/n) ").lower()
        
        if choiceans == 'y':
            for ele in questionz:
                random.shuffle(ele['options']) #randomizes and shuffles the options
        
        elif choiceans != 'n':
            continue
            print('Invalid Input. Please enter either y or n.')
            
        ready_or_not = input("Are you ready to take the test? ")
        
        if ready_or_not == "":
            pass
            
        else:
            pass
                
        for qns in range(0, num_qn): #loops through from 0 to the amount of qn the user states
            print("Questions {}: {}\n".format(qns + 1, questionz[qns]['Question'])) #uses format to print questios
            
            for x in range(len(questionz[qns]['options'])): #loops through the options in the given question key
                if questionz[qns]['options'][x].endswith('*'): #checks if the options ends with "*"
                    right_ans = questionz[qns]['options'][x][:-1] #assigns the option to right_ans variable
                    right = x + 1 #assigns the index to right variable
                    print("Options {}: {}".format(x+1, questionz[qns]['options'][x][:-1])) #prints out the ans w/o *
                else:
                    print("Options {}: {}".format(x+1, questionz[qns]['options'][x])) # prints out the options
                    
            le_input =  input("Option: ") #gets user input 
            
            if le_input.isdigit(): #checks if the input is a digit
                new_input = int(le_input) #changes type to int
                
                if new_input == right: #if user selects the correct option no.
                    print('\t\t\tGood Job!', right_ans, "is correct!\n")
                    score += 1 #adds 1 score to the score variable
                    
                else:
                    print('\t\t\tOops. Correct answer is ', right_ans, '\n') #uses right_ans to print the correct ans
                    
            else:
                print('Invalid Input! Please enter a valid Option number.\n')
                
        print(f'Your score is {round(100 * (score / num_qn), 2)}%') #prints score once user finishes the qns

        while True:
            try_again = input('Do you want to try again? (y/n) ').lower()

            if try_again == 'n':
                print('End of programme')
                break

            elif try_again == 'y':
                break

            else:
                print('Invalid Input! Please enter either y/n.')
                
        if try_again == 'n':
            quizlet = False
            break
            
        else:
            continue