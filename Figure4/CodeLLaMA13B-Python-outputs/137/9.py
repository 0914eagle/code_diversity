def compare_one(a, b):
    

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None


print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
