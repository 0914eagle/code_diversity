def pluck(arr):
    
    if not arr:
        return []
    even_min = min([x for x in arr if x % 2 == 0])
    return [even_min, arr.index(even_min)]


if __name__ == "__main__":
    print(pluck([4,2,3]))
    print(pluck([1,2,3]))
    print(pluck([]))
    print(pluck([5, 0, 3, 0, 4, 2]))
