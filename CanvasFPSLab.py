from tkinter import *
import tkinter
import time

class tkAnimator():
    def __init__(self):
        print('instantiated')

        self.deltaArr = []
        
        #Sets up Canvas, draws line down middle, 
        self.root = tkinter.Tk()

        #Action Button
        self.mahButton = Button(self.root, text = 'Animate',command = self.animator)

        #DeltaT Results
        self.deltaLabel = Label(self.root, text = 'FPS : ')

        #Canvas size etc.
        self.myCanvas = tkinter.Canvas(self.root, bg="grey", height=600, width=1024)

        #Middle Line
        self.line1 = self.myCanvas.create_line(512, 0, 512, 1024, fill="#000000", width=12)

        #Uh, packs stuff
        self.myCanvas.pack()
        self.mahButton.pack()
        self.deltaLabel.pack()

        #self.root.mainloop()

       

    def animator(self):
        
        #control variables for animation loop
        self.frameCount = 0
        self.deltaTotal = 0
        while self.deltaTotal < 1:
            #Runs until FPS determined.
            self.logVal = time.perf_counter()
            self.deltaArr.append(self.logVal)
            self.deltaTotal = self.deltaArr[-1] - self.deltaArr[0]
            #Insert Action code here
            

            
            print(self.frameCount) #This is just to slow the whole thing down till action code is made
            self.frameCount = self.frameCount + 1
        else:

            #Sends label to GUI
            self.deltaLabel.configure(text = 'FPS : ' + str(self.frameCount))
            self.deltaTotal = 0
            #print(self.deltaArr)  #This shows results in case
            self.deltaArr.clear()
            
    def fpsCounter(self):
        print(self.deltaArr[-1] - self.deltaArr[0])
    
if __name__ == '__main__':            
    qobo = tkAnimator()
    #qobo.contractor()
