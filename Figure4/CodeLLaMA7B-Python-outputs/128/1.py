def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(i) for i in arr) * (-1 if arr[0] < 0 else 1)


if __name__ == "__main__":
