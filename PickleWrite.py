import pickle

#transfer a dictionary
adict = {1:'adsf',2:'kjoi',3:'iopie'}

pickle_out = open('dict.pickle', 'wb')
pickle.dump(adict, pickle_out)
pickle_out.close()

class classtfer():
    def __init__(self, Var1, Var2, Var3):
        self.Var1 = Var1
        self.Var2 = Var2
        self.Var3 = Var3
        self.inClList = []

    def moreVars(self):
        self.moreVar1 = self.Var1 * self.Var2
        self.moreVar2 = self.Var2 * self.Var3
        self.newVal1 = self.moreVar1 * 2
        self.newVal2 = self.Var3 * 2
        self.inClList.append(self.moreVar1)
        self.inClList.append(self.moreVar2)
        self.inClList.append(self.newVal1)
        self.inClList.append(self.newVal2)
        clSaveFile = open('classAll.pick', 'wb')
        pickle.dump(classtfer, clSaveFile)
        clSaveFile.close()

cCall = classtfer(8, 15, 66)
cCall.moreVars()
print(cCall.inClList)

pickle_obj = pickle.dumps(cCall)
pickle_sv = open(b'classP.pickle', 'wb')
pickle.dump(pickle_obj, pickle_sv)
pickle_sv.close()


'''
if __name__ == '__main__':
    print('main')
    cCall = classtfer(3, 8, 17)
    cCall.moreVars()
    print(cCall.inClList)
    
    pickle_out = open('classP.pickle', 'wb')
    pickle.dumps(cCall, pickle_out)
    pickle_out.close
'''
