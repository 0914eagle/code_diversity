
def solve(K):
    snuke_numbers = []
    for i in range(1, 10**15):
        if is_snuke_number(i):
            snuke_numbers.append(i)
            if len(snuke_numbers) == K:
                break
    return snuke_numbers

def is_snuke_number(n):
    s = sum(int(digit) for digit in str(n))
    for m in range(n+1, 10**15):
        if s > sum(int(digit) for digit in str(m)):
            return False
    return True

