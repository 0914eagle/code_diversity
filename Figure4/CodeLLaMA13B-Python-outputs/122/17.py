def add_elements(arr, k):
    
    return sum(i for i in arr[:k] if i < 100)


if __name__ == "__main__":
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24