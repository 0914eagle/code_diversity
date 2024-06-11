def pluck(arr):
    
    if not arr:
        return []
    evens = [x for x in arr if x % 2 == 0]
    if not evens:
        return []
    return [min(evens), arr.index(min(evens))]


if __name__ == "__main__":
    assert pluck([4, 2, 3]) == [2