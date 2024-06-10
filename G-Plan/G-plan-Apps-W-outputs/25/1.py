year_name(n, m, s, t, q, years):
    def get_name(year):
        s_idx = (year - 1) % n
        t_idx = (year - 1) % m
        return s[s_idx] + t[t_idx]

    result = []
    for year in years:
        result.append(get_name(year))
    
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    q = int(input())
    years = [int(input()) for _ in range(q)]

    result = get_year_name(n, m, s, t, q, years)
    for name in result:
        print(name)
