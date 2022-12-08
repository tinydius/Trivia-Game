'''
Runs a trivia type interface that has different genres and collects points and returns them to you at the end
'''

# Importing the function to get needed output
import random

# lists of question to be shown in trivia
anime_questions = ['In which anime series is Ash Ketchum the main character?', "What color is Naruto's Hair?", 'What country does anime come from?', 'The first episode of Soul Eater was released in 2010', 'Which anime does Ichigo Kurosaki belong to?','What is the meaning of Aiko?', 'Which anime series revolves around a boy who sells his soul to a demon?', 'Who was the first character in ‘Dragon Ball Z’ who achieved the Super Saiyan 2?', 'Which Hunter X Hunter character wants to be a doctor', 'Who was the first Joestar', 'True or False: Saiki K’s favorite food is coffee jelly', 'What was Christa’s real name in Attack on Titan', 'What was Gon’s Hunter Exam number?', 'Demon Slayer: Infinity Train became the highest grossing anime and Japanese film of all-time', 'What Anime won Anime of the Year in Crunchyroll Anime Awards 2021']

marvel_questions = ['How many Infinity Stones are there?', 'What species is Groot?', 'In the first Avengers movie, how many avengers do we actually see?', 'Which Marvel movie has the shortest running time?', 'Who was Doctor Strange’s mentor?', 'Which eye does Thor lose? ', '	Who was the first female superhero to appear in the title of an MCU film? ', 'Who is Wolverine’s biggest enemy?', 'Is it true that the Hulk is immune to all kinds of diseases and viruses? ', "What symbol is on Captain America's shield?", 'The final battle between Mysterio and Spiderman takes place on which bridge? ', 'What newspaper does Peter Parker work for? ', "What’s Deadpool's real name? ", 'Who is Tony Stark’s father?', "Captain America’s shield and Bucky's arm are made of what?"]

one_liners = ['What movie is this line from? “A martini. Shaken, not stirred.”', 'What movie is this line from? “This Is Sparta”', 'What Movie is this line from? “Hasta la vista, baby.” ', 'What Movie is this line from?  "It was beauty killed the beast." ', 'What Movie is this line from? You’re killin’ me, Smalls.” ', 'What Movie is this line from? “Toto, I\'ve a feeling we\'re not in Kansas anymore.” ', 'What Movie is this line from? “I\'m walking here! I\'m walking here!”', 'What Movie is this line from? “Here\'s Johnny!” ', 'What Movie is this line from? “You had me at Hello”', 'What Movie is this line from? “You can’t handle the truth”', 'What Movie is this line from? “I feel the need, the need for speed”', 'What Movie is this line from? “I’m the King of the World”', 'What Movie is this line from? “I’ll get you, my pretty, and your little dog too!”', 'What Movie is this line from? “Carpe Diem. Seize the day, boys. Make your lives extraordinary”', 'What Movie is this line from? “"Every day above ground is a good day."', 'What movie is the line from? "I will look for you, I will find you, and I will kill you" ']

action_questions = ['How many movies make up the Fast & Furious franchise so far?', 'Who performed the theme song for the upcoming James Bond movie No Time to Die?', 'Will Smith and Martin Lawrence team up in which 1995 action-comedy movie?', 'What is the name of the lead character in the 1983 film "Scarface"?', 'Starring Arnold Schwarzenegger, the 1987 movie "The Running Man" is based on a novel by whom?', '"Go ahead, make my day." is a well-known quote from which classic-action film?', 'In The Matrix, does Neo take the blue pill or the red pill?', 'What is the kidnapper’s response to Liam Neeson’s epic monologue in Taken?', 'Which pet of John Wick’s do the gangsters kill', 'What computer program caused the end of the world in Terminator?', 'What war did John Rambo fight in?', 'Complete the 300 quote: “Tonight, we...”', 'What does the Predator see?', 'Which of these Fast & Furious movies introduced Dwayne Johnson’s character?', 'In The Matrix, what does déjà vu mean?']

comedy_questions = ['What is the number 1 rated comedy movie of all time according to the movie review website, Rotten Tomatoes?', 'How much did comedy actor Will Ferrell turn down to do an Elf Movie 2?', 'Who plays Sherman Klump in The Nutty Professor (1996)?', 'What comedy movie franchise do Jim Carrey and Harry Dunne play intelligently-challenged characters?', 'Name the comedy movie that features the hilarious line: \'Santa, I know him!\'', 'Which comedy movie sees Terry Crews singing and dancing to \'A thousand miles\' by Vanessa Carlton?', 'In which movie do we see 2 grown-up men pleading with their parents whether they can turn their beds into bunk beds? ', 'It took the makeup department an hour per day to create Eddie Murphy\'s transformation for The Nutty Professor', 'What city are Harry and Lloyd trying to get to in \'Dumb & Dumber\'?', 'In “Wedding Crashers,” what does Will Ferrell’s character crash?', 'According to Buddy the Elf, the four food groups are candy, candy canes, candy corns and…?', 'In what movie does the Stay Puft Marshmallow Man begin destroying New York City?', 'Making its debut in 1999, "Bigger, Longer and Uncut" was an animated movie version of which hit TV show?', 'In the movie "Ted", who does the voice of the bear?', 'What is Rita\'s drink of choice in \'Groundhog Day\'?']

