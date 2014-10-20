class Product:

    def __init__(self, name, purchase, sale):
        self.name = name
        self.purchase = purchase
        self.sale = sale

    def profit(self):
        return self.sale - self.purchase


class Laptop(Product):

    def __init__(self, name, purchase, sale, diskspace, ram):
        super().__init__(name, purchase, sale)
        self.diskspace = diskspace
        self.ram = ram


class Smartphone(Product):

    def __init__(self, name, purchase, sale, display_size, mega_pixels):
        super().__init__(name, purchase, sale)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def load_new_products(self, item, count):
        if item in self.items:
            self.items[item] += count
            print("was upgraded")
        else:
            self.items = {item:count}
            print("was added")

    def list_products(self):
        for item in self.items:
            print(item)








new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
new_store = Store('Laptop.bg')
new_store.load_new_products(new_smarthphone, 20)
new_store.list_products()

