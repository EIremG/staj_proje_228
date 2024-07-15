
class Item:
    def __init__(self, name, quantity, price):
        # Item sınıfının yapıcı (constructor) fonksiyonu.
        # name, quantity ve price parametrelerini alır ve bu değerleri sınıfın özelliklerine atar.
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        # Bu fonksiyon, Item nesnesi string olarak temsil edildiğinde nasıl görüneceğini tanımlar.
        return f"Item(name={self.name}, quantity={self.quantity}, price={self.price})"

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
            print(f"Item '{name}' not found in inventory.")

    def remove_item(self, name):
        # Envanterden bir öğeyi kaldırır.
        if name in self.items:
            # Eğer öğe envanterde varsa, onu siler.
            del self.items[name]
        else:
            # Eğer öğe envanterde yoksa, kullanıcıya öğenin bulunamadığını bildirir.
            print(f"Item '{name}' not found in inventory.")

    def list_items(self):
        # Envanterdeki tüm öğeleri listeler.
        for item in self.items.values():
            # Her bir öğeyi ekrana yazdırır.
            print(item)

def main():
    # Inventory sınıfından bir nesne oluşturur.
    inventory = Inventory()
    while True:
        # Kullanıcı menüsü ve seçenekler.
        print("\nEnvanter Yönetim Sistemi")
        print("1. Öğeyi Ekle")
        print("2. Öğeyi Güncelle")
        print("3. Öğeyi Kaldır")
        print("4. Envanteri Listele")
        print("5. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == '1':
            # Kullanıcıdan öğe bilgilerini alır ve envantere ekler.
            name = input("Öğe Adı: ")
            quantity = int(input("Miktar: "))
            price = float(input("Fiyat: "))
            inventory.add_item(name, quantity, price)
        elif choice == '2':
            # Kullanıcıdan güncellenmiş öğe bilgilerini alır ve envanteri günceller.
            name = input("Öğe Adı: ")
            quantity = int(input("Yeni Miktar: "))
            price = float(input("Yeni Fiyat: "))
            inventory.update_item(name, quantity, price)
        elif choice == '3':
            # Kullanıcıdan öğe adını alır ve envanterden kaldırır.
            name = input("Öğe Adı: ")
            inventory.remove_item(name)
        elif choice == '4':
            # Envanterdeki tüm öğeleri listeler.
            inventory.list_items()
        elif choice == '5':
            # Programdan çıkar.
            break
        else:
            # Geçersiz seçim yapıldığında kullanıcıyı uyarır.
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Program bu dosya olarak çalıştırıldığında main fonksiyonunu çağırır.
if __name__ == "__main__":
    main()

def test_inventory():
    # Inventory sınıfından bir nesne oluşturur.
    inventory = Inventory()

    # Envantere öğeler ekler ve listeyi gösterir.
    inventory.add_item("Elma", 10, 1.5)
    inventory.add_item("Armut", 5, 2.0)
    inventory.list_items()

    # Öğeyi günceller ve listeyi gösterir.
    inventory.update_item("Elma", 20, 1.4)
    inventory.list_items()

    # Öğeyi kaldırır ve listeyi gösterir.
    inventory.remove_item("Armut")
    inventory.list_items()

# test_inventory fonksiyonunu çalıştırır.
test_inventory()
