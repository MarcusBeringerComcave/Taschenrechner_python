import tkinter as tk

def calculate():
    first_num = float(entry1.get())
    second_num = float(entry2.get())
    operation = operator.get()
    if operation == "+":
        answer = first_num + second_num
    elif operation == "-":
        answer = first_num - second_num
    elif operation == "*":
        answer = first_num * second_num
    else:
        answer = first_num / second_num
    label.config(text="Answer: " + str(answer))

root = tk.Tk()
root.title("Calculator")

label = tk.Label(root, text="Enter first number")
label.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter second number")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

operator = tk.StringVar()
operator.set("+")

plus = tk.Radiobutton(root, text="+", variable=operator, value="+")
plus.grid(row=2, column=0)

minus = tk.Radiobutton(root, text="-", variable=operator, value="-")
minus.grid(row=2, column=1)

multiply = tk.Radiobutton(root, text="*", variable=operator, value="*")
multiply.grid(row=3, column=0)

divide = tk.Radiobutton(root, text="/", variable=operator, value="/")
divide.grid(row=3, column=1)

calculate = tk.Button(root, text="Calculate", command=calculate)
calculate.grid(row=4, column=1)

root.mainloop()
