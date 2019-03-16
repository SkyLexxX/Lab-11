class Cosmetics:

    def __init__(self, name, price, cosmeticType, consistenceType, rating, volume, isAvailable):
        self.name = name
        self.price = price
        self.cosmeticType = cosmeticType
        self.consistenceType = consistenceType
        self.rating = rating
        self.volume = volume
        self.isAvailable = isAvailable

    def __del__(self):
        print("Destructor called")
