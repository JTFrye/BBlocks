notes = '''
p is POSITION. 
v is VECTOR.  
p = (x , y)
v = (x, y)
newPosition p = (px + vx, py + vy)

in 3d.
p = (x,y,z)
v = (x,y,z)
newPosition p = (px +vx, py + vy, pz + vz)

'''

#Tuple implementation likely cleaner
class movementVectors():
    def __init__(self, px = 15, py = 15):
        #Position values
        self.px = px
        self.py = py

    def vectVals(self, vx = 1, vy = 1):
        #vectors
        self.vx = vx
        self.vy = vy
        
    def move(self):
        #Maths!!!
        self.px = self.px + self.vx
        self.py = self.py + self.vy
        #Checks work
        print('x is ', self.px)
        print('y is ', self.py)

if __name__ == '__main__':
    qobo = movementVectors()
    qobo.vectVals()
    #Should print 16, 160
    qobo.move()
    #Changes vec val
    qobo.vectVals(5,6)
    #Should print 21,22
    qobo.move()
    #Proving negative vals work too
    qobo.vectVals(-3, -4)
    #Should print 18,18
    qobo.move()

    
