from tkinter import *

class Calculator:
  def __init__(self, master):

    frame = Frame(master)
    frame.grid()

    self.buttons = []
    self.keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ".", "=", "/", "-", "*", "+"]
    self.left_col = ["7", "4", "1", "0"]
    self.middle = ["8", "5", "2", "."]
    self.right = ["9", "6", "3", "="]
    self.far_right = ["/", "-", "*", "+"]
    for i in self.keys:
      self.buttons.append(Button(frame, text=str(i)))

    self.screen = Label(frame, text="2 + 3", bg="white", height=2)
    self.screen.grid(row=0, sticky=W)
   
    for button in self.buttons:
        button.config(height=4, width=8)

    for button in self.buttons:
      if button.config("text")[-1] in self.left_col:
        button.grid(row=self.left_col.index(button.config("text")[-1]) + 2, column=0)
      elif button.config("text")[-1] in self.middle:
        button.grid(row=self.middle.index(button.config("text")[-1]) + 2, column=1)
      elif button.config("text")[-1] in self.right:
        button.grid(row=self.right.index(button.config("text")[-1]) + 2, column=2)
      else:
        button.grid(row=self.far_right.index(button.config("text")[-1]) + 2, column=3)

root = Tk()
root.resizable(0, 0)
root.title("Calculator")
calculator = Calculator(root)
root.mainloop()
