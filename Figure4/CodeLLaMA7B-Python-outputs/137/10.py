def compare_one(a, b):
    
    if a == b:
        return None
    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    if isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    if isinstance(a, str) and isinstance(b, str):
        return max(a, b)
    if isinstance(a, int) and isinstance(b, float):
        return max(a, b)
    if isinstance(a, float) and isinstance(b, int):
        return max(a, b)
    if isinstance(a, int) and isinstance(b, str):
        return max(a, b)
    if isinstance(a, str) and isinstance(b, int):
        return max(a, b)
    if isinstance(a, float) and isinstance(b, str):
        return max(a, b)
    if isinstance(a, str) and isinstance(b, float):
        return max(a, b)


print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
