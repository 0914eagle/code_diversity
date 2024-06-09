
def is_haiku(phrases):
    A, B, C = phrases
    return A + B + C == 17 and B - A == 2 and C - B == 2

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print("YES" if is_haiku((A, B, C)) else "NO")

