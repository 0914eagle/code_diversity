def pluck(arr):
    
    if not arr:
        return []
    evens = [i for i in arr if i % 2 == 0]
    if not evens:
        return []
    return [min(evens), arr.index(min(evens))]


if __name__ == "__main__":
