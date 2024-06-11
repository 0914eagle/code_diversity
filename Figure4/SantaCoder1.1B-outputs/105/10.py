def by_length(arr):
    
    if not arr:
        return []
    arr = sorted(arr)
    arr = [str(i) for i in arr]
    arr = [i.replace('One', 'Eight').replace('Two', 'Five').replace('Three', 'Four').replace('Four', 'Three').replace('Five', 'Two').replace('Six', 'One').replace('Seven', 'Two').replace('Eight', 'One').replace('Nine', 'One')]
    return arr

