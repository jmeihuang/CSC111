# --------------------------------------------------------
#        Name: Joyce Huang
#    Filename: slowpokemon.py
#        Date: November 12, 2018
#
# Description: battling pokemon
# References: TA's help: Georgina, Lizzie, Meredith, Anastasia
#             http://textart4u.blogspot.com/2014/04/pokeball-copy-paste-ascii-text-art.html for pokemball
# --------------------------------------------------------

from random import randint
import webbrowser

class Pokemon:
    def __init__(self, name, pokeType):
        self.name = name
        self.pokemon_type = pokeType
        self.max_hp = randint(20,30)
        self.current_hp = self.max_hp
        self.attack_power = randint(5, 15)
        self.defensive_power = randint(5, 15)
        self.fainted = False
        self.revivecounts = 0
    def printStats(self):
        print("Pokemon name:",self.name)
        print("Type:",self.pokemon_type)
        print("Max HP:",self.max_hp)
        print("Current HP:",self.current_hp)
        print("Attack Power:",self.attack_power)
        print("Defense Power:",self.defensive_power)
    def defendStrong(self): #when a pokemon is battling a stronger pokemon, the amound of defensive power it will subtract is greater
        if self.fainted == False:
            self.current_hp -= int(self.defensive_power*1.5)
            if (self.current_hp <= 0):
                self.current_hp = 0
                self.fainted = True
    def defendWeak(self): #hp decreases less when a pokemon is defending against weaker pokemon
        if self.fainted == False:
            self.current_hp -= (self.defensive_power//2)
            if (self.current_hp <= 0):
                self.current_hp = 0
                self.fainted = True
    def defend(self): #called when same pokemon are battling each other
        if self.fainted == False:
            self.current_hp -= self.defensive_power
            if (self.current_hp <= 0):
                self.current_hp = 0
                self.fainted = True
    def attack(self, opponent):
        opponent.defend()
    def revive(self):
        if (self.current_hp <= 0) and (self.revivecounts >= 2):
            self.current_hp = 0
            print("... OH NO... you are out of revives... Here are the final battle stats:")
            print(" ")
        elif (self.current_hp <= 0) and (self.revivecounts < 2):
            self.current_hp = self.max_hp//2
            self.revivecounts += 1
            self.fainted = False

def battle(PM1, PM2, turn):
    turn = 1
    while PM1.fainted == False and PM2.fainted == False:
        if (turn == 1):
            PM1.attack(PM2) #pokemon 1 attacks pokemon 2
            PM2.printStats() #after pokemon 2 defends, their stats will be printed
            print("")
            turn = 2 #switch turns!
        else:
            PM2.attack(PM1) #pokemon 2 attacks pokemon 1
            PM1.printStats() #after pokemon 1 defends, their stats will be printed
            print(" "*25)
            turn = 1 #switch back to pokemon 1
        #Revive
        if (PM1.fainted == True) or (PM2.fainted == True):
            askRevive = input("Do you want to revive? Choose Y or N: ")
            print(" "*25)
            print("Here are the current stats...")
            if (askRevive.upper() == "Y"):
                PM1.revive()
                PM2.revive()
                PM1.printStats()
                print("")
                PM2.printStats()
                print(" "*25)
                print("**********continue!**********")
                print(" "*25)
            else:
                PM1.printStats()
                print(" ")
                PM2.printStats()
                break

class Piplup(Pokemon):
    def __init__(self, name, pokeType):
        Pokemon.__init__(self, name, pokeType)
        self.pokemon_type = "WATER"
    def attack(self, opponent):
        if (opponent.pokemon_type == "FIRE"):
            print("Water is super effective against fire!")
            opponent.defendStrong() #fire is defending against stronger pokemon (water)
        elif (opponent.pokemon_type == "GRASS"):
            print("Water isn't effective against grass")
            opponent.defendWeak() #grass is defending against weaker pokemon (water)
        else:
            opponent.defend()

class Chimchar(Pokemon):
    def __init__(self, name, pokeType):
        Pokemon.__init__(self, name, pokeType)
        self.pokemon_type = "FIRE"
    def attack(self, opponent):
        if (opponent.pokemon_type == "GRASS"):
            print("Fire is super effective against grass!")
            opponent.defendStrong() #grass is defending against a stronger pokemon (fire)
        elif (opponent.pokemon_type == "WATER"):
            print("Fire isn't effective against water")
            opponent.defendWeak() #water is defending against a weaker pokemon (fire)
        else:
            opponent.defend()

class Turtwig(Pokemon):
    def __init__(self, name, pokeType):
        Pokemon.__init__(self, name, pokeType)
        self.pokemon_type = "GRASS"
    def attack(self, opponent):
        if (opponent.pokemon_type == "WATER"):
            print("Grass is super effective against water!")
            opponent.defendStrong() #water is defending against a stronger pokemon (grass)
        elif (opponent.pokemon_type == "FIRE"):
            print("Grass isn't effective against fire")
            opponent.defendWeak() #fire is defending against a weaker pokemon (grass)
        else:
            opponent.defend()

def main():
    print("""
────────▄██████████████▄────────
─────▄███▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▄─────
────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────
───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───
──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──
─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─
██▓▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓██░░░░░░░░██▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓██░░██████░░██▓▓▓▓▓▓▓██
███████████░░██████░░███████████
██░░░░░░░██░░██████░░██░░░░░░░██
██░░░░░░░░██░░░░░░░░██░░░░░░░░██
██░░░░░░░░░██████████░░░░░░░░░██
─██░░░░░░░░░░░░░░░░░░░░░░░░░░██─
──██░░░░░░░░░░░░░░░░░░░░░░░░██──
───██░░░░░░░░░░░░░░░░░░░░░░██───
────███░░░░░░░░░░░░░░░░░░███────
─────▀███░░░░░░░░░░░░░░███▀─────
────────▀██████████████▀────────
                                """)

    pm_list = ['PIPLUP', 'CHIMCHAR', 'TURTWIG'] #pokemon list to choose from

    #enter Pokemon 1 info
    Pokemon1 = input("Enter Pokemon 1 (Piplup, Chimchar, Turtwig): ")
    Pokemon1type = input("Enter Pokemon 1 type: ")
    if Pokemon1.upper() == pm_list[0]:
        PM1 = Piplup(Pokemon1, Pokemon1type)
        PM1.printStats()
    elif Pokemon1.upper() == pm_list[1]:
        PM1 = Chimchar(Pokemon1, Pokemon1type)
        PM1.printStats()
    elif Pokemon1.upper() == pm_list[2]:
        PM1 = Turtwig(Pokemon1, Pokemon1type)
        PM1.printStats()
    print("")
    
    #enter Pokemon 2 info
    Pokemon2 = input("Enter Pokemon 2 (Piplup, Chimchar, Turtwig): ")
    Pokemon2type = input("Enter Pokemon 2 type: ")
    if Pokemon2.upper() == pm_list[0]:
        PM2 = Piplup(Pokemon2, Pokemon2type)
        PM2.printStats()
    elif Pokemon2.upper() == pm_list[1]:
        PM2 = Chimchar(Pokemon2, Pokemon2type)
        PM2.printStats()
    elif Pokemon2.upper() == pm_list[2]:
        PM2 = Turtwig(Pokemon2, Pokemon2type)
        PM2.printStats()
    print(" ")

    askMusic = input("Would you like some music? Y or N: ")
    if (askMusic.upper() == "Y"):
        webbrowser.open('https://www.youtube.com/watch?v=7vpe_p9awTI')
    
    print("Time to battle!!!", Pokemon1, "attacks first!")
    print("-"*25)

    #BATTLE!!!
    battle(PM1, PM2, 1)
    print(" ")
    if (PM1.fainted == True): #after battle check if pokemon 1 fainted
        print("Congratulations", Pokemon2+"! You won the battle!")
    if (PM2.fainted == True): #after battle check if pokemon 2 fainted
        print("Congratualtions", Pokemon1+"! You won the battle!")

if __name__ == "__main__":
    main()
