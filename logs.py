import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def get_total_price(self):
        return self.price*self.quantity
        
class ShoppingCart(product):
    def __init__(self):
        self.products=[]
    
    def add_product(self,product):
        self.products.append(product)

    def get_total_price(self):
        return sum(product.get_total_price() for product in self.products)

    def clear_cart(self):
        self.products.clear()

class App:
    def __init__ (self,master):
        self.master=master
        self.master.geometry("500x500")
        self.master.title("Veikals")
        self.master.configure(background="grey")
        self.cart=ShoppingCart()

        input_frame = tk.Frame(master)
        input_frame.pack(pady=10)

        self.name_label=tk.Label(input_frame, text="Nosaukums")
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=1, column=1)

        self.quantity_label=tk.Label(input_frame, text="Daudzums")
        self.quantity_label.grid(row=2, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(input_frame)
        self.quantity_entry.grid(row=2, column=1)

        self.price_label=tk.Label(input_frame, text="Cena")
        self.price_label.grid(row=3, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(input_frame)
        self.price_entry.grid(row=3, column=1)
    
        







        master.mainloop()