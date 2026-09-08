import pytest

import source.shapes as shapes


class TestCircle:

    def setup_method(self,method):
        print(f"Setup method called for {method}")
        self.circle = shapes.Circle(10)

    def test_one(self):
        assert self.circle.area() == 3.14 * self.circle.radius * self.circle.radius

    def test_two(self):
        assert self.circle.perimeter() == 2 * 3.14 * self.circle.radius

    def teardown_method(self,method ):
        print(f"Teardown method called for {method}")