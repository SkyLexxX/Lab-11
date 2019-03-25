from enums.ConsistenceType import ConsistenceType
from enums.CosmeticType import CosmeticType
from enums.NapType import NapType
from enums.Rating import Rating
from enums.UseType import UseType
from manager.CosmeticsManager import ICosmeticsManager
from model.Cream import Cream
from model.Mascara import Mascara
from model.Soap import Soap
from model.Toothpaste import Toothpaste


class CosmeticsManagerImpl(ICosmeticsManager):
    customer_balance = 0

    def __init__(self, cosmeticList):
        ICosmeticsManager.__init__(self)
        self.cosmeticList = []

    def sortByVolume(self, reverse):
        return sorted(self.cosmeticList, key=lambda cosmetic: cosmetic.volume, reverse=reverse)

    def sortByPrice(self, reverse):
        return sorted(self.cosmeticList, key=lambda cosmetic: cosmetic.price, reverse=reverse)

    def findByAvailability(self):
        return list(filter(lambda cosmetics: cosmetics.isAvailable, self.cosmeticList))

    def checkBalance(self, customer_balance):
        if customer_balance == 0:
            print("Not enough money. Balance = 0 \n")
            return "Not enough money. Balance = 0"
        else:
            return customer_balance
