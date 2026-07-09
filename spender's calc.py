from tkinter import *


class SpenderCalc:

   def __init__(self, root):

      self.root = root 
      self.root .title('Calculator')
      self.root.geometry('615x630+400+100')
      self.root.configure(bg = 'brown')


      self.Mainframe = Frame(self.root , bd =18, width = 600, height=600, relief=RIDGE, bg = 'green')
      self.Mainframe.grid()
      self.Widgetframe = Frame(self.Mainframe , bd =18, width = 590, height=600, relief=RIDGE, bg = 'brown')
      self.Widgetframe.grid()

      self.lblDisplay = Label(self.Widgetframe, width =30, height=2, bg='white', font =('arial',20,'bold'), anchor='e')
      self.lblDisplay.grid (row =0, column=0, columnspan=4, padx =10, pady =10)




root = Tk()
App = SpenderCalc(root)
root.mainloop()
