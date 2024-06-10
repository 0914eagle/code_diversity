
def min_turns(x):
    return abs(x) % 360 // 90 + (1 if abs(x) % 360 != 0 else 0)

if __name__ == "__main__":
    x = int(input())
    print(min_turns(x))
