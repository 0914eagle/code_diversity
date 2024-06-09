
def solve(n, d, r):
    # Calculate the expected number of gems after d nights
    expected_gems = 1
    for i in range(d):
        expected_gems = expected_gems * (n + 1) / n
    
    # Calculate the expected number of gems held by the top r inhabitants
    expected_top_r_gems = 0
    for i in range(r):
        expected_top_r_gems += expected_gems * i / n
    
    return expected_top_r_gems

