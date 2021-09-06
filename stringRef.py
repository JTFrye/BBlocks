print('String Beaker')

daWord = 'theBirdistheWordBIRD BIRD BIRD BIRB IS DA WORB'
slicer = 2

#prints individual characters
for x in daWord:
    print(x)

for x in daWord:
    pass    

#This gives index Values
for x in range(len(daWord)):
    print(x)

#Good ole Sliding window
for x in range(len(daWord)):
    print(daWord[x:x+3])

#Print range of numbers (start, stop, step)
for x in range(25):
    print(x)

#Backward print
print('start Backwards')
for x in reversed(range(25)):
    print(x)

#Range Stepper
print('steps of three')
for x in range(0,50,3):
    print(x)
