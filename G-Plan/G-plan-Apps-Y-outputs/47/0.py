
def color_string(n, s):
    colors = {}
    color = 1
    for char in s:
        if char not in colors:
            colors[char] = color
            color += 1
    print(len(colors))
    print(" ".join(str(colors[char]) for char in s))

if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    color_string(n, s)
