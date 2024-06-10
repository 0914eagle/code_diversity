
def count_takahashi_dates(a, b):
    return min(a, b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    result = count_takahashi_dates(a, b)
    print(result)
