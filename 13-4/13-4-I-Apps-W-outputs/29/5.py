
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
    for i in range(n+1, 10**15):
        if sum(int(digit) for digit in str(i)) <= s:
            return False
    return True

