# importing csv module
import csv

#csv file name
filename = 'Trivia Game.csv'

# initializing the titles and rows list
fields = []
rows = []

# user friendly greeting
print('Greetings! I am your friendly neighbothood trivia game!')
print('\nWhen ansering questions refrain from entering anything other than the letter of your choice')
print('No other answers will be accepted')

choice = None
correct_answer = 'Correct, Great Job!'
wrong_answer = 'Incorrect!'
points_possible = 15

# main loop
while choice != 'q':
    points_obtained = 0
    index = 0
    decision = input('Choose a Topic From List: Anime, Marvel, One Liners, Action Movies, Comedy Movies, Horror Movies, General Knowledge, Sports\n')

    decision = decision.capitalize()
    print('You chose' ,decision)
    points_obtained = 0

    
    #   reading the csv file
    with open(filename, 'r') as csvfile:
    # creating a new csv reader object
        csvreader = csv.reader(csvfile)

    #extracting field names through first row
        fields = next(csvreader)

    # extracting data from each row one by one 
        for row in csvreader:
            rows.append(row)

    while decision == 'Anime': #A loop thats runs the specific trivia
        index = 7
        for row in rows[:15]:
            print('\n')

            #parsing each column of a row
            for col in row[1:6]:
                print(col, end = ' ')
                print('\n')

            answer = input('Enter your answer: ')
            answer = answer.lower()
                
            if answer == row[index]:
                print(correct_answer)
                points_obtained += 1
                             
            else:
                print(wrong_answer)

        decision = None
        retry = input('Would you like to play again? y/n: ')
        if retry == 'y':
            decision = None
        else:
            print('Thank you for playing! You got',int((points_obtained/points_possible)*100),'%!')
            choice = 'q'
            

    while decision == 'Marvel': #A loop thats runs the specific trivia
        index = 7
        for row in rows[18:31]:
            print('\n')

            #parsing each column of a row
            for col in row[1:6]:
                print(col, end = ' ')
                print('\n')

            answer = input('Enter your answer: ')
            answer = answer.lower()
                
            if answer == row[index]:
                print(correct_answer)
                points_obtained += 1
                             
            else:
                print(wrong_answer)

        decision = None
        retry = input('Would you like to play again? y/n: ')
        if retry == 'y':
            decision = None
        else:
            print('Thank you for playing! You got',int((points_obtained/points_possible)*100),'%!')
            choice = 'q'
                           

    while decision == 'One liners': #A loop thats runs the specific trivia
        index = 7
        for row in rows[34:48]:
            print('\n')

            #parsing each column of a row
            for col in row[1:6]:
                print(col, end = ' ')
                print('\n')

            answer = input('Enter your answer: ')
            answer = answer.lower()
                
            if answer == row[index]:
                print(correct_answer)
                points_obtained += 1
                             
            else:
                print(wrong_answer)

        decision = None
        retry = input('Would you like to play again? y/n: ')
        if retry == 'y':
            decision = None
        else:
            print('Thank you for playing! You got',int((points_obtained/points_possible)*100),'%!')
            choice = 'q'
            

    while decision == 'Action' or decision == 'Action movies': #A loop thats runs the specific trivia
        index = 7
        for row in rows[51:64]:
            print('\n')

            #parsing each column of a row
            for col in row[1:6]:
                print(col, end = ' ')
                print('\n')

            answer = input('Enter your answer: ')
            answer = answer.lower()
                
            if answer == row[index]:
                print(correct_answer)
                points_obtained += 1
                             
            else:
                print(wrong_answer)

        decision = None
        retry = input('Would you like to play again? y/n: ')
        if retry == 'y':
            decision = None
        else:
            print('Thank you for playing! You got',int((points_obtained/points_possible)*100),'%!')
            choice = 'q'
            

    while decision == 'Comedy' or decision == 'Comedy movies': #A loop thats runs the specific trivia
        index = 7
        for row in rows[67:80]:
            print('\n')

            #parsing each column of a row
            for col in row[1:6]:
                print(col, end = ' ')
                print('\n')

            answer = input('Enter your answer: ')
            answer = answer.lower()
                
            if answer == row[index]:
                print(correct_answer)
                points_obtained += 1
                             
            else:
                print(wrong_answer)

        decision = None
        retry = input('Would you like to play again? y/n: ')
        if retry == 'y':
            decision = None
        else:
            print('Thank you for playing! You got',int((points_obtained/points_possible)*100),'%!')
            choice = 'q'
            

    while decision == 'Horror' or decision == 'Horror movies': #A loop thats runs the specific trivia
        index = 7
        for row in rows[83:96]:
            print('\n')

            #parsing each column of a row
            for col in row[1:6]:
                print(col, end = ' ')
                print('\n')

            answer = input('Enter your answer: ')
            answer = answer.lower()
                
            if answer == row[index]:
                print(correct_answer)
                points_obtained += 1
                             
            else:
                print(wrong_answer)

        decision = None
        retry = input('Would you like to play again? y/n: ')
        if retry == 'y':
            decision = None
        else:
            print('Thank you for playing! You got',int((points_obtained/points_possible)*100),'%!')
            choice = 'q'
            

    while decision == 'General' or decision == 'General knowledge': #A loop thats runs the specific trivia
        index = 7
        for row in rows[99:113]:
            print('\n')

            #parsing each column of a row
            for col in row[1:6]:
                print(col, end = ' ')
                print('\n')

            answer = input('Enter your answer: ')
            answer = answer.lower()
                
            if answer == row[index]:
                print(correct_answer)
                points_obtained += 1
                             
            else:
                print(wrong_answer)

        decision = None
        retry = input('Would you like to play again? y/n: ')
        if retry == 'y':
            decision = None
        else:
            print('Thank you for playing! You got',int((points_obtained/points_possible)*100),'%!')
            choice = 'q'
            

    while decision == 'Sports': #A loop thats runs the specific trivia
        index = 7
        for row in rows[116:129]:
            print('\n')

            #parsing each column of a row
            for col in row[1:6]:
                print(col, end = ' ')
                print('\n')

            answer = input('Enter your answer: ')
            answer = answer.lower()
                
            if answer == row[index]:
                print(correct_answer)
                points_obtained += 1
                             
            else:
                print(wrong_answer)

        decision = None
        retry = input('Would you like to play again? y/n: ')
        if retry == 'y':
            decision = None
        else:
            print('Thank you for playing! You got',int((points_obtained/points_possible)*100),'%!')
            choice = 'q'
                          

