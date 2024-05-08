import tkinter as tk
import math



def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

def clear():
    entry.delete(0, tk.END)

def clear_entry():
    current = entry.get()
    new_text = current[:-1]  # Remove the last character
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_text)


def percentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def reciprocal():
    try:
        result = 1 / float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square():
    try:
        result = float(entry.get()) ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def toggle_sign():
    try:
        current = float(entry.get())
        result = -current
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
# Define color schemes
color_schemes = [
    {"bg": "alice blue", "fg": "cyan", "button_bg": "medium purple", "button_fg": "cyan"},
    {"bg": "cyan", "fg": "alice blue", "button_bg": "light coral", "button_fg": "alice blue"},
    {"bg": "snow2", "fg": "cyan", "button_bg": "deep sky blue", "button_fg": "cyan"},
    # Add more color schemes as needed
]

current_color_scheme_index = 0

def changecolor():
    global current_color_scheme_index
    current_color_scheme_index = (current_color_scheme_index + 1) % len(color_schemes)
    apply_color_scheme(color_schemes[current_color_scheme_index])

def apply_color_scheme(scheme):
    root.configure(bg=scheme["bg"])
    entry.configure(bg=scheme["bg"], fg=scheme["fg"], insertbackground=scheme["fg"])
    for button in l1.winfo_children():
        if isinstance(button, tk.Button):
            button.configure(bg=scheme["button_bg"], fg=scheme["button_fg"])
    for button in l2.winfo_children():
        if isinstance(button, tk.Button):
            button.configure(bg=scheme["button_bg"], fg=scheme["button_fg"])
    for button in l3.winfo_children():
        if isinstance(button, tk.Button):
            button.configure(bg=scheme["button_bg"], fg=scheme["button_fg"])
    for button in l4.winfo_children():
        if isinstance(button, tk.Button):
            button.configure(bg=scheme["button_bg"], fg=scheme["button_fg"])
    for button in l5.winfo_children():
        if isinstance(button, tk.Button):
            button.configure(bg=scheme["button_bg"], fg=scheme["button_fg"])
    for button in l6.winfo_children():
        if isinstance(button, tk.Button):
            button.configure(bg=scheme["button_bg"], fg=scheme["button_fg"])

root = tk.Tk()
root.title("Calculator")
root.wm_iconbitmap("1.ico")
root.resizable(False, False)

entry = tk.Entry(root, width=15, justify='center', font="lucida  28 bold", borderwidth=5)
entry.pack()
l1 = tk.Frame(root)
box1 = tk.Button(l1, text="%", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=percentage)
box1.grid(row=1, column=1, padx=3, pady=3)
box2 = tk.Button(l1, text="C", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=clear)
box2.grid(row=1, column=2, padx=3, pady=3)
img= tk.PhotoImage(file='clear_icon.png')
box3 = tk.Button(l1, image=img, borderwidth=2, relief='raised', width=75, height=50,command=clear_entry)
box3.grid(row=1, column=3, padx=3, pady=3)
img1= tk.PhotoImage(file='dark.png')
box4 = tk.Button(l1, image=img1, borderwidth=2, relief='raised', width=75, height=50, command=changecolor)
box4.grid(row=1, column=4, padx=3, pady=3)
l1.pack()
l2 = tk.Frame(root)
box1 = tk.Button(l2, text="1/x", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=reciprocal)
box1.grid(row=1, column=1, padx=3, pady=3)
box2 = tk.Button(l2, text="x^2", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=square)
box2.grid(row=1, column=2, padx=3, pady=3)
box3 = tk.Button(l2, text="sqrt x", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=square_root)
box3.grid(row=1, column=3, padx=3, pady=3)
box4 = tk.Button(l2, text="/", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click)
box4.grid(row=1, column=4, padx=3, pady=3)
l2.pack()
l3 = tk.Frame(root)
box1 = tk.Button(l3, text="7", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("7"))
box1.grid(row=1, column=1, padx=3, pady=3)
box2 = tk.Button(l3, text="8", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("8"))
box2.grid(row=1, column=2, padx=3, pady=3)
box3 = tk.Button(l3, text="9", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("9"))
box3.grid(row=1, column=3, padx=3, pady=3)
box4 = tk.Button(l3, text="X", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click)
box4.grid(row=1, column=4, padx=3, pady=3)
l3.pack()
l4 = tk.Frame(root)
box1 = tk.Button(l4, text="4", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("4"))
box1.grid(row=1, column=1, padx=3, pady=3)
box2 = tk.Button(l4, text="5", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("5"))
box2.grid(row=1, column=2, padx=3, pady=3)
box3 = tk.Button(l4, text="6", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("6"))
box3.grid(row=1, column=3, padx=3, pady=3)
box4 = tk.Button(l4, text="-", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click)
box4.grid(row=1, column=4, padx=3, pady=3)
l4.pack()
l5 = tk.Frame(root)
box1 = tk.Button(l5, text="1", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("1"))
box1.grid(row=1, column=1, padx=3, pady=3)
box2 = tk.Button(l5, text="2", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("2"))
box2.grid(row=1, column=2, padx=3, pady=3)
box3 = tk.Button(l5, text="3", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("3"))
box3.grid(row=1, column=3, padx=3, pady=3)
box4 = tk.Button(l5, text="+", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click)
box4.grid(row=1, column=4, padx=3, pady=3)
l5.pack()
l6 = tk.Frame(root)
box1 = tk.Button(l6, text="-/+", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=toggle_sign)
box1.grid(row=1, column=1, padx=3, pady=3)
box2 = tk.Button(l6, text="0", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click("0"))
box2.grid(row=1, column=2, padx=3, pady=3)
box3 = tk.Button(l6, text=".", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=lambda: button_click)
box3.grid(row=1, column=3, padx=3, pady=3)
box4 = tk.Button(l6, text="=", borderwidth=2, relief='raised', width=10, height=3, font=("Times New Roman", 10, 'bold'), command=calculate)
box4.grid(row=1, column=4, padx=3, pady=3)
l6.pack()
root.mainloop()