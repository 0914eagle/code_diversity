year_name(n, m, s, t, q, years):
    def get_name(year):
        idx_s = (year - 1) % n
        idx_t = (year - 1) % m
        return s[idx_s] + t[idx_t]

    names = [get_name(year) for year in years]
    return names


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    q = int(input())
    years = [int(input()) for _ in range(q)]

    names = get_year_name(n, m, s, t, q, years)
    for name in names:
        print(name)