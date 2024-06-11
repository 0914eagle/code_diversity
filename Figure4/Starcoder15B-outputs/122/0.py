def add_elements(arr, k):
    
    return sum(int(str(x)[0:2]) for x in arr[:k])
/tests/test_arrays/test_array_manipulation.py
from unittest import TestCase

from arrays.array_manipulation import array_manipulation


class TestArrayManipulation(TestCase):
    