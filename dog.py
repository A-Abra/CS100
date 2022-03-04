'''
Anosh Abraham
CS 100 2019 Section 025
HW 11
11/22/19
'''

class Dog:

    species = 'canis familiaris'
    
    def __init__(self,_name,_breed):
        self.name = _name
        self.breed = _breed
        self.tricks = []
        
    def teach(self,trick):
        self.tricks.append(trick)
        print(self.name+' knows '+trick)
        #print(self.name+' knows '+self.tricks[len(self.tricks)-1])
        
    def knows(self,trick):
        if trick in self.tricks:
            print('Yeah, '+self.name+' knows '+trick)
            return True
        else:
            print('No, '+self.name+ ' knows nothing of '+trick)
            return False
