year_name(s, t, year):
    n = len(s)
    m = len(t)
    idx_s = (year - 1) % n
    idx_t = (year - 1) % m
    return s[idx_s] + t[idx_t]

if __name__ == "__main__":
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    q = int(input())
    
    for _ in range(q):
        year = int(input())
        print(get_year_name(s, t, year))
