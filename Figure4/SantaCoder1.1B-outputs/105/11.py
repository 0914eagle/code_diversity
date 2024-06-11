def by_length(arr):
    
    if not arr:
        return []
    arr.sort()
    arr = [str(i) for i in arr]
    arr = [i.replace("One", "Eight").replace("Two", "Five").replace("Three", "Four").replace("Four", "Three").replace("Five", "Two").replace("Six", "One").replace("Seven", "One").replace("Eight", "One").replace("Nine", "One")]
    return arr

