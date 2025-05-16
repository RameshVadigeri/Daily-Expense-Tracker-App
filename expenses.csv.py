import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime

# File to save expenses
FILENAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Note"])

# Function to add an expense
def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    note = note_entry.get()

    if not (date and category and amount):
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    try:
        float(amount)  # check if amount is a number
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")
        return

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    messagebox.showinfo("Saved", "Expense saved successfully!")
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

# Function to view all expenses
def view_expenses():
    if not os.path.exists(FILENAME):
        messagebox.showinfo("No Data", "No expenses found.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    output_window = tk.Toplevel(root)
    output_window.title("All Expenses")
    text = tk.Text(output_window, width=70, height=20)
    text.pack()

    for row in data:
        text.insert(tk.END, ", ".join(row) + "\n")

# GUI
root = tk.Tk()
root.title("Daily Expense Tracker")

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
tk.Label(root, text="Category:").grid(row=1, column=0)
tk.Label(root, text="Amount:").grid(row=2, column=0)
tk.Label(root, text="Note:").grid(row=3, column=0)

date_entry = tk.Entry(root)
category_entry = tk.Entry(root)
amount_entry = tk.Entry(root)
note_entry = tk.Entry(root)

# Auto-fill today's date
date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))

date_entry.grid(row=0, column=1)
category_entry.grid(row=1, column=1)
amount_entry.grid(row=2, column=1)
note_entry.grid(row=3, column=1)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=4, column=0, pady=10)
tk.Button(root, text="View Expenses", command=view_expenses).grid(row=4, column=1, pady=10)

root.mainloop()
