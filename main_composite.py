from Composite import Composite
from Leaf import Leaf

# composite = list
# leaf = number
# [ 5, [ 2, 2, 2, , [ [ 2, 1] ] ]]
root = Composite("container0")
circle1 = Leaf("Circle1")
rectangle1 = Leaf("rectangle1")

container1 = Composite("container1")
circle2 = Leaf("Circle2")
circle3 = Leaf("Circle3")
container1.add_child(circle2)
container1.add_child(circle3)

container2 = Composite("container2")
container3 = Composite("container3")
container2.add_child(container3)

triangle = Leaf("triangle1")
container3.add_child(triangle)

root.add_child(circle1)
root.add_child(rectangle1)
root.add_child(container1)
root.add_child(container2)

root.draw()
