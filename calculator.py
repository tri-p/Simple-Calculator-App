# Import tkinter GUI
from tkinter import *

# Define the buttons to function

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

# Buttons 4, 5, 6, -

# Buttons 1, 2, 3, *

# Buttons C, 0, =, /

# Create a popup window for another calculation

# Create a popup window to exit the app

# ===== start =====
calcu.mainloop()