# Import tkinter GUI
from tkinter import *

# Define the buttons to function
# def button_func for number and operation buttons to work
def button_func(number):
    global operation
    operation = operation + str(number)
    input_value.set(operation)

# def button_clear for the clear button to work
def button_clear():
    global operation
    operation = ""
    input_value.set("")
    output_text.config(fg="black", justify=RIGHT)

# def button_equal to evaluate the input
def button_equal():

    try:
        global operation
        equal = str(eval(operation))
        input_value.set(equal)
        operation = ""
    except ZeroDivisionError:
        output_text.config(fg="red", justify=CENTER)
        error_display = "Math Error"
        input_value.set(error_display)
    except SyntaxError:
        output_text.config(fg="red", justify=CENTER)
        error_display = "Syntax Error"
        input_value.set(error_display)
    
    popup_window()

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
button_c = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="C", command=button_clear)
button_c.grid(row=4, column=0)

button_0 = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="0", command=lambda: button_func(0))
button_0.grid(row=4, column=1)

button_equal = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="=", command=button_equal)
button_equal.grid(row=4, column=2)

button_div = Button(calcu, padx=30, bd=10, fg="black", font=("helvetica", 30, "bold"), text="/", command=lambda: button_func("/"))
button_div.grid(row=4, column=3)

# Create a popup window for another calculation
# def choice(option) for the "yes" and "no" buttons to work
def choice(option):
    if option == "yes":
        button_clear()
        popup.destroy()
    else:
        calcu.destroy()

# def popup_window to open a new window
def popup_window():
    global popup
    popup = Toplevel(calcu)
    popup.title("Calculator - 2023")
    popup.geometry("400x200")
    popup.config(bg="light pink") 
    
    popup_label = Label(popup, text="Would you like to try again?", bg="light pink", fg="white",
                        font=("helvetica", 12, "bold"))
    popup_label.pack(pady=10)

    # yes and no buttons to try again or exit the app
    yes_button = Button(popup, bd=5, fg="black", font=("helvetica", 12, "bold"), text="Yes", command=lambda: choice("yes"))
    yes_button.pack(pady=20)
    
    no_button = Button(popup, bd=5, fg="black", font=("helvetica", 12, "bold"), text="No", command=lambda: choice("no"))
    no_button.pack(pady=15)

# Create a popup window to exit the app

# ===== start =====
calcu.mainloop()