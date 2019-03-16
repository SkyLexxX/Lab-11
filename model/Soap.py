from model.Cosmetics import Cosmetics


class Soap(Cosmetics):

    def __init__(self, name, price, cosmeticType, consistenceType, rating, volume, isAvailable, fatPercentage, taste):
        super().__init__(name, price, cosmeticType, consistenceType, rating, volume, isAvailable)
        self.fatPercentage = fatPercentage
        self.taste = taste

    def __del__(self):
        print("Destructor called")
