def add_elements(arr, k):
    
    return sum(x % 10000 for x in arr[:k])


if __name__ == '__main__':
    print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))