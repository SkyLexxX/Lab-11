from model.Cosmetics import Cosmetics


class Cream(Cosmetics):

    def __init__(self, name, price, cosmeticType, consistenceType, rating, volume, isAvailable, useType, extract):
        super().__init__(name, price, cosmeticType, consistenceType, rating, volume, isAvailable)
        self.useType = useType
        self.extract = extract

    def __del__(self):
        print("Destructor called")
