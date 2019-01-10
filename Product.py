class Product:
   total = 0
   def __init__(self, price,quantity,ID):
      self.price = price
      self.quantity = quantity
      self.ID = ID
      Product.total += 1

class Inventory:
	def __init__(self,products=[]):
		self.products = products

	def addProduct(self):
		id = int(input("Enter a id"))
		price = int(input("Enter the price"))
		quantity = int(input("Enter the quantity of item"))
		self.products.append(Product(price,quantity,id))

	def removeProduct(self,id):
		Todelete = 0
		for i in range(len(self.products)):
			if self.products[i].ID == id:
				Todelete = self.products[i]
				id1 = self.products.index(Todelete)
				self.products.pop(id1)
				print("Deleted")
			else:
				print("Product not found")
	def displayProducts(self):
		print("The products are:")
		for i in range(len(self.products)):
			print(f"ID is {self.products[i].ID}")
			print(f"Price is {self.products[i].price}")
			print(f"Quantity is {self.products[i].quantity}")

	def sumValue(self):
		sum = 0
		for i in range(len(self.products)):
			sum = sum + self.products[i].quantity * self.products[i].price
		print(sum) 

while(true):
	inventory = Inventory()
	ch = int(input("Enter: 1.Add elements\n2.Delete Elements\n3.Display Products\n4.Sum Value\n5.Exit"))
	if(ch == 1):
		inventory.addProduct()
	if(ch == 2):
		id = int(input("Enter the ID to be deleted")
		inventory.removeProduct(id)	
	if(ch == 3):
		inventory.displayProducts()
	if(ch == 4):
		inventory.sumValue()
	if(ch == 5):
		exit()