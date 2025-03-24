# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class POSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pos_ui.ui", self, None)

        # Data produk
        self.products = {
            "God Of War X (Rp.100.000,00)": 100000.0,
            "GTA 8 (Rp. 200.000,00)": 200000.0,
            "Dewa Abadi (Rp.800.000,00)": 800000.0
        }

        # Isi dropdown produk
        self.productDropdown.addItem("")  # Awalnya kosong
        self.productDropdown.addItems(self.products.keys())

        # Event Handling
        self.addToCartButton.clicked.connect(self.add_to_cart)
        self.clearButton.clicked.connect(self.clear_form)

        # Inisialisasi cart
        self.cart = []
        self.clear_form()  # Set awal kosong

    def add_to_cart(self):
        product = self.productDropdown.currentText()
        quantity = self.quantityInput.value()
        discount = int(self.discountDropdown.currentText().replace("%", ""))

        if not product or quantity == 0:
            self.totalLabel.setText("Invalid Input")
            return

        price = self.products[product] * quantity
        price_after_discount = price * (1 - discount / 100)

        self.cart.append(price_after_discount)
        self.cartList.addItem(f"{product} - {quantity} x Rp.{self.products[product]:,.0f} (disc {discount}%)")

        self.update_total()

    def clear_form(self):
        self.productDropdown.setCurrentIndex(0)
        self.quantityInput.setValue(0)
        self.discountDropdown.setCurrentIndex(0)
        self.cartList.clear()
        self.cart = []
        self.update_total()

    def update_total(self):
        total_price = sum(self.cart)
        self.totalLabel.setText(f"Total: Rp. {total_price:,.2f}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = POSApp()
    window.show()
    sys.exit(app.exec())
