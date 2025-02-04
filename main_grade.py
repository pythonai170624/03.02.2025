from CompositeGrade import CompositeGrade
from LeafGrade import LeafGrade

# composite = list
# leaf = number
# [ 5, [ 2, 2, 2, , [ [ 2, 1] ] ]]
class_yod1 = CompositeGrade("class-yod1")
talmid11 = LeafGrade("talmid1", 90)
talmid12 = LeafGrade("talmid1", 85)
class_yod1.add_child(talmid11)
class_yod1.add_child(talmid12)

class_yod2 = CompositeGrade("class-yod1")
talmid21 = LeafGrade("talmid1", 90)
talmid22 = LeafGrade("talmid2", 100)
class_yod2.add_child(talmid21)
class_yod2.add_child(talmid22)

print('class_yod1.get_grade()', class_yod1.get_grade())
print('class_yod2.get_grade()', class_yod2.get_grade())

shihvat_yod = CompositeGrade("shihvat-yod")
shihvat_yod.add_child(class_yod1)
shihvat_yod.add_child(class_yod2)
memutza_yod = shihvat_yod.get_grade()
print('shihvat_yod.get_grade()', memutza_yod)
