
def is_shichi_go_san(n):
    n_str = str(n)
    return '7' in n_str and '5' in n_str and '3' in n_str and len(set(n_str)) == 3

def solve(n):
    count = 0
    for i in range(1, n+1):
        if is_shichi_go_san(i):
            count += 1
    return count

