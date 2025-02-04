from typing import override

from Component import Component
from ComponentGrade import ComponentGrade


class LeafGrade(ComponentGrade):

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    @override
    def add_child(self, child):
        pass

    @override
    def remove_child(self, child):
        pass

    @override
    def get_children(self):
        return None

    @override
    def get_grade(self):
        return self.grade

    def __str__(self):
        return f"{self.name} {self.grade}"

# [ [99, 80, 91], 91]



