# Import tkinter GUI
from tkinter import *

# Define the buttons to function
# def button_func for number and operation buttons to work
def button_func(number):
    global operation
    operation = operation + str(number)
    input_value.set(operation)

# Create the window for the calculator
calcu = Tk()
calcu.title("Calculator - 2023")

# Display the numbers and operation
operation = ""
input_value = StringVar()
output_text = Entry(calcu, font=("helvetica", 30, "bold"), textvariable=input_value, bd=30, insertwidth=3,
                    bg="light pink", justify=RIGHT)
output_text.grid(columnspan=4)

# Buttons 7, 8, 9, +
button_7 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="7", command=lambda: button_func(7))
button_7.grid(row=1, column=0)

button_8 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="8", command=lambda: button_func(8))
button_8.grid(row=1, column=1)

button_9 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="9", command=lambda: button_func(9))
button_9.grid(row=1, column=2)

button_plus = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="+", command=lambda: button_func("+"))
button_plus.grid(row=1, column=3)

# Buttons 4, 5, 6, -
button_4 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="4", command=lambda: button_func(4))
button_4.grid(row=2, column=0)

button_5 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="5", command=lambda: button_func(5))
button_5.grid(row=2, column=1)

button_6 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="6", command=lambda: button_func(6))
button_6.grid(row=2, column=2)

button_minus = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="-", command=lambda: button_func("-"))
button_minus.grid(row=2, column=3)

# Buttons 1, 2, 3, *
button_1 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="1", command=lambda: button_func(1))
button_1.grid(row=3, column=0)

button_2 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="2", command=lambda: button_func(2))
button_2.grid(row=3, column=1)

button_3 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="3", command=lambda: button_func(3))
button_3.grid(row=3, column=2)

button_times = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="*", command=lambda: button_func("*"))
button_times.grid(row=3, column=3)

# Buttons C, 0, =, /
button_c = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="C")
button_c.grid(row=4, column=0)

button_0 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="0", command=lambda: button_func(0))
button_0.grid(row=4, column=1)

button_equal = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="=")
button_equal.grid(row=4, column=2)

button_div = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="/", command=lambda: button_func("/"))
button_div.grid(row=4, column=3)

# Create a popup window for another calculation

# Create a popup window to exit the app

# ===== start =====
calcu.mainloop()