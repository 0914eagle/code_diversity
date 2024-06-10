
def count_takahashi_dates(a, b):
    return min(a, b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(count_takahashi_dates(a, b))
