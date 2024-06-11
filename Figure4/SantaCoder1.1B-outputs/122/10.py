def add_elements(arr, k):
    
    # TODO: Your code here
    # 1. Sort the array
    arr.sort()
    # 2. Find the first k elements
    first_k = arr[:k]
    # 3. Find the last k elements
    last_k = arr[-k:]
    # 4. Find the sum of the first k elements
    sum_first_k = sum(first_k)
    # 5. Find the sum of the last k elements
    sum_last_k = sum(last_k)
    # 6. Find the difference between the sum of the first k elements and the sum of the last k elements
    diff = sum_first_k - sum_last_k
    # 7. Return the difference
    return diff


if __name__ == "__main__":
    print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))
