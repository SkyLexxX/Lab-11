from enums.CosmeticType import CosmeticType
from enums.ConsistenceType import ConsistenceType
from enums.Rating import Rating
from enums.UseType import UseType
from enums.NapType import NapType
from manager.CosmeticsManagerImpl import CosmeticsManagerImpl
from model.Cream import Cream
from model.Mascara import Mascara
from model.Soap import Soap
from model.Toothpaste import Toothpaste


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
