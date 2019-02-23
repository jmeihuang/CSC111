from graphics import *
import random
from time import sleep

def greeting():
    WIDTH = 600
    HEIGHT = 400

    win = GraphWin("Greetings!", WIDTH, HEIGHT)
    bg = Image(Point(WIDTH/2, HEIGHT/2), "bg1.png")
    bg.draw(win)

    greeting = Text(Point(WIDTH/2, HEIGHT/2-100), "Which Smith House are you?")
    greeting.setFace("courier")
    greeting.setSize(36)
    greeting.draw(win)

    choose = Text(Point(WIDTH/2, HEIGHT/2), "Click to choose an avatar"
                  + " to quiz you!")
    choose.setFace("courier")
    choose.setSize(24)
    choose.draw(win)

    dogBox = Rectangle(Point(150,300), Point(250,350))
    dogBox.setFill(color_rgb(255,150,150))
    dogBox.draw(win)
    dog = Text(Point(WIDTH/2-100, HEIGHT/2+125), "Dog?")
    dog.setFace("courier")
    dog.setSize(18)
    dog.draw(win)

    catBox = Rectangle(Point(350,300), Point(450,350))
    catBox.setFill("light blue")
    catBox.draw(win)
    cat = Text(Point(WIDTH/2+100, HEIGHT/2+125), "Cat?")
    cat.setFace("courier")
    cat.setSize(18)
    cat.draw(win)

    
    clickPoint = win.getMouse()
    
    x = True
    animal = ""
    while x:
        if (clickPoint.getX() > 150 and clickPoint.getX() < 250 and
            clickPoint.getY() > 300 and clickPoint.getY() < 350):
            animal = "dog"
            x = False
        if (clickPoint.getX() > 350 and clickPoint.getX() < 450 and
            clickPoint.getY() > 300 and clickPoint.getY() < 350):
            animal = "cat"
            x = False
            
            
    win.close()
    return animal

def graphicChat(win, animal, WIDTH, HEIGHT):
    if animal == "cat":
        avatar = Image(Point(WIDTH/2 - 180, HEIGHT/2 + 50), "cat2.png")
        avatar.draw(win)        
    else:
        avatar = Image(Point(WIDTH/2 - 200, HEIGHT/2 + 50), "dog.png")
        avatar.draw(win)
    bubble = Image(Point(WIDTH/2 + 100, HEIGHT/2 - 50), "bubble.png")
    bubble.draw(win)

    hello = Text(Point(WIDTH/2 + 110, HEIGHT/2- 50), "Hi there!\nI have " +
                 "some\nquestions for you!\nClick here to\ncontinue!") 
    hello.setFace("courier")
    hello.setSize(22)
    hello.draw(win)
    win.getMouse()
    hello.undraw()

    return avatar

    #react(win, animal, WIDTH, HEIGHT)

    #win.getMouse()
    #win.close()

