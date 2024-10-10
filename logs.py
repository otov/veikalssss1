import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def get_total_price(self):
        return self.price*self.quantity


class ShoppingCart(Product):
    def __init__(self):
        self.products=[]
    
    def add_product(self,product):
        self.products.append(product)

    def get_total_price(self):
        return sum(product.get_total_price() for product in self.products)

    def clear_cart(self):
        self.products.clear()

    

class App(ShoppingCart):
    def __init__ (self,master):
        self.master=master
        self.master.geometry("500x860")
        self.master.title("Veikals")
        self.master.configure(background="grey")
        self.cart=ShoppingCart()


        title_frame = tk.Frame(master)
        title_frame.pack(pady=10)

        self.virsraksts=tk.Label(title_frame, text="Automašīnu rezerves daļu veikals", font=("Helvetica",20, "bold"), fg="Black", bd=1, bg="gray")
        self.virsraksts.grid(row=0,column=1)

        input_frame = tk.Frame(master, bg="gray")
        input_frame.pack(pady=10)

        

        self.name_label=tk.Label(input_frame, text="Nosaukums:", bg="grey", font=("Helvetica", 15, "bold"))
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=1, column=1)

        self.quantity_label=tk.Label(input_frame, text="Daudzums:", bg="grey",font=("Helvetica", 15, "bold"))
        self.quantity_label.grid(row=2, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(input_frame)
        self.quantity_entry.grid(row=2, column=1)

        self.price_label=tk.Label(input_frame, text="Cena:", bg="grey",font=("Helvetica", 15, "bold"))
        self.price_label.grid(row=3, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(input_frame)
        self.price_entry.grid(row=3, column=1)


        self.add_button=tk.Button(master, text="Pievienot grozam",command=self.add_to_cart, font=("Helvetica", 15, "bold"),fg="Green",bd=3)
        self.add_button.pack(pady=5)

        self.cart_listbox=tk.Listbox(master,width=60,bg="black",fg="white", font=("Helvetica", 10, "bold" ))
        self.cart_listbox.pack(pady=5)

        self.total_label = tk.Label(master, text="Kopējā cena: 0.00 Eur",font=("Helvetica",15,"bold"),bg="grey")
        self.total_label.pack(pady=5)

        self.clear_button = tk.Button(master, text="Dzēst grozu", command=self.clear_cart, font=("Helvetica", 15, "bold"),fg="Red",bd=3)
        self.clear_button.pack(pady=5)

        self.quit_button=tk.Button(master,text="Aizvērt logu", command=master.destroy, font=("Helvica", 15, "bold"),fg="Red",bd=3)
        self.quit_button.pack(pady=2)


        self.foto_frame=tk.Frame(master, bg="Black")
        self.foto_frame.pack(pady=5)
        self.foto_image=Image.open("BMW.jpg")
        self.resized_foto=self.foto_image.resize((400,260))
        self.foto = ImageTk.PhotoImage(self.resized_foto)
        self.foto_label=ttk.Label(self.foto_frame,image=self.foto, background="black")
        self.foto_label.grid(row=1,column=1,columnspan=2,padx=1,pady=1)




    def add_to_cart(self):
        name=self.name_entry.get()
        price = float(self.price_entry.get())
        quantity = float(self.quantity_entry.get())

        product = Product(name, price, quantity)
        self.cart.add_product(product)
        self.cart_listbox.insert(tk.END, f"| Produkts: {name} | Cena: ${price} | Daudzums: {quantity} gab. |")

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

        self.update_total_price()

    def update_total_price(self):
        total=self.cart.get_total_price()
        self.total_label.config(text=f"Kopējā cena: {total:.2f} $")
    
    def clear_cart(self):
        self.cart.clear_cart()
        self.cart_listbox.delete(0, tk.END)
        self.update_total_price()




if __name__ == "__main__":
    root=tk.Tk()
    app=App(root)   
    root.mainloop()