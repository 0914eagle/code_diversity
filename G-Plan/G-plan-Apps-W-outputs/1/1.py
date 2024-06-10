
def min_turns_to_vertical(x):
    min_turns = abs(x) % 360 // 90 + (1 if abs(x) % 360 != 0 else 0)
    return min_turns

if __name__ == "__main__":
    x = int(input())
    print(min_turns_to_vertical(x))