def react(win, animal, WIDTH, HEIGHT, avatar):
    x = random.randint(1,7)
    if x == 1:
        hmm = Text(Point(WIDTH/2 + 110, HEIGHT/2- 50), "Hmmm...")
        hmm.setFace("courier")
        hmm.setSize(24)
        hmm.draw(win)
        avatar.undraw()
        if animal == "dog":
            avatar1 = Image(Point(WIDTH/2 - 200, HEIGHT/2 + 50), "dogtailmove.png")
        else:
            avatar1 = Image(Point(WIDTH/2 - 180, HEIGHT/2 + 50), "cat2tailmove.png")
        avatar1.draw(win)
        sleep(1)
        avatar1.undraw()
        avatar.draw(win)
        return hmm
    elif x == 2:
        interest = Text(Point(WIDTH/2 + 110, HEIGHT/2- 50), "Interesting!")
        interest.setFace("courier")
        interest.setSize(24)
        interest.draw(win)
        avatar.undraw()
        if animal == "dog":
            avatar1 = Image(Point(WIDTH/2 - 200, HEIGHT/2 + 50), "dogtailmove.png")
        else:
            avatar1 = Image(Point(WIDTH/2 - 180, HEIGHT/2 + 50), "cat2tailmove.png")
        avatar1.draw(win)
        sleep(1)
        avatar1.undraw()
        avatar.draw(win)
        return interest
    elif x == 3:
        metoo = Text(Point(WIDTH/2 + 110, HEIGHT/2- 50), "Yeah, me too!")
        metoo.setFace("courier")
        metoo.setSize(24)
        metoo.draw(win)
        avatar.undraw()
        if animal == "dog":
            avatar1 = Image(Point(WIDTH/2 - 200, HEIGHT/2 + 50), "dogtailmove.png")
        else:
            avatar1 = Image(Point(WIDTH/2 - 180, HEIGHT/2 + 50), "cat2tailmove.png")
        avatar1.draw(win)
        sleep(1)
        avatar1.undraw()
        avatar.draw(win)
        return metoo
    elif x == 4:
        idk = Text(Point(WIDTH/2 + 110, HEIGHT/2- 50), "I don't know\nabout that...")
        idk.setFace("courier")
        idk.setSize(24)
        idk.draw(win)
        avatar.undraw()
        if animal == "dog":
            avatar1 = Image(Point(WIDTH/2 - 200, HEIGHT/2 + 50), "dogtailmove.png")
        else:
            avatar1 = Image(Point(WIDTH/2 - 180, HEIGHT/2 + 50), "cat2tailmove.png")
        avatar1.draw(win)
        sleep(1)
        avatar1.undraw()
        avatar.draw(win)
        return idk
    elif x == 5:
        fun = Text(Point(WIDTH/2 + 110, HEIGHT/2- 50), "How fun!")
        fun.setFace("courier")
        fun.setSize(24)
        fun.draw(win)
        avatar.undraw()
        if animal == "dog":
            avatar1 = Image(Point(WIDTH/2 - 200, HEIGHT/2 + 50), "dogtailmove.png")
        else:
            avatar1 = Image(Point(WIDTH/2 - 180, HEIGHT/2 + 50), "cat2tailmove.png")
        avatar1.draw(win)
        sleep(1)
        avatar1.undraw()
        avatar.draw(win)
        return fun
    elif x == 6:
        itb = Text(Point(WIDTH/2 + 110, HEIGHT/2- 50), "It be like that\nsometimes :D")
        itb.setFace("courier")
        itb.setSize(24)
        itb.draw(win)
        avatar.undraw()
        if animal == "dog":
            avatar1 = Image(Point(WIDTH/2 - 200, HEIGHT/2 + 50), "dogtailmove.png")
        else:
            avatar1 = Image(Point(WIDTH/2 - 180, HEIGHT/2 + 50), "cat2tailmove.png")
        avatar1.draw(win)
        sleep(1)
        avatar1.undraw()
        avatar.draw(win)
        return itb
    else:
        cool = Text(Point(WIDTH/2 + 110, HEIGHT/2- 50), "COOL!")
        cool.setFace("courier")
        cool.setSize(24)
        cool.draw(win)
        avatar.undraw() 
        if animal == "dog":
            avatar1 = Image(Point(WIDTH/2 - 200, HEIGHT/2 + 50), "dogtailmove.png")
        else:
            avatar1 = Image(Point(WIDTH/2 - 180, HEIGHT/2 + 50), "cat2tailmove.png")
        avatar1.draw(win)
        sleep(1)
        avatar1.undraw()
        avatar.draw(win)
        return cool
def main():
    WIDTH = 600
    HEIGHT = 400

    animal = greeting()
    win = GraphWin("Your Furry Friend!", WIDTH, HEIGHT)
    graphicChat(win, animal, WIDTH, HEIGHT)

if __name__ == "__main__":
    main()
