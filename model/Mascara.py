from model.Cosmetics import Cosmetics


class Mascara(Cosmetics):

    def __init__(self, name, price, cosmeticType, consistenceType, rating, volume, isAvailable, napType, isSoluble):
        super().__init__(name, price, cosmeticType, consistenceType, rating, volume, isAvailable)
        self.napType = napType
        self.isSoluble = isSoluble

    def __del__(self):
        print("Destructor called")
