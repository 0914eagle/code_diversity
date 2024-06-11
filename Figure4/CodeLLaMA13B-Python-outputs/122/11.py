def add_elements(arr, k):
    
    return sum(x if x < 100 else x // 10 for x in arr[:k])


if __name__ == "__main__":
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4