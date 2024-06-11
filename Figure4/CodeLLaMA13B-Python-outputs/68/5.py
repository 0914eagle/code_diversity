def pluck(arr):
    
    if len(arr) == 0:
        return []
    evens = [x for x in arr if x % 2 == 0]
    if len(evens) == 0:
        return []
    return [min(evens), arr.index(min(evens))]


if __name__ == "__main__":
    assert pluck([4, 2, 3]) == [2, 1]
    assert pluck([1, 2