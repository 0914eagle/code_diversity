
def f1(n, k, d, s):
    # Calculate the average difficulty of the solved problems
    avg_solved = s * k / n
    
    # Calculate the average difficulty of the unsolved problems
    avg_unsolved = (d - avg_solved) * (n - k) / n
    
    # Check if the average difficulty of the unsolved problems is possible
    if avg_unsolved < 0 or avg_unsolved > 100:
        return "impossible"
    else:
        return round(avg_unsolved, 6)

def f2(...):
    # Calculate the average difficulty of the solved problems
    avg_solved = s * k / n
    
    # Calculate the average difficulty of the unsolved problems
    avg_unsolved = (d - avg_solved) * (n - k) / n
    
    # Check if the average difficulty of the unsolved problems is possible
    if avg_unsolved < 0 or avg_unsolved > 100:
        return "impossible"
    else:
        return round(avg_unsolved, 6)

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    d = int(input())
    s = int(input())
    print(f1(n, k, d, s))
    print(f2(n, k, d, s))

