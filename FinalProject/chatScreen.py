#after the avatar will show up on the screen, questions will generate randomly
import random
from graphics import *
import graphicScreen
from time import sleep

#chat function to initiate quiz
def chat(win, animal, WIDTH, HEIGHT, avatar):

    #list of questions to ask user
    questions = ['How are you feeling today?','What do you do in your free time?',
                 "What would your dream house be like?", 'Which one of these would you like for a pet?',
                 'Which one of these things bothers you the most?',
                 'Which one of these foods do you want to eat right now?',
                 'If you had to change your name to one of these, which one would you choose?',
                 'Which one of these super powers would you want?',
                 'Pick a color',"Where do you like to study?",]
    #List of houses in their area
    lowerElm = ['Duckett/Chase', 'Albright', 'Baldwin'] #a
    upperElm = ['Capen', 'Lamont', 'Northrop-Gillett', 'Talbot'] #b
    centerC = ['Chapin', 'Haven-Wesley', 'Cutter/Ziskind', 'Park', 'Sessions'] #c
    eastQuad = ['Cushing', 'Emerson', 'Jordan', 'King', 'Scales'] #d
    westQuad = ['Comstock', 'Gardiner', 'Morrow', 'Wilder', 'Wilson'] #e
    greenStreet = ['Hubbard', 'Lawrence', 'Morris', 'Tyler'] #f

    #counter for houses
    counterLower = 0
    counterUpper = 0
    countercenterC = 0
    counterEast = 0
    counterWest = 0
    counterGreen = 0
 
    #while loop to initiate questions
    ask = "yes"
    while ask == "yes":
        rand = random.randint(0,len(questions)-1)
        out = questions[rand]
        print(out)

        valid = True
        while valid:    #another while loop for questions and to make sure that user enters the correct input
            if out == "How are you feeling today?":
                print("a. Great!")
                print("b. :/")
                print("c. Tired...")
                print("d. Feeling fine")
                print("e. LSJFSLDKJFKLF")
                print("f. Okay...")
            elif out == "What do you do in your free time?":
                print("a. Read books")
                print("b. What is free time???")
                print("c. Hang out with friends")
                print("d. Listen to music :DD")
                print("e. PARTY!!!!!!!!!!")
                print("f. Sleep... zzz...")
            elif out == "What would your dream house be like?":
                print("a. A house nice and homey")
                print("b. A brick house in a suburban area")
                print("c. Something modern and close to everything")
                print("d. A nice house near the city but not in the city")
                print("e. A house in a secluded place with a lot of people")
                print("f. A small house near a library and shops where I can study")
            elif out == "Which one of these would you like for a pet?":
                print("a. Alpaca")
                print("b. Cat")
                print("c. Sugar glider")
                print("d. Dog")
                print("e. Fish")
                print("f. I don't want a pet")
            elif out == "Which one of these things bothers you the most?":
                print("a. When people don't use headphones in public spaces")
                print("b. When people don't clean up after themselves")
                print("c. When the dining halls get overcrowded")
                print("d. People making the whole house smell like weed")
                print("e. People partying downstairs")
                print("f. People chewing loudly")
            elif out == "Which one of these foods do you want to eat right now?":
                print("a. Steak Fries")
                print("b. Mac and Cheese")
                print("c. Vegan Mediterranean Burgers")
                print("d. Coffee Oreo Ice Cream")
                print("e. Beef Bulgogi")
                print("f. BBQ Tempeh")
            elif out == "If you had to change your name to one of these, which one would you choose?":
                print("a. Jordyn")
                print("b. Rocket")
                print("c. Pineapple")
                print("d. Avocado")
                print("e. Coach")
                print("f. Blue")
            elif out == "Which one of these super powers would you want?":
                print("a. Telekenesis")
                print("b. Make money magically appear $$$")
                print("c. Read minds")
                print("d. Teleportation")
                print("e. Bending matter")
                print("f. Healing!")
            elif out == "Pick a color":
                print("a. Pomegranate red")
                print("b. Sky blue")
                print("c. Sunset orange")
                print("d. Dandelion yellow")
                print("e. Black")
                print("f. Lime green")
            elif out == "Where do you like to study?":
                print("a. Hillyer Art Museum")
                print("b. Young Library")
                print("c. In the campus center")
                print("d. In the dining hall or my room")
                print("e. I don't study LOL")
                print("f. Josten Library")
            
            useranswer = input("Type your answer (a, b, c, d, e, or f): ") #user inputs answer, and that letter is associated with a certain house; that houses's counter shows up
            if useranswer == "a":
                counterLower += 1
                valid = False
                questions.remove(out)
            elif useranswer == "b":
                counterUpper += 1
                valid = False
                questions.remove(out)
            elif useranswer == "c":
                countercenterC += 1
                valid = False
                questions.remove(out)
            elif useranswer == "d":
                counterEast += 1
                valid = False
                questions.remove(out)
            elif useranswer == "e":
                counterWest += 1
                valid = False
                questions.remove(out)
            elif useranswer == "f":
                counterGreen += 1
                valid = False
                questions.remove(out)
            else: #if user inputs something other than a,b,c,d,e,f, they have to try again
                print("Please type a, b, c, d, e, or f")
            

        #initite avatar's rection
        reaction = graphicScreen.react(win, animal, WIDTH, HEIGHT, avatar) #avatar will react in the window
        sleep(1) #timer for reaction to take place
        reaction.undraw() #undraw the reaction so avatar will go back to original posision
        if len(questions) == 0: #when all questions are asked, user will be given a result
            print("Congrats, you finished the quiz! Here are your results!")

            #compile counters into a list
            countList = [counterLower, counterUpper, countercenterC,
                         counterEast, counterWest, counterGreen]
            #find house with highest counter for their assigned answer
            maxList = max(countList)
            
            #if the counter for one house is the highest, then that is the user's house!
            if maxList == counterLower:
                  houseresult = random.choice(lowerElm)
                  print("Your house is",houseresult.upper()+"!")
            elif maxList == counterUpper:
                  houseresult = random.choice(upperElm)
                  print("Your house is",houseresult.upper()+"!")
            elif maxList == countercenterC:
                  houseresult = random.choice(centerC)
                  print("Your house is",houseresult.upper()+"!")
            elif maxList == counterEast:
                  houseresult = random.choice(eastQuad)
                  print("Your house is",houseresult.upper()+"!")
            elif maxList == counterWest:
                  houseresult = random.choice(westQuad)
                  print("Your house is",houseresult.upper()+"!")
            else:
                  houseresult = random.choice(greenStreet)
                  print("Your house is",houseresult.upper()+"!")
            win.close()
            break
            

def main():
    animal = graphicScreen.greeting() #greeting screen from graphicScreen file will open
    WIDTH = 600
    HEIGHT = 400
    win = GraphWin("Your Furry Friend", WIDTH, HEIGHT) #draw window
    avatar = graphicScreen.graphicChat(win, animal, WIDTH, HEIGHT) #avatar pops up
    
    chat(win, animal, WIDTH, HEIGHT, avatar) #call chat function with avatar

if __name__ == "__main__":
    main()
