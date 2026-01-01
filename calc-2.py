import tkinter as tk
from tkinter import messagebox

# Function for calculation
def calculate():
    try:
        x = float(entry_num1.get())
        y = float(entry_num2.get()) if operation_var.get() != "Factorial" else 0
        operation = operation_var.get()

        if operation == "Add(+)":
            result = x + y
        elif operation == "Subtract(-)":
            result = x - y
        elif operation == "Multiply(*)":
            result = x * y
        elif operation == "Divide(/)":
            if y == 0:
                raise ZeroDivisionError
            result = x / y
        elif operation == "Modulus(%)":
            result = x % y
        elif operation == "Exponent(^)":
            result = x ** y
        elif operation == "Factorial(!)":
            y = x
            if x < 0 or not x.is_integer():
                raise ValueError
            result = 1
            for i in range(1, int(x) + 1):
                result *= i
        else:
            result = "Invalid operation ! "

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error ! ", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error ! ", "Division by zero is not allowed.")

# Main GUI Part
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("450x450")
window.resizable(True, True)
tk.Label(window, text="Simple Calculator", font=("Sans", 16, "bold")).pack(pady=10)
tk.Label(window, text="Enter First Number").pack()
entry_num1 = tk.Entry(window)
entry_num1.pack(pady=5)
tk.Label(window, text="Enter Second Number").pack()
entry_num2 = tk.Entry(window)
entry_num2.pack(pady=5)
operation_var = tk.StringVar()
operation_var.set("SELECT")           
tk.Label(window, text="Select Operation\n⬇️", bg="lightblue").pack()
operations = ["Add(+)", "Subtract(-)", "Multiply(*)", "Divide(/)", "Modulus(%)", "Exponent(^)", "Factorial(!)"]
tk.OptionMenu(window, operation_var, *operations).pack(pady=5)
tk.Button(window, text="Calculate", command=calculate, bg="Red").pack(pady=10)
result_label = tk.Label(window, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()
