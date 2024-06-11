def add_elements(arr, k):
    
    return sum(map(lambda x: x if x < 100 else 0, arr[:k]))
/tests/test_add_elements.py
from src.add_elements import add_elements


