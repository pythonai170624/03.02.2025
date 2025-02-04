from CoffeeLatte import CoffeeLatte
from Drink import Drink
from Espresso import Espresso
from HotCoco import HotCoco


class Aroma:

    @staticmethod
    def get_drink() -> Drink:
        age = int(input('how old are you? '))
        if age < 12:
            return HotCoco('shoko ham')
        lactose = input('are you ok with lactose [yes,no]? ')
        if lactose.lower() == "yes":
            return CoffeeLatte('hafuh gadol')
        return Espresso('double shot')
