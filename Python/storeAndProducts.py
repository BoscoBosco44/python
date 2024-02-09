# turn productList and priceList in to a list of dictionaries


class Store:
    productList = []
    priceList = []

    def __init__(self, name, productList=[]):
        self.name = name
        self.productList = productList
        for x in productList:
            Store.productList.append(x)

    def addProduct(self, newProduct, price):
        self.productList.append(newProduct)
        return self
    
    def sellProduct(self, id):
        del self.productList[id]
        return self
    
    def inflation(self, percentIncrease):
        for x in Store.productList:
            x.update_price(percentIncrease, True)

    def printInfo(self):
        print("//------------- Printing Store Info ------------//")
        print("Name: ", self.name)
        print("Num Products: ", len(self.productList))
        print(self.productList)
        for Product in self.productList:
            print(Product.price)
        print("//----------------------------------------------//")

        return self

class Product:
    def __init__(self, name, category, price=5):
        self.name = name
        self.price = price
        self.category = category
        Store.productList.append(self)

    def update_price(self, percentChange, isIncreased):
        self.percentChange = percentChange
        self.isIncreased = isIncreased
        return self
    
    def printInfo(self):
        print("Name: ", self.name)
        print("Category: ", self.category)
        print("Price: ", self.price)
        return self
    


sharaMart = Store("Shara Mart")
sharaMart.addProduct()
sharaMart.printInfo()

sharaMart.addProduct("Muffins")