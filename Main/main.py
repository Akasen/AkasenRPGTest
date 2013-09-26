#RPG?

#randint to be used in the future for random variables
#from random import randint

##Character and NPC classes##
class Character(object):
    def __init__(self, MaxHP, health, strength, dexterity, stamina):
        self.health = health
        self.MaxHP = MaxHP
        self.strength = strength
        self.dexterity = dexterity
        self.stamina = stamina

    #Healing function. If a character is healed,
    #this checks to make sure the character is unable to
    #get mor health than the max Health
    def heal(self, amount):
        if self.health + amount >= int(self.MaxHP):
            self.health = int(self.MaxHP)
        else:
            self.health = int(self.health) + amount
        print "Your health is now " +str(self.health)

###Player Class###
class Player(Character):
    def __init__(self, MaxHP, health, strength, dexterity, stamina, level, experience):
        Character.__init__(self, MaxHP, health, strength, dexterity, stamina)
        self.level = level
        self.experience = experience

    def attack(self):
        damage = self.strength/2 + 1
        print damage
        return damage

    
    #def exp_gain(self):
    #    if experience >= expThresh:
            #Player Levels up... uuuuuh
    
    def show_stats(self):
        print "Player Level is " +str(self.level)
        print "Player HP is " +str(self.health)
        print "Player Strength is " +str(self.strength)
        print "Player Dexterity is " +str(self.dexterity)
        print "Player Stamina is " +str(self.stamina)

###ENEMY CLASS###                                                        
class Enemy(Character):
    def __init__(self, MaxHP, health, strength, dexterity, stamina):
        Character.__init__(self, MaxHP, health, strength, dexterity, stamina)
        

###ITEM CLASS###
class Item(object):
    def __init__(self, itemtype):
        self.itemtype = itemtype

class Potion(Item):
    def __init(self, itemtype):
        Item.__init__(self, itemtype)
        
    def use_heal(self):
        PC.heal(2)

##Gameplay... I think 

PC = Player(10, 10, 18, 18, 18, 1, 0)

def heal(x):
    PC.heal(1)
    
def hurt(x):
    PC.heal(-1)    

Commands = {"Stats" :   Player.show_stats,
            "Test"  :   "Testing",
            "Attack" :  Player.attack,
            "TestHeal" :    heal,
            "TestHurt" :    hurt
            }
#While loop that takes in commands
#From Balducci Source.    
while PC.health > 0:
    line = raw_input(">> ")
    args = line.split()
    if len(line) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                Commands[c](PC)
                commandFound = True
                break
        if not commandFound:
            print "No such term"
    
##Main Loop##
#def