import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import mysql.connector

class Product:
    def __init__(self, id, name, description, quantity, id_category, price):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.id_category = id_category
        self.price = price

    def to_tuple(self):
        return self.id, self.name, self.description, self.quantity, self.id_category, self.price

class Dashboard:
    def __init__(self, master):
        self.master = master
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="azerty1234",
            database="store"
        )
        self.cursor = self.mydb.cursor()
        self.products = []
        self.tree = ttk.Treeview(master, columns=('ID', 'Nom', 'Description', 'Quantité', 'ID Catégorie', 'Prix'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nom', text='Nom')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Quantité', text='Quantité')
        self.tree.heading('ID Catégorie', text='ID Catégorie')
        self.tree.heading('Prix', text='Prix')
        self.tree.pack()

        add_button = tk.Button(master, text="Ajouter un produit", command=self.add_product)
        add_button.pack()

        delete_button = tk.Button(master, text="Supprimer un produit", command=self.delete_product)
        delete_button.pack()

        modify_button = tk.Button(master, text="Modifier un produit", command=self.modify_product)
        modify_button.pack()

        self.load_products()

    def load_products(self):
        self.cursor.execute("SELECT * FROM product")
        for row in self.cursor.fetchall():
            product = Product(*row)
            self.products.append(product)
            self.tree.insert('', 'end', values=product.to_tuple())

    def add_product(self):
        name = simpledialog.askstring("Ajouter un produit", "Nom du produit:")
        description = simpledialog.askstring("Ajouter un produit", "Description du produit:")
        quantity = simpledialog.askinteger("Ajouter un produit", "Quantité:")
        id_category = simpledialog.askinteger("Ajouter un produit", "ID Catégorie:")
        price = simpledialog.askfloat("Ajouter un produit", "Prix:")
        product = Product(None, name, description, quantity, id_category, price)
        self.products.append(product)
        self.tree.insert('', 'end', values=product.to_tuple()[1:])  # Exclude 'id' from display
        self.cursor.execute("INSERT INTO product (nom, description, quantity, id_category, price) VALUES (%s, %s, %s, %s, %s)", product.to_tuple()[1:])
        self.mydb.commit()

    def delete_product(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Erreur", "Aucun produit sélectionné")
            return
        product = self.products.pop(self.tree.index(selected))
        self.tree.delete(selected)
        self.cursor.execute("DELETE FROM product WHERE id = %s", (product.id,))
        self.mydb.commit()

    def modify_product(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Erreur", "Aucun produit sélectionné")
            return
        product = self.products[self.tree.index(selected)]
        new_name = simpledialog.askstring("Modifier un produit", "Nouveau nom pour {}: ".format(product.name))
        new_description = simpledialog.askstring("Modifier un produit", "Nouvelle description pour {}: ".format(product.name))
        new_quantity = simpledialog.askinteger("Modifier un produit", "Nouvelle quantité pour {}: ".format(product.name))
        new_id_category = simpledialog.askinteger("Modifier un produit", "Nouvel ID de catégorie pour {}: ".format(product.name))
        new_price = simpledialog.askfloat("Modifier un produit", "Nouveau prix pour {}: ".format(product.name))
        product.name = new_name
        product.description = new_description
        product.quantity = new_quantity
        product.id_category = new_id_category
        product.price = new_price
        self.tree.set(selected, 'Nom', product.name)
        self.tree.set(selected, 'Description', product.description)
        self.tree.set(selected, 'Quantité', product.quantity)
        self.tree.set(selected, 'ID Catégorie', product.id_category)
        self.tree.set(selected, 'Prix', product.price)
        self.cursor.execute("UPDATE product SET nom = %s, description = %s, quantity = %s, id_category = %s, price = %s WHERE id = %s", 
                            (product.name, product.description, product.quantity, product.id_category, product.price, product.id))
        self.mydb.commit()

root = tk.Tk()
root.geometry("800x600")  # Définit la taille de la fenêtre à 800x600 pixels
dashboard = Dashboard(root)
root.mainloop()
