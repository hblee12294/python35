from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text = "Hello, world!")
		self.helloLabel.pack()
		self.quitButton = Button(self, text = "Quit")
		self.quitButton.pack()

	def hello(self):
		name = self.nameInput.get() or "world"
		messagebox.showinfo("Message", "Hello, %s" % name)

app = Application()
app.master.title("Hello world")
app.mainloop()