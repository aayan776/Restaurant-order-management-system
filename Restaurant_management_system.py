import tkinter as tk
from tkinter import messagebox
#Functions
def calculate():
    try:
        qty_pizza = int(entry_pizza.get())
        qty_burger = int(entry_burger.get())
        qty_pasta = int(entry_pasta.get())

        pizza_price = 1099
        burger_price = 899
        pasta_price = 699

        total = (qty_pizza * pizza_price) + (qty_burger * burger_price) + (qty_pasta * pasta_price)
        total_label.config(text = f"Total: ${total: .2f}")
    except ValueError:
        messagebox.showerror("Value error", "Invalid Input")
def reset_fields():
    entry_pizza.delete(0, tk.END)
    entry_burger.delete(0, tk.END)
    entry_pasta.delete(0, tk.END)
    total_label.config(text = "Total: 0.00")
def exit_app():
    root.destroy()
def show_home():
    messagebox.showinfo("Home", "Welcome to our restaurant order management system.")
def show_order():
    messagebox.showinfo("Order", "Please place your order using the form below.")
def show_checklist():
    messagebox.showinfo("Checklist", "Review your order details before submission.")
#Main window
root = tk.Tk()
root.title("Restaurant management system")
root.geometry("400x400")
root.configure(bg = "light yellow")
#Navigation bar
menu_bar = tk.Menu(root)
#Home menu
home_menu = tk.Menu(menu_bar, tearoff = 0)
home_menu.add_command(label = "Home", command = show_home)
menu_bar.add_cascade(label = "Home", menu = home_menu)
#Order menu
order_menu = tk.Menu(menu_bar, tearoff = 0)
order_menu.add_command(label = "Order", command = show_order)
menu_bar.add_cascade(label = "Order", menu = order_menu)
#Checklist menu
checklist_menu = tk.Menu(menu_bar, tearoff = 0)
checklist_menu.add_command(label = "Checklist", command = show_checklist)
menu_bar.add_cascade(label = "Checklist", menu = checklist_menu)
#Heading label
heading_label = tk.Label(root, text = "Restaurant menu", font = ("Arial", 16, "bold"), bg = "light yellow")
heading_label.pack(pady = 10)
#Menu items and quantity menu
frame = tk.Frame(root, bg = "light yellow")
frame.pack(pady = 10)
#Pizza
label_pizza = tk.Label(frame, text = "Pizza (1099 BDT)", font = ("Arial", 12), bg = "light yellow")
label_pizza.grid(row = 0, column = 0, padx = 10, pady = 5)
entry_pizza = tk.Entry(frame, width = 10)
entry_pizza.grid(row = 0, column = 1, pady = 5)
#Burger
label_burger = tk.Label(frame, text = "Burger (899 BDT)", font = ("Arial", 12), bg = "light yellow")
label_burger.grid(row = 1, column = 0, padx = 10, pady = 5)
entry_burger = tk.Entry(frame, width = 10)
entry_burger.grid(row = 1, column = 1, pady = 5)
#Pasta
label_pasta = tk.Label(frame, text = "Pasta (699 BDT)", font = ("Arial", 12), bg = "light yellow")
label_pasta.grid(row = 3, column = 0, padx = 10, pady = 5)
entry_pasta = tk.Entry(frame, width = 10)
entry_pasta.grid(row = 3, column = 1, pady = 5)
#Total label
total_label = tk.Label(root, text = "Total: 0.00 BDT", font = ("Arial", 12), bg = "light yellow")
total_label.pack(pady = 10)
#Buttons
button_frame = tk.Frame(root, bg = "light yellow")
button_frame.pack(pady = 20)
#Calculate button
calculate_button = tk.Button(button_frame, text = "Calculate total", font = ("Arial", 12), bg = "green",fg = "white", command = calculate)
calculate_button.grid(row = 0, column = 0, padx = 10)
#Reset button
reset_button = tk.Button(button_frame, text = "Reset", font = ("Arial", 12), bg = "orange",fg = "white", command = reset_fields)
reset_button.grid(row = 0, column = 1, padx = 10)
#Exit button
exit_button = tk.Button(button_frame, text = "Exit", font = ("Arial", 12), bg = "red",fg = "white", command = exit_app)
exit_button.grid(row = 0, column = 2, padx = 10)
#Mainloop
root.mainloop()