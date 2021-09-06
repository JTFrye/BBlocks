from statMaker import statColl

#Inheritance basics. statColl is class name in other file, imported above
#super is used to get access to init attributes
print('class playerChar(is self, name, lvl, hp, mp, strength, agility)')
class playerChar(statColl):
    def __init__(self, name, lvl, hp, mp, strength, agility):
        super().__init__(name, lvl, hp, mp, strength, agility)

        

    

if __name__ == '__main__':
    print('mnr')
    newp = playerChar('Joyner', 3, 45, 20, 15, 18)
