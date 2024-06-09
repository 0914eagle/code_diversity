
def is_possible(n):
    for a in range(n//1234567+1):
        for b in range(n//123456+1):
            if n-a*1234567-b*123456 in [0, 1234]:
                return "YES"
    return "NO"

