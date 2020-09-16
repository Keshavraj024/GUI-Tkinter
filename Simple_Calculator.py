"""
GUI for Simple Mathematical Operations
"""
# Import the necessary modules
from tkinter import *
from PIL import ImageTk,Image

class simple_calculator(object):
	def __init__(self):
		self.root = Tk()			 #Create the window
		self.root.title("Calculator")#Add the title
		#Number input from the user
		self.num_entry = Entry(self.root,width=50,borderwidth=10)
		self.num_entry.grid(columnspan=3,row=0,column=0,padx=10,pady=10)

	def click(self,number):
		# Retrieve the number
		self.num = self.num_entry.get()
		self.num_entry.delete(0,END)
		self.num_entry.insert(0,str(self.num)+str(number))

	def operations(self,op): 
		# Specify the operation to be carried out
		self.operation = op
		self.first_num = self.num_entry.get()
		self.num_entry.delete(0,END)

	def equal(self):
		self.second_num = self.num_entry.get()
		self.num_entry.delete(0,END)
		# Carry out the operation
		if self.operation == "+":
			result = int(self.first_num) + int(self.second_num)
		if self.operation == "-":
			result = int(self.first_num) - int(self.second_num)
		if self.operation == "*":
			result = int(self.first_num) * int(self.second_num)
		if self.operation == "/":
			result = int(self.first_num) / int(self.second_num)
		self.num_entry.insert(0,result)

	def clear(self):
		# Clear the entry
		self.num_entry.delete(0,END)

def main():
	obj = simple_calculator()
	#Create the buttons
	button_1 = Button(obj.root,text="1",command=lambda:obj.click(1),padx=40,pady=20)
	button_2 = Button(obj.root,text="2",command=lambda:obj.click(2),padx=40,pady=20)
	button_3 = Button(obj.root,text="3",command=lambda:obj.click(3),padx=40,pady=20)

	button_4 = Button(obj.root,text="4",command=lambda:obj.click(4),padx=40,pady=20)
	button_5 = Button(obj.root,text="5",command=lambda:obj.click(5),padx=40,pady=20)
	button_6 = Button(obj.root,text="6",command=lambda:obj.click(6),padx=40,pady=20)

	button_7 = Button(obj.root,text="7",command=lambda:obj.click(7),padx=40,pady=20)
	button_8 = Button(obj.root,text="8",command=lambda:obj.click(8),padx=40,pady=20)
	button_9 = Button(obj.root,text="9",command=lambda:obj.click(9),padx=40,pady=20)

	button_0 = Button(obj.root,text="0",command=lambda:obj.click(0),padx=40,pady=20)

	button_plus = Button(obj.root,text="+",padx=40,pady=20,command=lambda:obj.operations("+"))
	button_sub = Button(obj.root,text="-",padx=40,pady=20,command=lambda:obj.operations("-"))
	button_mul = Button(obj.root,text="*",padx=40,pady=20,command=lambda:obj.operations("*"))
	button_div = Button(obj.root,text="/",padx=40,pady=20,command=lambda:obj.operations("/"))

	button_clear = Button(obj.root,text="Clear",command = obj.clear,padx=40,pady=20)
	button_equal = Button(obj.root,text="=",padx=40,pady=20,command=obj.equal)
	#Exits the entire program
	button_exit = Button(obj.root,text="exit",padx=40,pady=20,command=obj.root.quit)

	#Where to place the created buttons
	button_1.grid(row=3,column=0)
	button_2.grid(row=3,column=1)
	button_3.grid(row=3,column=2)

	button_4.grid(row=2,column=0)
	button_5.grid(row=2,column=1)
	button_6.grid(row=2,column=2)


	button_7.grid(row=1,column=0)
	button_8.grid(row=1,column=1)
	button_9.grid(row=1,column=2)

	button_0.grid(row=4,column=0)

	button_plus.grid(row=4,column=1)
	button_equal.grid(row=4,column=2)
	button_sub.grid(row=5,column=0)
	button_mul.grid(row=5,column=1)
	button_div.grid(row=5,column=2)

	button_clear.grid(row=6,column=0)
	button_exit.grid(row=6,column=1)
	obj.root.mainloop()

if __name__ == "__main__":
	main()

