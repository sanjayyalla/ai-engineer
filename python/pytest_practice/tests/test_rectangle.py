import source.shapes as shapes
import pytest

# def test_rectangle():
#     rect = shapes.Rectangle(10,20000)
#     expected = 200000

#     assert rect.area() == expected


# def test_perimeter():

#     rectangle = shapes.Rectangle(10,20)
#     assert rectangle.perimeter() == 60

@pytest.fixture
def my_rect():
    return shapes.Rectangle(10,20)

def test_area(my_rect):
    assert my_rect.area() == 200