
def read_input():
    n = int(input())
    top_left_corners = []
    bottom_right_corners = []
    for i in range(n):
        r, c = map(int, input().split())
        top_left_corners.append((r, c))
        r, c = map(int, input().split())
        bottom_right_corners.append((r, c))
    return n, top_left_corners, bottom_right_corners

def is_valid_matching(n, top_left_corners, bottom_right_corners):
    for i in range(n):
        for j in range(i+1, n):
            if top_left_corners[i] == bottom_right_corners[j]:
                return False
            if bottom_right_corners[i] == top_left_corners[j]:
                return False
    return True

def find_matching(n, top_left_corners, bottom_right_corners):
    matching = []
    for i in range(n):
        for j in range(n):
            if top_left_corners[i] == bottom_right_corners[j]:
                matching.append((i, j))
                break
    return matching

def print_output(n, matching):
    for i, j in matching:
        print(i+1, j+1)

def main():
    n, top_left_corners, bottom_right_corners = read_input()
    if not is_valid_matching(n, top_left_corners, bottom_right_corners):
        print("syntax error")
    else:
        matching = find_matching(n, top_left_corners, bottom_right_corners)
        print_output(n, matching)

if __name__ == '__main__':
    main()

