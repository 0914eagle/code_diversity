
def is_possible(n):
    for a in range(n//1234567+1):
        b = (n-a*1234567)//123456
        if b*(123456+1234567) > n:
            break
        c = (n-a*1234567-b*123456)//1234
        if a*1234567+b*123456+c*1234 == n:
            return "YES"
    return "NO"

