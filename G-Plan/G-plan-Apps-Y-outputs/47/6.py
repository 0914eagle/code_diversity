
def color_string(n, s):
    colors = {}
    color_count = 0
    for char in s:
        if char not in colors:
            color_count += 1
            colors[char] = color_count
    print(color_count)
    print(" ".join(str(colors[char]) for char in s))

if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    color_string(n, s)
