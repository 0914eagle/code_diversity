def compare_one(a, b):
    
    if a > b:
        return a
    if b > a:
        return b
    return None


print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