horror_questions = ['What was the first horror movie in color?', 'What horror movie was the debut of Johnny Depp?', 'What color is present in almost every shot of The Shining?', 'What is the famous quote from The Sixth Sense?', 'How many Saw movies are there?', 'What color jumpsuit did the doppelgangers wear in Jordan Peele’s Us?', 'In which movie do we see a high school girl (Drew Barrymore) get increasingly threatening phone calls?', 'Which classic horror film stars a serial killer dressed as William Shatner?', 'What eerie film is credited with coining the notorious phrase, “Do you like horror movies?”', 'In which film did Annabelle the doll make her debut? ', 'What arms does Leatherface prefer? ', 'How many Friday the 13th movies are there?', 'What is the name of the creatures from the Predator franchise? ', 'What is Chucky’s real name within the Child’s Play film series?', 'In Scream, what is Randy’s number one rule to survive a horror movie? ']

general_questions = ['What does “www” stand for in a website browser?', 'How long is an Olympic swimming pool (in meters)?', 'What is "cynophobia"?', 'How many languages are written from right to left?', 'Which animal can be seen on the Porsche logo?', 'What is the name of the largest ocean on earth?', 'Who was the first woman pilot to fly solo across the Atlantic?', 'Which country consumes the most chocolate per capita?', 'What is the rarest M&M color?', 'What was the first soft drink in space?', 'Which is the only edible food that never goes bad?', 'Which country invented ice cream?', 'What is Earth\'s largest continent?', 'Area 51 is located in which U.S state?', 'What in the state of Georgia, it’s illegal to eat what with a fork?', 'What is a duel between three people called?']

sports_questions = ['What’s the diameter of a basketball hoop in inches?', 'The Olympics are held every how many years?', 'What sport is best known as the ‘king of sports’?', 'Who has won more tennis grand slam titles, Venus Williams or Serena Williams?', 'What country has competed the most times in the Summer Olympics yet hasn’t won any kind of medal?', 'How many holes are played in an average round of golf?', 'How long is a marathon?', 'A sporting event is held every year on Memorial Day. What is it?', '9.	How old was Tiger Woods when he won the Masters?', 'How many Olympic games were held in countries that no longer exist?', 'What team won the very first NBA game in 1946?', 'What African country was the first ever to qualify for a World Cup?', 'In what year were women allowed to compete in the modern Olympic games and in what sport?', 'In what game is “love” a score?', 'What country has competed the most times in the Summer Olympics yet hasn’t won a gold medal?']

#User friendly greeting

print('Greetings! I am your friendly neighbothood trivia game :)')
print('\nWhen ansering questions refrain from entering anything other than "Option" followed by the letter of your answer')
print('No other answers will be accepted')

