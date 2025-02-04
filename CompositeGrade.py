from typing import override

from Component import Component
from ComponentGrade import ComponentGrade


class CompositeGrade(ComponentGrade):

    def __init__(self, name):
        super().__init__(name)
        self.children = []

    @override
    def add_child(self, child):
        self.children.append(child)

    @override
    def remove_child(self, child):
        self.children.remove(child)

    @override
    def get_children(self):
        return self.children

    @override
    def get_grade(self):
        total_grades = 0
        counter = 0
        # [99, 80, 80, 77]
        # [ [99, 88] , [77, 100] ]
        #     kita1      kita2
        for child in self.children:
            counter += 1
            total_grades += child.get_grade()
        return total_grades / counter






