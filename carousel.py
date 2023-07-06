from tkinter import Tk, Label, Button

class Carousel:
    def __init__(self, master):
        self.master = master
        self.master.title("Карусель товаров")

        self.products = [
            {"name": "Товар 1", "price": "$10"},
            {"name": "Товар 2", "price": "$20"},
            {"name": "Товар 3", "price": "$30"},
            # Добавьте здесь остальные товары
        ]

        self.current_product = 0

        self.product_name_label = Label(master, text=self.products[self.current_product]["name"])
        self.product_name_label.pack()

        self.product_price_label = Label(master, text=self.products[self.current_product]["price"])
        self.product_price_label.pack()

        self.next_button = Button(master, text="Следующий", command=self.next_product)
        self.next_button.pack()

    def next_product(self):
        self.current_product += 1
        if self.current_product >= len(self.products):
            self.current_product = 0

        self.product_name_label.config(text=self.products[self.current_product]["name"])
        self.product_price_label.config(text=self.products[self.current_product]["price"])

root = Tk()
carousel = Carousel(root)
root.mainloop()