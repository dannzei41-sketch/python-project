import tkinter as tk

# Create a main window
window = tk.Tk()
window.title("My calculator app")
window.geometry("350x500")
window.resizable(False, False)
window.configure(bg="black")

# Create a display
display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bg="black",
    fg="white",
    bd=0,
    insertbackground="white",
)
display.pack(fill="x", padx=15, pady=20, ipady=20)

# Frame for the buttons
button_frame = tk.Frame(window, bg="black")
button_frame.pack(expand=True, fill="both", padx=10, pady=15)


def on_click(label):
    if label == "AC":
        display.delete(0, tk.END)
    elif label == "DEL":
        display.delete(len(display.get()) - 1, tk.END)
    elif label == "=":
        expression = display.get()
        expression = expression.replace("×", "*").replace("÷", "/").replace("−", "-")
        expression = expression.replace("%", "/100")
        try:
            result = eval(expression)  # fine for a learning project
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, label)


# Calculator buttons
buttons = [
    ["AC", "DEL", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "="],
]

for row_index, row in enumerate(buttons):
    for col_index, text in enumerate(row):
        if text in ["÷", "×", "−", "+", "="]:
            color = "orange"
        elif text in ["AC", "DEL", "%"]:
            color = "gray30"
        else:
            color = "gray20"

        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 19, "bold"),
            bg=color,
            fg="white",
            bd=0,
            command=lambda t=text: on_click(t),
        )

        # Make "0" span two columns, shifting the rest across
        if row_index == 4:
            if text == "0":
                button.grid(row=row_index, column=0, columnspan=2,
                            sticky="nsew", padx=5, pady=5)
            elif text == ".":
                button.grid(row=row_index, column=2,
                            sticky="nsew", padx=5, pady=5)
            else:  # "="
                button.grid(row=row_index, column=3,
                            sticky="nsew", padx=5, pady=5)
        else:
            button.grid(row=row_index, column=col_index,
                        sticky="nsew", padx=5, pady=5)

# Make the button cells expand equally (outside the loops)
for i in range(5):
    button_frame.rowconfigure(i, weight=1)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# Keep the window running (once, at the very end, no indentation)
window.mainloop()