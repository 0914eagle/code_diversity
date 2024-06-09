
def xor_angles(n):
    count = 0
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            c = a ^ b ^ n
            if a <= c <= b:
                count += 1
    return count

