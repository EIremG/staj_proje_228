import tkinter as tk
from tkinter import messagebox, ttk

class Item:
    def __init__(self, name, quantity, price):
        # Item sınıfının yapıcı (constructor) fonksiyonu.
        # name, quantity ve price parametrelerini alır ve bu değerleri sınıfın özelliklerine atar.
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        # Bu fonksiyon, Item nesnesi string olarak temsil edildiğinde nasıl görüneceğini tanımlar.
        return f"{self.name}: {self.quantity} adet, {self.price:.2f} TL"

class Inventory:
    def __init__(self):
        # Inventory sınıfının yapıcı (constructor) fonksiyonu.
        # Envanterdeki öğeleri saklamak için boş bir sözlük oluşturur.
        self.items = {}

    def add_item(self, name, quantity, price):
        # Envantere yeni bir öğe ekler veya mevcut bir öğenin miktarını artırır.
        if name in self.items:
            # Eğer öğe zaten envanterde varsa, mevcut miktara ekler.
            self.items[name].quantity += quantity
        else:
            # Eğer öğe envanterde yoksa, yeni bir Item nesnesi oluşturur ve envantere ekler.
            self.items[name] = Item(name, quantity, price)

    def update_item(self, name, quantity, price):
        # Envanterdeki bir öğeyi günceller.
        if name in self.items:
            # Eğer öğe envanterde varsa, miktar ve fiyatını günceller.
            self.items[name].quantity = quantity
            self.items[name].price = price
        else:
            # Eğer öğe envanterde yoksa, kullanıcıya öğenin bulunamadığını bildirir.
            messagebox.showerror("Hata", f"Item '{name}' envanterde bulunamadı.")

    def remove_item(self, name):
        # Envanterden bir öğeyi kaldırır.
        if name in self.items:
            # Eğer öğe envanterde varsa, onu siler.
            del self.items[name]
        else:
            # Eğer öğe envanterde yoksa, kullanıcıya öğenin bulunamadığını bildirir.
            messagebox.showerror("Hata", f"Item '{name}' envanterde bulunamadı.")

    def list_items(self):
        # Envanterdeki tüm öğeleri listeler.
        items_str = "\n".join(str(item) for item in self.items.values())
        if items_str:
            # Eğer envanterde öğeler varsa, kullanıcıya gösterir.
            messagebox.showinfo("Envanter", items_str)
        else:
            # Eğer envanter boşsa, kullanıcıya bildirir.
            messagebox.showinfo("Envanter", "Envanter boş.")

class InventoryApp:
    def __init__(self, root):
        # InventoryApp sınıfının yapıcı (constructor) fonksiyonu.
        # Inventory sınıfından bir nesne oluşturur ve Tkinter ana penceresini başlatır.
        self.inventory = Inventory()

        self.root = root
        self.root.title("Envanter Yönetim Sistemi")
        self.root.geometry("500x400")  # Pencere boyutunu ayarlar.
        self.root.resizable(False, False)  # Pencerenin boyutunun değiştirilememesini sağlar.

        # Stil ve fontları ayarlar.
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 14))
        self.style.configure("TButton", font=("Helvetica", 12))

        # Öğe Adı etiketi ve giriş alanı.
        self.name_label = ttk.Label(root, text="Öğe Adı")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        self.name_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="EW")

        # Miktar etiketi ve giriş alanı.
        self.quantity_label = ttk.Label(root, text="Miktar")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.quantity_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10, sticky="EW")

        # Fiyat etiketi ve giriş alanı.
        self.price_label = ttk.Label(root, text="Fiyat")
        self.price_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.price_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.price_entry.grid(row=2, column=1, padx=10, pady=10, sticky="EW")

        # Öğe Ekle düğmesi.
        self.add_button = ttk.Button(root, text="Öğe Ekle", command=self.add_item)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)

        # Öğe Güncelle düğmesi.
        self.update_button = ttk.Button(root, text="Öğe Güncelle", command=self.update_item)
        self.update_button.grid(row=3, column=1, padx=10, pady=10)

        # Öğe Kaldır düğmesi.
        self.remove_button = ttk.Button(root, text="Öğe Kaldır", command=self.remove_item)
        self.remove_button.grid(row=4, column=0, padx=10, pady=10)

        # Envanteri Listele düğmesi.
        self.list_button = ttk.Button(root, text="Envanteri Listele", command=self.list_items)
        self.list_button.grid(row=4, column=1, padx=10, pady=10)

    def add_item(self):
        # Kullanıcıdan alınan bilgilerle envantere öğe ekler.
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        self.inventory.add_item(name, quantity, price)
        messagebox.showinfo("Başarılı", f"{name} eklendi.")

    def update_item(self):
        # Kullanıcıdan alınan bilgilerle envanterdeki öğeyi günceller.
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        self.inventory.update_item(name, quantity, price)
        messagebox.showinfo("Başarılı", f"{name} güncellendi.")

    def remove_item(self):
        # Kullanıcıdan alınan bilgiyle envanterden öğe kaldırır.
        name = self.name_entry.get()
        self.inventory.remove_item(name)
        messagebox.showinfo("Başarılı", f"{name} kaldırıldı.")

    def list_items(self):
        # Envanterdeki tüm öğeleri listeler.
        self.inventory.list_items()

if __name__ == "__main__":
    # Tkinter ana penceresini oluşturur ve InventoryApp'i başlatır.
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
