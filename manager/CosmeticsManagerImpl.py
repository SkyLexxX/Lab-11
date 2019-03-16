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


def main():
    cream = Cream("Nivea", 100, CosmeticType.PROTECTIVE, ConsistenceType.EMULSION, Rating.EXCELLENT, 130, True,
                  UseType.BODY, "Honey")
    toothpaste = Toothpaste("Colgate", 150, CosmeticType.DECORATIVE, ConsistenceType.LIQUID, Rating.GREAT, 125, False,
                            "Pineapple")
    mascara = Mascara("mascaraName", 200, CosmeticType.HEALING, ConsistenceType.PASTE, Rating.GOOD, 100, True,
                      NapType.LONG, True)
    soap = Soap("Head&Shoulders", 250, CosmeticType.HYGIENIC, ConsistenceType.SOLID, Rating.GREAT, 200, True, 72,
                "Apple")

    cosmetics_manager_impl = CosmeticsManagerImpl([cream, toothpaste, mascara, soap])
    cosmetics_manager_impl.cosmeticList = [cream, toothpaste, mascara, soap]

    print("\n", cosmetics_manager_impl.sortByVolume(False))
    print("\n", cosmetics_manager_impl.sortByPrice(False))
    print("\n", cosmetics_manager_impl.findByAvailability())
    print("\n", cosmetics_manager_impl.checkBalance(5))


if __name__ == '__main__':
    main()
