import pickle
#import PickleWrite

pickle_in = open('dict.pickle', 'rb')
newDict = pickle.load(pickle_in)

print(newDict)

pickleClOpen = open('classAll.pick', 'rb')
instObj = pickle.load(pickleClOpen)
pickleClOpen.close()

picklealtin = open('classP.pickle','rb')
secObj = pickle.load(picklealtin)

with open('classP.pickle', 'rb') as infile:
    newObj = pickle.load(infile)

#print(newObj)

#class unPickler(object):
 #   def __init__(self, newObj):
  #      print('instance')
