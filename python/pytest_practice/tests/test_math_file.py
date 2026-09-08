import pytest
import source.math_file as math_file

def test_add():
    res = math_file.add(10000000,10000000)
    assert res == 20000000


def test_divide():
    res = math_file.divide(10, 2)
    assert res == 5

    # with pytest.raises(ValueError):
    #     math_file.divide(10, 0)

def test_divide_by_zero():
    with pytest.raises(ValueError):
            math_file.divide(10, 0)

