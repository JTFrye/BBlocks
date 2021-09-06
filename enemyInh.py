from statMaker import statColl

print('class is enemyChar(self, name, lvl, hp, mp, strength, agility)')
class enemyChar(statColl):
    def __init__(self, name, lvl, hp, mp, strength, agility):
        super().__init__(name, lvl, hp, mp, strength, agility)



if __name__ == '__main__':
    print('mnr')
    qrewp = enemyChar('Skeley', 2, 20, 12, 10, 10)
