from PyQt5 import QtWidgets

class POSApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("F1D022052 Ida Bagus Brahmanta")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QtWidgets.QVBoxLayout()
        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        
        # Dropdown Produk
        self.productDropdown = QtWidgets.QComboBox()
        self.products = {"God Of War X (Rp.100.000,00)": 100000.0, "GTA 8 (Rp. 200.000,00)": 200000.0, "Dewa Abadi (Rp.800.000,00)": 800000.0}
        self.productDropdown.addItem("")
        self.productDropdown.addItems(self.products.keys())
        layout.addWidget(QtWidgets.QLabel("Product"))
        layout.addWidget(self.productDropdown)
        
        # Input Jumlah
        self.quantityInput = QtWidgets.QSpinBox()
        self.quantityInput.setMinimum(0)
        layout.addWidget(QtWidgets.QLabel("Quantity"))
        layout.addWidget(self.quantityInput)
        
        # Dropdown Diskon
        self.discountDropdown = QtWidgets.QComboBox()
        self.discountDropdown.addItems(["0%", "10%", "20%", "30%"])
        layout.addWidget(QtWidgets.QLabel("Discount"))
        layout.addWidget(self.discountDropdown)
        
        # Tombol
        buttonLayout = QtWidgets.QHBoxLayout()
        self.addToCartButton = QtWidgets.QPushButton("Add to Cart")
        self.clearButton = QtWidgets.QPushButton("Clear")
        buttonLayout.addWidget(self.addToCartButton)
        buttonLayout.addWidget(self.clearButton)
        layout.addLayout(buttonLayout)
        
        # List Keranjang
        self.cartList = QtWidgets.QListWidget()
        layout.addWidget(self.cartList)
        
        # Label Total
        self.totalLabel = QtWidgets.QLabel("Total: Rp. 0")
        layout.addWidget(self.totalLabel)
        
        # Event Handling
        self.addToCartButton.clicked.connect(self.add_to_cart)
        self.clearButton.clicked.connect(self.clear_form)
        
        self.cart = []
        self.clear_form()  # Set awal kosong
        
    def add_to_cart(self):
        product = self.productDropdown.currentText()
        quantity = self.quantityInput.value()
        discount = int(self.discountDropdown.currentText().replace("%", ""))
        
        if not product or quantity == 0:
            return self.totalLabel.setText("Invalid Input")

        price = self.products[product] * quantity
        price_after_discount = price * (1 - discount / 100)
        
        self.cart.append(price_after_discount)
        self.cartList.addItem(f"{product} - {quantity} x  Rp.{self.products[product]}  (disc {discount}%)")
        
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
        self.totalLabel.setText(f"Total: Rp. {total_price:.2f}")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = POSApp()
    window.show()
    sys.exit(app.exec_())
