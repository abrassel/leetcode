from kth_polynomial import _permutations, _numbers, kth_polynomial
from indexed_tree import singleton_empty_indexed_tree

def test_polynomials():
    polynomials = _permutations(3)
    assert polynomials == [1, 1, 2, 6]

def test_numbers():
    numbers = singleton_empty_indexed_tree
    numbers = _numbers(singleton_empty_indexed_tree, 1, 8)
    assert numbers.value == 4
    assert numbers.left.value == 2
    assert numbers.left.left.value == 1
    assert numbers.left.right.value == 3
    assert numbers.right.value == 6
    assert numbers.right.left.value == 5
    assert numbers.right.right.value == 7

def test_kth_polynomial():
    assert kth_polynomial(3, 3) == "213"
    assert kth_polynomial(4, 9) == "2314"
    assert kth_polynomial(3, 1) == "123"