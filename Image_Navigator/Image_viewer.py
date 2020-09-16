"""
GUI to navigate between images
"""
# Import the necessary modules
from tkinter import *
from PIL import ImageTk,Image

# Create a root object
class image_navigator:
	def __init__(self):
		self.root = Tk()
		# Load the necessary images
		img_1 = ImageTk.PhotoImage(Image.open("1.jpeg"))
		img_2 = ImageTk.PhotoImage(Image.open("2.png"))
		img_3 = ImageTk.PhotoImage(Image.open("3.png"))
		img_4 = ImageTk.PhotoImage(Image.open("4.png"))
		img_5 = ImageTk.PhotoImage(Image.open("5.png"))
		self.label = Label(image = img_1)
		self.label.grid(row=0,column = 0,columnspan=3)
		self.image_list_array = {"img_1":img_1,"img_2":img_2,"img_3":img_3,"img_4":img_4,"img_5":img_5}
		self.num = []
		self.i = 0

	# Function to navigate forward
	def forward(self):
		self.i += 1
		self.label.grid_forget()

		if self.i == 0:
			image_num = "img_1"
		elif self.i == 1:
			image_num = "img_2"
		elif self.i == 2:
			image_num = "img_3"
		elif self.i == 3:
			image_num = "img_4"
		elif self.i == 4:
			image_num = "img_5"
		else:
			return
		img = self.image_list_array[image_num]
		self.label = Label(image = img)
		self.label.grid(row=0,column = 0,columnspan=3)
	
	# Function to navigate backward	
	def backward(self):
		self.i -= 1
		self.label.grid_forget()

		if self.i == 0:
			image_num = "img_1"
		elif self.i == 1:
			image_num = "img_2"
		elif self.i == 2:
			image_num = "img_3"
		elif self.i == 3:
			image_num = "img_4"
		elif self.i == 4:
			image_num = "img_5"
		else:
			return
		img = self.image_list_array[image_num]
		self.label = Label(image = img)
		self.label.grid(row=0,column = 0,columnspan=3)
		
def main():
	# Create the object the Class
	obj = image_navigator()
	# Create the button of required size
	button_forward  = Button(obj.root,text=">>",command=obj.forward,padx=40,pady=20)
	button_backward = Button(obj.root,text="<<",command=obj.backward,padx=40,pady=20)
	button_exit     = Button(obj.root,text="Exit",command=obj.root.quit,padx=40,pady=20)

	button_forward.grid(row=1,column = 2)
	button_backward.grid(row=1,column = 0)
	button_exit.grid(row=1,column = 1)

	obj.root.mainloop()

if __name__=="__main__":
	main()

