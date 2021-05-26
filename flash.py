# importing libraries 
from tkinter import *
from random import randint

# creating a window
root = Tk()
root.title("Flashcard App")
root.geometry("500x500")
root.iconbitmap("c:/guis/logo.ico")

# Create function to determine add answer correct?

def add_correct(num1,num2):
	# calculate the actual answer
	correct = num1 + num2

	# correct an incorrect message
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct " +   str(num1) + " + " + str(num2) + " = " + str(correct))
	output_answer_incorrect.set("Incorrect " +   str(num1) + " + " + str(num2) + " = " + str(correct) + " not " + add_answer.get())


	if int(add_answer.get()) == correct:
		add_correct_label.config(text=output_answer_correct.get())
	else:
		add_correct_label.config(text=output_answer_incorrect.get())

	# clear  the answer box
	add_answer.delete(0,'end')

	# Generate two new random numbers
	num_1.set(randint(0,100))
	num_2.set(randint(0,50))
	add_flash.config(text = str(num_1.get()) + "+" + str(num_2.get()),font = ("helvetica",32))

# Create our addition function
def add():
	hide_menu_frame()
	add_frame.pack(fill="both",expand=1)

	# creating 2 random numbers
	
	global num_1
	global num_2
	
	# Note: Tkinter supports some variables [BooleanVar(), StringVar(), IntVar(), DoubleVar()]
	#       which are used to manipulate the values of Tkinter widgets.
	#       These variables work like normal variables.  set() and get() methods are used
	#       to set and retrieve the values of these variables.

	num_1 = IntVar()
	num_2 = IntVar() 

	num_1.set(randint(0,100))
	num_2.set(randint(0,50))

	# put our random number onto the screen
	global add_flash
	add_flash = Label(add_frame, text = str(num_1.get()) + "+" + str(num_2.get()),font = ("helvetica",32))
	add_flash.pack(pady=10)

	# Answer entry box
	global add_answer
	add_answer = Entry(add_frame)
	add_answer.pack(pady = 5)

	# Answer button
	add_button = Button(add_frame,text="Anwer", command= lambda:add_correct(num_1.get(),num_2.get()))
	add_button.pack(pady=5)

	# Correct or Incorrect message

	global add_correct_label
	add_correct_label = Label(add_frame, text= "")
	add_correct_label.pack()
	
# Create our substraction function
def substract():
	hide_menu_frame()
	substract_frame.pack(fill="both",expand=1)

# Create our mutiplication 
def multiply():
	hide_menu_frame()
	multiply_frame.pack(fill="both",expand=1)

# Create our division function


# Create function to determine add answer correct for division?

def divide_correct(num1,num2):
	# calculate the actual answer
	correct = num1 / num2

	# correct an incorrect message
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct " +   str(num1) + " / " + str(num2) + " = " + str(correct))
	output_answer_incorrect.set("Incorrect " +   str(num1) + " / " + str(num2) + " = " + str(correct) + " not " + divide_answer.get())


	if float(divide_answer.get()) == correct:
		divide_correct_label.config(text=output_answer_correct.get())
	else:
		divide_correct_label.config(text=output_answer_incorrect.get())

	# clear  the answer box
	divide_answer.delete(0,'end')

	# Generate two new random numbers
	num_1.set(randint(0,100))
	num_2.set(randint(1,50))
	divide_flash.config(text = str(num_1.get()) + "/" + str(num_2.get()),font = ("helvetica",32))

# Create our addition function
def divide():
	hide_menu_frame()
	divide_frame.pack(fill="both",expand=1)

	# creating 2 random numbers
	
	global num_1
	global num_2
	
	# Note: Tkinter supports some variables [BooleanVar(), StringVar(), IntVar(), DoubleVar()]
	#       which are used to manipulate the values of Tkinter widgets.
	#       These variables work like normal variables.  set() and get() methods are used
	#       to set and retrieve the values of these variables.

	num_1 = IntVar()
	num_2 = IntVar() 

	num_1.set(randint(0,100))
	num_2.set(randint(1,50))

	# put our random number onto the screen
	global divide_flash
	divide_flash = Label(divide_frame, text = str(num_1.get()) + "/" + str(num_2.get()),font = ("helvetica",32))
	divide_flash.pack(pady=10)

	# Answer entry box
	global divide_answer
	divide_answer = Entry(divide_frame)
	divide_answer.pack(pady = 5)

	# Answer button
	divide_button = Button(divide_frame,text="Anwer", command= lambda:divide_correct(num_1.get(),num_2.get()))
	divide_button.pack(pady=5)

	# Correct or Incorrect message

	global divide_correct_label
	divide_correct_label = Label(divide_frame, text= "")
	divide_correct_label.pack()

# hide Frame function abd destroy widget
def hide_menu_frame():

	# destroying  the children widget in each frame
	for widget in add_frame.winfo_children():
		widget.destroy()
	for widget in substract_frame.winfo_children():
		widget.destroy()
	for widget in multiply_frame.winfo_children():
		widget.destroy()
	for widget in divide_frame.winfo_children():
		widget.destroy()

	add_frame.pack_forget()
	substract_frame.pack_forget()
	multiply_frame.pack_forget()
	divide_frame.pack_forget()
	start_frame.pack_forget()

# Define Main menu
my_menu = Menu(root)
root.config(menu=my_menu)

#create menu items
math_menu = Menu(my_menu)
my_menu.add_cascade(label="MathCards",menu=math_menu)
math_menu.add_command(label="Add",command=add)
math_menu.add_command(label="Substract",command=substract)
math_menu.add_command(label="Multiply",command=multiply)
math_menu.add_command(label="Divide",command=divide)
math_menu.add_separator()
math_menu.add_command(label="Exit", command=root.quit)

# Create Math Frames
add_frame =Frame(root, width=400, height=400, bg="gray")
substract_frame =Frame(root, width=400, height=400, bg="red")
multiply_frame =Frame(root, width=400, height=400, bg="yellow")
divide_frame =Frame(root, width=400, height=400, bg="green")

# start screen 
start_frame = Frame(root,width=400, height=400 )
start_frame.pack(fill="both",expand=1)
start_label = Label(start_frame,text="Welcome to Math Flashcard!",font =("helvetica",18))
start_label.pack(pady=40)

# Button to flashcards
a_button = Button(start_frame, text="Addition Flashcards",command=add)
a_button.pack()
s_button = Button(start_frame, text="Substraction Flashcards",command=substract)
s_button.pack()
m_button = Button(start_frame, text="mutiplication Flashcards",command=multiply)
m_button.pack()
d_button = Button(start_frame, text="Division Flashcards",command=divide)
d_button.pack()




root.mainloop()
