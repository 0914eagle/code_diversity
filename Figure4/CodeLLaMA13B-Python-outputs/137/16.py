def compare_one(a, b):
    
    if a == b:
        return None
    if a > b:
        return a
    return b


print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
