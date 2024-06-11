def add_elements(arr, k):
    
    return sum(int(x) for x in map(str, arr[:k]) if len(x) <= 2)


if __name__ == "__main__":
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) ==