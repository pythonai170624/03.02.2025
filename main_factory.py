from Aroma import Aroma
from CoffeeLatte import CoffeeLatte
from Espresso import Espresso
from HotCoco import HotCoco

coco = HotCoco('shoko')
espresso = Espresso('double espresso')
late = CoffeeLatte('hafuh gadol')

my_drink = Aroma.get_drink()