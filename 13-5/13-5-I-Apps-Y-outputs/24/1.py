
def is_good_number(n):
    if n == 1:
        return True
    
    while n > 1:
        if n % 3 != 0:
            return False
        n //= 3
    
    return True

def find_next_good_number(n):
    m = n
    while not is_good_number(m):
        m += 1
    
    return m

q = int(input())
for _ in range(q):
    n = int(input())
    print(find_next_good_number(n))

