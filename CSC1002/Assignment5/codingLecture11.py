from tkinter import *
root=Tk()
root.geometry('200x200')
color=[['yellow','red'],['green','blue']]
labelArray=[]
for i in range(2):
    labelRow=[]
    for j in range(2):
        labelRow.append(Label(root, text='%s,%s'%(i,j), bg=color[i][j]))
        labelRow[j].place(x=j*100,y=i*100,width=100,height=100)
    labelArray.append(labelRow)


##def Click_0_0(event):
##    labelArray[0][0].configure(bg='white')
##
##labelArray[0][0].bind('<Button-1>', Click_0_0)


for i in range(2):
    for j in range(2):
        exec('def Click_%s_%s(event):\n\tlabelArray[%s][%s].configure(bg=\'white\')'%(i,j,i,j))        
        exec('labelArray[%s][%s].bind(\'<Button-1>\',Click_%s_%s)'%(i,j,i,j))

        

def KeyUpPress(event):
    labelArray[0][0].configure(text='Up')
def KeyDownPress(event):
    labelArray[0][0].configure(text='Down')
def KeyLeftPress(event):
    labelArray[0][0].configure(text='Left')
def KeyRightPress(event):
    labelArray[0][0].configure(text='Right')
   
root.bind('<KeyPress-Up>', KeyUpPress)
root.bind('<KeyPress-Down>', KeyDownPress)
root.bind('<KeyPress-Left>', KeyLeftPress)
root.bind('<KeyPress-Right>', KeyRightPress)

def KeyUpRelease(event):
    labelArray[0][0].configure(text='')
def KeyDownRelease(event):
    labelArray[0][0].configure(text='')
def KeyLeftRelease(event):
    labelArray[0][0].configure(text='')
def KeyRightRelease(event):
    labelArray[0][0].configure(text='')
    
root.bind('<KeyRelease-Up>', KeyUpRelease)
root.bind('<KeyRelease-Down>', KeyDownRelease)
root.bind('<KeyRelease-Left>', KeyLeftRelease)
root.bind('<KeyRelease-Right>', KeyRightRelease)

colorIndex=0
def Flash(string):
    global colorIndex
    labelArray[0][1].configure(bg=color[0][colorIndex], text=string)
    colorIndex=1-colorIndex
    root.after(500,Flash,string)

Flash('Hello!')



def ShowImage(event):
    myImage=PhotoImage(file='painting.gif')
    labelArray[1][0].configure(image=myImage)
    labelArray[1][0].photo=myImage
    
labelArray[1][0].bind('<Button-3>',ShowImage)

def DeleteImage(event):
    labelArray[1][0].configure(image='')
    
labelArray[1][0].bind('<Button-2>',DeleteImage)
    
root.mainloop()

