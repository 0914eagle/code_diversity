
def get_snukes(k):
    snukes = []
    for i in range(1, 10**15):
        if is_snukes(i):
            snukes.append(i)
            if len(snukes) == k:
                break
    return snukes

def is_snukes(n):
    s = sum(int(digit) for digit in str(n))
    for m in range(n+1, 10**15):
        if s > sum(int(digit) for digit in str(m)):
            return False
    return True

