
def min_90_degree_turns(x):
    min_turns = abs(x) % 360 // 90 + (1 if abs(x) % 360 != 0 else 0)
    return min_turns

if __name__ == "__main__":
    x = int(input())
    print(min_90_degree_turns(x))
