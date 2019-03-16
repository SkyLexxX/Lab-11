from model.Cosmetics import Cosmetics


class Toothpaste(Cosmetics):

    def __init__(self, name, price, cosmeticType, consistenceType, rating, volume, isAvailable, extract):
        super().__init__(name, price, cosmeticType, consistenceType, rating, volume, isAvailable)
        self.extract = extract

    def __del__(self):
        print("Destructor called")
