
def get_months(n, days):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_in_year = 12
    years = int(n / months_in_year)
    months_left = n % months_in_year
    total_days = 0
    for i in range(years):
        for j in range(months_in_year):
            total_days += months[j]
        if total_days == days:
            return "YES"
        total_days = 0
    for i in range(months_left):
        total_days += months[i]
        if total_days == days:
            return "YES"
        total_days = 0
    return "NO"

def main():
    n = int(input())
    days = list(map(int, input().split()))
    print(get_months(n, days))

if __name__ == '__main__':
    main()

