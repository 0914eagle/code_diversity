def compare_one(a, b):
    
    if a == b:
        return None
    elif type(a) == type(b):
        return max(a, b)
    else:
        if type(a) == int:
            return int(max(a, float(b)))
        else:
            return float(max(float(a), b))


print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
