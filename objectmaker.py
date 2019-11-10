class character:
    def __init__(self, arghealth, argattack, argdefense, argdescription,):
        self.health = arghealth
        self.attack = argattack
        self.defense = argdefense
        self.description = argdescription



#objects that I'm instantiating 
human = character("100", "10", "5", "A human is a fragile character with low individual defense and attack stats, relies on a large population and survives using unique methods as they have the best intelligence in the game.")
cat = character ("35", "5", "300", "the housecat is super fast and nimble so it can easily run from its enemies, and can hit them with light attacks if neccessary.")   



#use .__dict__ to look at the attributes of the object at hand in dictionary form
#or use object.attribute to be more specific

def rendercharacter(self):
    print (self.__dict__)

#prints stuff to terminal





#this function call takes two arguments which are both objects that have been instantiated.
#it prints some stuff to the terminal

rendercharacter(human)