choice = None
correct_answer = 'Correct, Great Job!'
wrong_answer = 'Incorrect!'
index = 0 
#Sets trivia to work as long as choice isnt equal to 'q' or quit
while choice != 'q':
    decision = input('Choose a Topic From List: Anime, Marvel, One Liners, Action Movies, Comedy Movies, Horror Movies, General Knowledge, Sports\n')

    decision = decision.capitalize()
    print('You chose' ,decision)

    index = 0
    points_obtained = 0
    total_points = 15
   

    while decision == 'Anime': #A loop thats runs the specific trivia
        while index <= len(anime_questions) - 1:
            current_question = anime_questions[index]
            print('\nYour question is:', current_question)
            if current_question == anime_questions[0]:  # Runs specific question at the index from list
                print('\nHere are your options:')
                print('\nOption a: Pokemon')
                print('\nOption b: Naruto')
                print('\nOption c: Dragon Ball Z')
                print('\nOption d: Bleach')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[1]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: Grey')
                print('\nOption b: Blue')
                print('\nOption c: Yellow')
                print('\nOption d: Red')
                
                answer = input('\nEnter your answer: ')
                if answer == 'option c' or answer == 'Option c' or answer == 'Option C':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[2]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: United States')
                print('\nOption b: Japan')
                print('\nOption c: Germany')
                print('\nOption d: Spain')

                answer = input('\nEnter your answer: ')
                if answer == 'option b' or answer == 'Option b' or answer == 'Option B':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1

                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[3]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: True')
                print('\nOption b: False')

                answer = input('\nEnter your answer: ')
                if answer == 'option b' or answer == 'Option b' or answer == 'Option B':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1

                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[4]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: Blue Lock')
                print('\nOption b: Attack on Titan')
                print('\nOption c: Highschool DXD')
                print('\nOption d: Bleach')

                answer = input('\nEnter your answer: ')
                if answer == 'option d' or answer == 'Option d' or answer == 'Option D':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[5]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: Child of Love')
                print('\nOption b: Demon of Hate')
                print('\nOption c: Peace')
                print('\nOption d: Joy')

                answer = input('\nEnter your answer: ')
                if answer == 'option a' or answer == 'Option a' or answer == 'Option A':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[6]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: Demon Slayer')
                print('\nOption b: Naruto')
                print('\nOption c: Black Butler')
                print('\nOption d: Hunter X Hunter')

                answer = input('\nEnter your answer: ')
                if answer == 'option c' or answer == 'Option c' or answer == 'Option C':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[7]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: Vegeta')
                print('\nOption b: Gohan')
                print('\nOption c: Trunks')
                print('\nOption d: Goku')

                answer = input('\nEnter your answer: ')
                if answer == 'option b' or answer == 'Option b' or answer == 'Option B':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == anime_questions[8]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: Feitan')
                print('\nOption b: Hisoka')
                print('\nOption c: Leorio')
                print('\nOption d: Gon')

                answer = input('\nEnter your answer: ')
                if answer == 'option c' or answer == 'Option c' or answer == 'Option C':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[9]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: Johnathon Joestar')
                print('\nOption b: Giorno Giovanna')
                print('\nOption c: Joseph Joestar')
                print('\nOption d: Jotaro Joestar')

                answer = input('\nEnter your answer: ')
                if answer == 'option a' or answer == 'Option a' or answer == 'Option A':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[10]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: True')
                print('\nOption b: False')
              

                answer = input('\nEnter your answer: ')
                if answer == 'option a' or answer == 'Option a' or answer == 'Option A':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == anime_questions[11]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: Mariah')
                print('\nOption b: Anne')
                print('\nOption c: Christa')
                print('\nOption d: Historia')
            

                answer = input('\nEnter your answer: ')
                if answer == 'option d' or answer == 'Option d' or answer == 'Option D':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[12]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: 305')
                print('\nOption b: 405')
                print('\nOption c: 269')
                print('\nOption d: 71')

                answer = input('\nEnter your answer: ')
                if answer == 'option b' or answer == 'Option b' or answer == 'Option B':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[13]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: True')
                print('\nOption b: False')
                

                answer = input('\nEnter your answer: ')
                if answer == 'option a' or answer == 'Option a' or answer == 'Option A':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == anime_questions[14]:
                print('\nYour question is: ',current_question)
                print('\nHere are your options: ')
                print('\nOption a: Attack On Titan')
                print('\nOption b: Shimoneta')
                print('\nOption c: Jujustu kaisen')
                print('\nOption d: Spy X Family')

                answer = input('\nEnter your answer: ')
                if answer == 'option c' or answer == 'Option c' or answer == 'Option C':
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1 
                else:
                    print('\n',wrong_answer)
                    index += 1

            if points_obtained == 15:
                print('Congrats, you have succesfully answered all the questions in this genre!')

            if index == len(anime_questions):
                break

        
        retry = input('\nWould you like to play Again? y/n: ') #After the loss of trivia, user input to retry or quit

        if retry == 'y':
            break

        elif retry == 'n':
            choice == 'q'
            decision == None
            break
        

    while decision == 'Marvel': #User input chose marvel
        while index <= len(marvel_questions) - 1:
            current_question = marvel_questions[index]
            print('\nYour question is:', current_question)

            if current_question == marvel_questions[0]:  # Runs specific question at the index from list
                print('\nHere are your options:')
                print('\nOption a: 6')
                print('\nOption b: 7')
                print('\nOption c: 4')
                print('\nOption d: 9')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[1]:  
                print('\nHere are your options:')
                print('\nOption a: Random Tree')
                print('\nOption b: Groot')
                print('\nOption c: Maple')
                print('\nOption d: Flora Colossus')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[2]:  
                print('\nHere are your options:')
                print('\nOption a: 9')
                print('\nOption b: 2')
                print('\nOption c: 6')
                print('\nOption d: 3')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[3]:  
                print('\nHere are your options:')
                print('\nOption a: Iron Man')
                print('\nOption b: The Winter Soldier')
                print('\nOption c: Spiderman')
                print('\nOption d: The Incredible Hulk')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[4]:  
                print('\nHere are your options:')
                print('\nOption a: Iron Man')
                print('\nOption b: The Mist')
                print('\nOption c: The Acient One')
                print('\nOption d: Peter Parker')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[5]:  
                print('\nHere are your options:')
                print('\nOption a: The Left One')
                print('\nOption b: The Right One')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[6]:  
                print('\nHere are your options:')
                print('\nOption a: Black Widow')
                print('\nOption b: Wanda')
                print('\nOption c: Catwoman')
                print('\nOption d: The Wasp')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            
            elif current_question == marvel_questions[7]:  
                print('\nHere are your options:')
                print('\nOption a: Lady Deathstrike')
                print('\nOption b: Cyber')
                print('\nOption c: Sabertooth')
                print('\nOption d: Gorgon')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[8]:  
                print('\nHere are your options:')
                print('\nOption a: True')
                print('\nOption b: False')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[9]:  
                print('\nHere are your options:')
                print('\nOption a: A circle')
                print('\nOption b: A Star')
                print('\nOption c: A Square')
                print('\nOption d: A Rhombus')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[10]:  
                print('\nHere are your options:')
                print('\nOption a: Bay Bridge')
                print('\nOption b: Golden Gate')
                print('\nOption c: Star Bridge')
                print('\nOption d: Tower Bridge')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[11]:  
                print('\nHere are your options:')
                print('\nOption a: Daily Bulge')
                print('\nOption b: The Press')
                print('\nOption c: Paper Express')
                print('\nOption d: CNN')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[12]:  
                print('\nHere are your options:')
                print('\nOption a: Wade Cunningham')
                print('\nOption b: Jerry Cane')
                print('\nOption c: Wade Wilsom')
                print('\nOption d: Thomas Wilson')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[13]:  
                print('\nHere are your options:')
                print('\nOption a: Steven Stark')
                print('\nOption b: Howard Stark')
                print('\nOption c: Terrence Stark')
                print('\nOption d: Cade Stark')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == marvel_questions[14]:  
                print('\nHere are your options:')
                print('\nOption a: Aluminum')
                print('\nOption b: Steel')
                print('\nOption c: Alien Metal')
                print('\nOption d: Vibranium')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            if points_obtained == 15:
                print('Congrats, you have succesfully answered all the questions in this genre!')

            
        retry = input('\nWould you like to play Again? y/n: ') #After the loss of trivia, user input to retry or quit

        if retry == 'y':
            break
        

        elif retry == 'n':
            choice == 'q'
            decision == None
            break
        
    while decision == 'One liners':
        while index <= len(one_liners) - 1:
            current_question = one_liners[index]

            if current_question == one_liners[0]:  
                print('\nHere are your options:')
                print('\nOption a: Spirted')
                print('\nOption b: Golfinger')
                print('\nOption c: ScarFace')
                print('\nOption d: Ted')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[1]:  
                print('\nHere are your options:')
                print('\nOption a: Batman: Dark Night Rises')
                print('\nOption b: The Godfather')
                print('\nOption c: 12 Angry Men')
                print('\nOption d: 300')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[2]:  
                print('\nHere are your options:')
                print('\nOption a: Terminator 2: Judgment Day')
                print('\nOption b: Goodfellas')
                print('\nOption c: Se7en')
                print('\nOption d: Forest Gump')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[3]:  
                print('\nHere are your options:')
                print('\nOption a: Beauty And The Beast')
                print('\nOption b: City of God')
                print('\nOption c: Saving Private Ryan')
                print('\nOption d: King Kong')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[4]:  
                print('\nHere are your options:')
                print('\nOption a: The Sandlot')
                print('\nOption b: The Green Mile')
                print('\nOption c: Life is Beautiful ')
                print('\nOption d: Psycho')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == one_liners[5]:  
                print('\nHere are your options:')
                print('\nOption a: Back To The Future')
                print('\nOption b: The Lion King')
                print('\nOption c: The Wizard of Oz')
                print('\nOption d: Whiplash')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[6]:  
                print('\nHere are your options:')
                print('\nOption a: Harakiri')
                print('\nOption b: Midnight Cowboy')
                print('\nOption c: Modern Times')
                print('\nOption d: Djanjo Unchained')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == one_liners[7]:  
                print('\nHere are your options:')
                print('\nOption a: The Shining')
                print('\nOption b: Sunset Blvd.')
                print('\nOption c: Aliens')
                print('\nOption d: Sausage Party')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[8]:  
                print('\nHere are your options:')
                print('\nOption a: The Intouchables')
                print('\nOption b: Rear Window')
                print('\nOption c: American Beauty')
                print('\nOption d: Jerry Maguire')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == one_liners[9]:  
                print('\nHere are your options:')
                print('\nOption a: Paths to Glory')
                print('\nOption b: A Few Good Men')
                print('\nOption c: Momento')
                print('\nOption d: Joker')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[10]:  
                print('\nHere are your options:')
                print('\nOption a: Your Name')
                print('\nOption b: 3 Idiots')
                print('\nOption c: Coco')
                print('\nOption d: Top Gun')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == one_liners[11]:  
                print('\nHere are your options:')
                print('\nOption a: Snatch')
                print('\nOption b: To Kill A Mockingbird')
                print('\nOption c: Titanic')
                print('\nOption d: Forest Gump')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[12]:  
                print('\nHere are your options:')
                print('\nOption a: The wizard of Oz')
                print('\nOption b: Die Hard')
                print('\nOption c: Taken')
                print('\nOption d: 1917')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[13]:  
                print('\nHere are your options:')
                print('\nOption a: Green Book')
                print('\nOption b: Goodfellas')
                print('\nOption c: The Father')
                print('\nOption d: Dead Poets Society')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[14]:  
                print('\nHere are your options:')
                print('\nOption a: Scarface')
                print('\nOption b: Goodfellas')
                print('\nOption c: Se7en')
                print('\nOption d: Casino')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == one_liners[15]:  
                print('\nHere are your options:')
                print('\nOption a: Terminator 2: Judgment Day')
                print('\nOption b: The Wolf Of Wall Street')
                print('\nOption c: Taken')
                print('\nOption d: Ran')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option c":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            if points_obtained == 16:
                print('Congrats, you have succesfully answered all the questions in this genre!')


        retry = input('\nWould you like to play Again? y/n: ') #After the loss of trivia, user input to retry or quit

        if retry == 'y':
            break
        

        elif retry == 'n':
            choice == 'q'
            decision == None
            break
        

    while decision == 'Action':
        while index <= len(action_questions) - 1:
            current_question = action_questions[index]

            if current_question == action_questions[0]:  
                print('\nHere are your options:')
                print('\nOption a: 9')
                print('\nOption b: 6')
                print('\nOption c: 12')
                print('\nOption d: 10')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[1]:  
                print('\nHere are your options:')
                print('\nOption a: Chnace The Rapper')
                print('\nOption b: Lil Baby')
                print('\nOption c: 12 Mariah Carey')
                print('\nOption d: Billie Elish')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[2]:  
                print('\nHere are your options:')
                print('\nOption a: Bad Boys')
                print('\nOption b: Men In Black')
                print('\nOption c: Madea')
                print('\nOption d: White Chicks')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[3]:  
                print('\nHere are your options:')
                print('\nOption a: Joey Montana')
                print('\nOption b: Tony Montana')
                print('\nOption c: Jerry Price')
                print('\nOption d: Tyler Kong')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[4]:  
                print('\nHere are your options:')
                print('\nOption a: Stephen King')
                print('\nOption b: Mark Twain')
                print('\nOption c: James Joyce ')
                print('\nOption d: William Shakespeare')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == action_questions[5]:  
                print('\nHere are your options:')
                print('\nOption a: Taken')
                print('\nOption b: Shutter Island')
                print('\nOption c: Sudden Impact')
                print('\nOption d: Jurassic Park')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[6]:  
                print('\nHere are your options:')
                print('\nOption a: Blue Pill')
                print('\nOption b: Red Pill')
                
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == action_questions[7]:  
                print('\nHere are your options:')
                print('\nOption a: "Good Luck"')
                print('\nOption b: "Come and get me"')
                print('\nOption c: "Nice Try"')
                print('\nOption d: "Have Fun Trying"')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[8]:  
                print('\nHere are your options:')
                print('\nOption a: His Parrot')
                print('\nOption b: His Cat')
                print('\nOption c: His Goldfish')
                print('\nOption d: His Dog')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == action_questions[9]:  
                print('\nHere are your options:')
                print('\nOption a: JavaScript')
                print('\nOption b: SkyNet')
                print('\nOption c: Matrix')
                print('\nOption d: MetaVerse')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[10]:  
                print('\nHere are your options:')
                print('\nOption a: World War 1')
                print('\nOption b: 3 World War 2')
                print('\nOption c: Spanish-American War')
                print('\nOption d: Vietnam War')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == action_questions[11]:  
                print('\nHere are your options:')
                print('\nOption a: "Raise Hell"')
                print('\nOption b: "Bathe In The Blood Of Our Enemies')
                print('\nOption c: "Dine in Hell"')
                print('\nOption d: "Die For Sparta"')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[12]:  
                print('\nHere are your options:')
                print('\nOption a: Heat')
                print('\nOption b: Movement')
                print('\nOption c: Brain Waves')
                print('\nOption d: Energy')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[13]:  
                print('\nHere are your options:')
                print('\nOption a: The Fast and The Furious')
                print('\nOption b: 2 fast 2 Furious')
                print('\nOption c: Fast 9')
                print('\nOption d: Fast Five')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == action_questions[14]:  
                print('\nHere are your options:')
                print('\nOption a: A new object has been introduced')
                print('\nOption b: The same event has already happened')
                print('\nOption c: The Code has been changed')
                print('\nOption d: The Code is the same')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option c":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            if points_obtained == 15:
                print('Congrats, you have succesfully answered all the questions in this genre!')
            decision = None 

        retry = input('\nWould you like to play Again? y/n: ') #After the loss of trivia, user input to retry or quit

        if retry == 'y':
            break

        elif retry == 'n':
            choice == 'q'
            decision == None
            break


    while decision == 'Comedy':
        while index <= len(comedy_questions) - 1:
            current_question = comedy_questions[index]

            if current_question == comedy_questions[0]:  
                print('\nHere are your options:')
                print('\nOption a: It Happened One Night')
                print('\nOption b: Men In Black')
                print('\nOption c: Scary Movie 2')
                print('\nOption d: Sextuplets')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[1]:  
                print('\nHere are your options:')
                print('\nOption a: $7 Million')
                print('\nOption b: $52 Million')
                print('\nOption c: $29 Million')
                print('\nOption d: $14 Million')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[2]:  
                print('\nHere are your options:')
                print('\nOption a: Nick Cannon')
                print('\nOption b: Steve Harvey')
                print('\nOption c: Ice Cube')
                print('\nOption d: Eddie Murphy')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[3]:  
                print('\nHere are your options:')
                print('\nOption a: Forest Gump')
                print('\nOption b: Dumb And Dumber')
                print('\nOption c: We\'re The Millers')
                print('\nOption d: Tyler Kong')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[4]:  
                print('\nHere are your options:')
                print('\nOption a: Elf')
                print('\nOption b: The Polar Express')
                print('\nOption c: This Christmas')
                print('\nOption d: Spirted')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == comedy_questions[5]:  
                print('\nHere are your options:')
                print('\nOption a: Taken')
                print('\nOption b: Madea')
                print('\nOption c: White Chicks')
                print('\nOption d: Groundhog Day')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[6]:  
                print('\nHere are your options:')
                print('\nOption a: The Brothers')
                print('\nOption b: StepBothers')
                print('\nOption c: Brothers Grim')
                print('\nOption d: Four Brothers')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == comedy_questions[7]:  
                print('\nHere are your options:')
                print('\nOption a: True')
                print('\nOption b: False')
                
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[8]:  
                print('\nHere are your options:')
                print('\nOption a: Sandy')
                print('\nOption b: Providence')
                print('\nOption c: Salt Lake City')
                print('\nOption d: Aspen')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == comedy_questions[9]:  
                print('\nHere are your options:')
                print('\nOption a: Weddings')
                print('\nOption b: Funerals')
                print('\nOption c: Birthdays')
                print('\nOption d: Bar Mitzvahs')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[10]:  
                print('\nHere are your options:')
                print('\nOption a: Milk')
                print('\nOption b: Cookies')
                print('\nOption c: Soda')
                print('\nOption d: Syrup')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == comedy_questions[11]:  
                print('\nHere are your options:')
                print('\nOption a: The BFG')
                print('\nOption b: GooseBumps')
                print('\nOption c: Ghostbusters')
                print('\nOption d: The Goonies')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[12]:  
                print('\nHere are your options:')
                print('\nOption a: South Park')
                print('\nOption b: Family Guy')
                print('\nOption c: American Dad')
                print('\nOption d: Robot Chicken')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[13]:  
                print('\nHere are your options:')
                print('\nOption a: Sam J. Jones')
                print('\nOption b: Joel McHale')
                print('\nOption c: Mark Wahlberg')
                print('\nOption d: Seth McFarlane')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == comedy_questions[14]:  
                print('\nHere are your options:')
                print('\nOption a: Martini')
                print('\nOption b: Red Wine')
                print('\nOption c: Sweet Vermouth')
                print('\nOption d: Fino Sherry')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option c":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            if points_obtained == 15:
                print('Congrats, you have succesfully answered all the questions in this genre!')
                
        
        retry = input('\nWould you like to play Again? y/n: ') #After the loss of trivia, user input to retry or quit

        if retry == 'y':
            break

        elif retry == 'n':
            choice == 'q'
            decision == None
            break


    while decision == 'Horror':
        while index <= len(horror_questions) - 1:
            current_question = horror_questions[index]

            if current_question == horror_questions[0]:  
                print('\nHere are your options:')
                print('\nOption a: The Curse of Frankenstein')
                print('\nOption b: The Thing')
                print('\nOption c: The Exorcist')
                print('\nOption d: Poltergist')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[1]:  
                print('\nHere are your options:')
                print('\nOption a: Tusk')
                print('\nOption b: Black Mass')
                print('\nOption c: A Nightmare On Elm Street')
                print('\nOption d: Secret Window')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[2]:  
                print('\nHere are your options:')
                print('\nOption a: Black')
                print('\nOption b: White')
                print('\nOption c: Blue')
                print('\nOption d: Red')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[3]:  
                print('\nHere are your options:')
                print('\nOption a: "Here\'s Johnny"')
                print('\nOption b: "I See Dead People"')
                print('\nOption c: "Be Afraid"')
                print('\nOption d: "The\'re Here"')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[4]:  
                print('\nHere are your options:')
                print('\nOption a: 9')
                print('\nOption b: 5')
                print('\nOption c: 12')
                print('\nOption d: 7')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == horror_questions[5]:  
                print('\nHere are your options:')
                print('\nOption a: Black')
                print('\nOption b: Orange')
                print('\nOption c: Red')
                print('\nOption d: Yellow')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[6]:  
                print('\nHere are your options:')
                print('\nOption a: Halloween')
                print('\nOption b: Scream')
                print('\nOption c: The Ninth Gate')
                print('\nOption d: Run')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == horror_questions[7]:  
                print('\nHere are your options:')
                print('\nOption a: Us')
                print('\nOption b: Halloween')
                print('\nOption c: The Purge')
                print('\nOption d: Happy Death Day')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[8]:  
                print('\nHere are your options:')
                print('\nOption a: Get Out')
                print('\nOption b: The boy')
                print('\nOption c: Nightmare On Elm Street')
                print('\nOption d: Scream')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == horror_questions[9]:  
                print('\nHere are your options:')
                print('\nOption a: Annabelle')
                print('\nOption b: The Conjuring')
                print('\nOption c: The Nun')
                print('\nOption d: Child\'s Play')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[10]:  
                print('\nHere are your options:')
                print('\nOption a: Sledge Hammer')
                print('\nOption b: Axe')
                print('\nOption c: Hook')
                print('\nOption d: Chainsaw')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == horror_questions[11]:  
                print('\nHere are your options:')
                print('\nOption a: 13')
                print('\nOption b: 10')
                print('\nOption c: 12')
                print('\nOption d: 15')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[12]:  
                print('\nHere are your options:')
                print('\nOption a: Yautja')
                print('\nOption b: Banshee')
                print('\nOption c: Chimera')
                print('\nOption d: Chupacabra')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[13]:  
                print('\nHere are your options:')
                print('\nOption a: Caleb Ray')
                print('\nOption b: Chuck Ray')
                print('\nOption c: Colton Ray')
                print('\nOption d: Charles Ray')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == horror_questions[14]:  
                print('\nHere are your options:')
                print('\nOption a: "Don\'t Go Alone"')
                print('\nOption b: "Never Say you\'ll be back"')
                print('\nOption c: "Dont Have Sex"')
                print('\nOption d: "Never trust Your Love Interest"')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option c":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            if points_obtained == 15:
                print('Congrats, you have succesfully answered all the questions in this genre!')
            

        retry = input('\nWould you like to play Again? y/n: ') #After the loss of trivia, user input to retry or quit

        if retry == 'y':
            break

        elif retry == 'n':
            choice == 'q'
            decision == None
            break

    while decision == 'General knowledge':
        while index <= len(general_questions) - 1:
            current_question = general_questions[index]

            if current_question == general_questions[0]:  
                print('\nHere are your options:')
                print('\nOption a: World Wide Web')
                print('\nOption b: Wa Wa Wubsy')
                print('\nOption c: Wawa')
                print('\nOption d: "Wait Waldo Wait"')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[1]:  
                print('\nHere are your options:')
                print('\nOption a: 55 Meters')
                print('\nOption b: 30 Meter')
                print('\nOption c: 50 Meters')
                print('\nOption d: 70 Meters')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[2]:  
                print('\nHere are your options:')
                print('\nOption a: Fear Of Rabbits')
                print('\nOption b: Fear Of Cats')
                print('\nOption c: Fear Of Holes')
                print('\nOption d: Fear Of Dogs')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[3]:  
                print('\nHere are your options:')
                print('\nOption a: 27')
                print('\nOption b: 12')
                print('\nOption c: 59')
                print('\nOption d: 42')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[4]:  
                print('\nHere are your options:')
                print('\nOption a: Horse')
                print('\nOption b: Bull')
                print('\nOption c: Cheetah')
                print('\nOption d: Camel')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == general_questions[5]:  
                print('\nHere are your options:')
                print('\nOption a: Indian Ocean')
                print('\nOption b: Atlantic Ocean')
                print('\nOption c: Pacific Ocean')
                print('\nOption d: Antarctic Ocean')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[6]:  
                print('\nHere are your options:')
                print('\nOption a: Harriet Quimby')
                print('\nOption b: Amelia Earhart')
                print('\nOption c: Amy Johnson')
                print('\nOption d: Bessie Coleman')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == general_questions[7]:  
                print('\nHere are your options:')
                print('\nOption a: Japan')
                print('\nOption b: Switzerland')
                print('\nOption c: United States')
                print('\nOption d: Germany')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[8]:  
                print('\nHere are your options:')
                print('\nOption a: Blue')
                print('\nOption b: Red')
                print('\nOption c: Green')
                print('\nOption d: Brown')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == general_questions[9]:  
                print('\nHere are your options:')
                print('\nOption a: Sprite')
                print('\nOption b: Coca Cola')
                print('\nOption c: Fanta')
                print('\nOption d: Ginger Ale')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[10]:  
                print('\nHere are your options:')
                print('\nOption a: Dried Fruit')
                print('\nOption b: Beans')
                print('\nOption c: Rice')
                print('\nOption d: Honey')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == general_questions[11]:  
                print('\nHere are your options:')
                print('\nOption a: Germany')
                print('\nOption b: Japan')
                print('\nOption c: China')
                print('\nOption d: United States')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[12]:  
                print('\nHere are your options:')
                print('\nOption a: Asia')
                print('\nOption b: North America')
                print('\nOption c: Europe')
                print('\nOption d: Africa')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[13]:  
                print('\nHere are your options:')
                print('\nOption a: Utah')
                print('\nOption b: Texas')
                print('\nOption c: Washington D.C')
                print('\nOption d: Nevada')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[14]:  
                print('\nHere are your options:')
                print('\nOption a: Corn')
                print('\nOption b: Seafood Boil')
                print('\nOption c: Fried Chicken')
                print('\nOption d: Gumbo')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option c":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == general_questions[15]:  
                print('\nHere are your options:')
                print('\nOption a: "King Of The Court"')
                print('\nOption b: "A Free For All"')
                print('\nOption c: A TriDuel')
                print('\nOption d: A Truel')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            if points_obtained == 16:
                print('Congrats, you have succesfully answered all the questions in this genre!')
            

        retry = input('\nWould you like to play Again? y/n: ') #After the loss of trivia, user input to retry or quit

        if retry == 'y':
            break

        elif retry == 'n':
            choice == 'q'
            decision == None
            break


    while decision == 'Sports':
        while index <= len(sports_questions) - 1:
            current_question = sports_questions[index]

            if current_question == sports_questions[0]:  
                print('\nHere are your options:')
                print('\nOption a: 18 Inches')
                print('\nOption b: 21 Inches')
                print('\nOption c: 16 Inches')
                print('\nOption d: 25 Inches')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[1]:  
                print('\nHere are your options:')
                print('\nOption a: 12 Years')
                print('\nOption b: 6 Years')
                print('\nOption c: 4 Years')
                print('\nOption d: 8 Years')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[2]:  
                print('\nHere are your options:')
                print('\nOption a: Hockey')
                print('\nOption b: Basketball')
                print('\nOption c: Football')
                print('\nOption d: Soccer')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[3]:  
                print('\nHere are your options:')
                print('\nOption a: Venus Williams')
                print('\nOption b: Serena Williams')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[4]:  
                print('\nHere are your options:')
                print('\nOption a: Liechtenstein')
                print('\nOption b: Belize')
                print('\nOption c: Sierra Leone')
                print('\nOption d: Turkmenistan')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == sports_questions[5]:  
                print('\nHere are your options:')
                print('\nOption a: 15')
                print('\nOption b: 30')
                print('\nOption c: 18')
                print('\nOption d: 25')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[6]:  
                print('\nHere are your options:')
                print('\nOption a: 24.9')
                print('\nOption b: 26.2')
                print('\nOption c: 30.1')
                print('\nOption d: 26.7')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == sports_questions[7]:  
                print('\nHere are your options:')
                print('\nOption a: Darts')
                print('\nOption b: Indianapolis 500')
                print('\nOption c: Tennis')
                print('\nOption d: Handball')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[8]:  
                print('\nHere are your options:')
                print('\nOption a: 18 Years Old')
                print('\nOption b: 22 Years Old')
                print('\nOption c: 19 Years Old')
                print('\nOption d: 21 Years Old')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == sports_questions[9]:  
                print('\nHere are your options:')
                print('\nOption a: 5 Games')
                print('\nOption b: 3 Games')
                print('\nOption c: 7 Games')
                print('\nOption d: 2 Games')
                answer = input('\nEnter your answer: ')

                if answer == 'option b' or answer == 'Option b' or answer == "Option B":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[10]:  
                print('\nHere are your options:')
                print('\nOption a: Toronto Huskies')
                print('\nOption b: Seattle SuperSonics ')
                print('\nOption c: Boston Celtics')
                print('\nOption d: New York Knickerbockers')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1
            
            elif current_question == sports_questions[11]:  
                print('\nHere are your options:')
                print('\nOption a: Ghana')
                print('\nOption b: Senegal')
                print('\nOption c: Egypt')
                print('\nOption d: Cameroon')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option C":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[12]:  
                print('\nHere are your options:')
                print('\nOption a: 1900, Tennis')
                print('\nOption b: 1896, Tennis')
                print('\nOption c: 1900, Golf')
                print('\nOption d: 1909, Soccer')
                answer = input('\nEnter your answer: ')

                if answer == 'option a' or answer == 'Option a' or answer == "Option A":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[13]:  
                print('\nHere are your options:')
                print('\nOption a: Badminton')
                print('\nOption b: Bowling')
                print('\nOption c: Golf')
                print('\nOption d: Tennis')
                answer = input('\nEnter your answer: ')

                if answer == 'option d' or answer == 'Option d' or answer == "Option D":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            elif current_question == sports_questions[14]:  
                print('\nHere are your options:')
                print('\nOption a: Albania')
                print('\nOption b: Greece')
                print('\nOption c: Philippines')
                print('\nOption d: Norway')
                answer = input('\nEnter your answer: ')

                if answer == 'option c' or answer == 'Option c' or answer == "Option c":
                    print('\n',correct_answer)
                    points_obtained += 1
                    index += 1
                else:
                    print('\n',wrong_answer)
                    index += 1

            if points_obtained == 15:
                print('Congrats, you have succesfully answered all the questions in this genre!')
            

        retry = input('\nWould you like to play Again? y/n: ') #After the loss of trivia, user input to retry or quit

        if retry == 'y':
            break

        elif retry == 'n':
            choice == 'q'
            decision == None
            break

    if retry == 'n':
        choice == 'q'
        decision == None
        print('Thank you for playing!')
        print('You got a', int((points_obtained/total_points) * 100),'%!')
        break

   

