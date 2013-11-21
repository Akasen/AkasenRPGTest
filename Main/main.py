#randint to be used in the future for random variables
#from random import randint

##Character and NPC classes##
class Character(object):
    def __init__(self, name, MaxHP, health, strength, dexterity, stamina):
        self.name = name
        self.health = health
        self.MaxHP = MaxHP
        self.strength = strength
        self.dexterity = dexterity
        self.stamina = stamina

    #Healing function. If a character is healed,
    #this checks to make sure the character is unable to
    #get mor health than the max Health
    def heal(self, y):
        if self.health < self.MaxHP:
            self.health += y
            print "Healed by %s HP" % y
        else:
            print "You are at full health"
        if self.health > self.MaxHP:
            self.health = self.MaxHP

    def damage(self):
        damage = self.strength/4 + 1
        return damage
###END CHARACTER CLASS###

###Player Class###
class Player(Character):
    def __init__(self, name, MaxHP, health, strength, dexterity, stamina, level, experience):
        Character.__init__(self, name, MaxHP, health, strength, dexterity, stamina)
        self.level = level
        self.experience = experience
    
    #def exp_gain(self):
    #    if experience >= expThresh:
            #Player Levels up... uuuuuh
    ###COMMANDS### 
    
    def cAttack(self, target):
        cDamage = self.damage()
        target.health -= cDamage
        return target.health
    
    ###COMMANDS END###
    
    def show_stats(self):
        print "Player Level is " +str(self.level)
        print "Player HP is " +str(self.health)
        print "Player Strength is " +str(self.strength)
        print "Player Dexterity is " +str(self.dexterity)
        print "Player Stamina is " +str(self.stamina)
###END Player Class###

###ENEMY CLASS###                                                        
class Enemy(Character):
    def __init__(self, name, MaxHP, health, strength, dexterity, stamina):
        Character.__init__(self, name, MaxHP, health, strength, dexterity, stamina)
        

###ITEM CLASS###
class Item(object):
    def __init__(self, itemtype, cost):
        self.itemtype = itemtype
        self.cost = cost

class Potion(Item):
    def __init__(self, itemtype):
        Item.__init__(self, itemtype)
        
    def use_heal(self):
        #PC.heal(2)
        pass
###ITEM CLASS END###

enemies = 0

ED = Enemy(10, 10, 10, 10, 10, 10)
    

class State(object):
    def __init__(self, name, MaxHP, health, strength, dexterity, stamina, level, experience, commands):
        self.player = Player(name, 10, 9, 18, 18, 18, 1, 0,)
        self.commands = commands
        self.quest1 = False
        self.done = False

### State Command ###
def cmdAttack(state):
    ED.health = state.player.cAttack(ED)
    print ED.health

def cmdHeal(state):
    state.player.heal(10)
    
def cmdHurt(state):
    state.player.hurt(1)

def cmdShowStats(state):
    state.player.show_stats()
    
def cmdQuit(state):
    state.done = True

def cmdStore(state):
    state.player.shop()    
### Commands End ###
    


def initState():
    state = State(
    raw_input("What is your name? \n"), 10, 9, 18, 18, 18, 1, 0,
    {"Stats"    :    cmdShowStats,
    "Attack"    :    cmdAttack,
    "TestHeal"  :    cmdHeal,
    "TestHurt"  :    cmdHurt,
    "Quit"      :    cmdQuit
    })
                  
    return state

#Function that takes in player input
#and compars with Commands Dictionary
def player_input(cmds):
    def getCommandStr():
        args = raw_input(">> ").split()
        if args == []:
            return None
        return args[0]
    def commandNotFound(state):
        print "I can't do that right now"
    s = getCommandStr()
    if s in cmds:
        return cmds[s]
    else:
        return commandNotFound
                
            
def gameplay():
    state = initState()
    while not state.done:
        cmd = player_input(state.commands)
        cmd(state)
            
gameplay()