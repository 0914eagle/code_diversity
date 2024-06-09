
def is_non_decreasing(heights):
    for i in range(len(heights) - 1):
        if heights[i] > heights[i + 1]:
            return False
    return True

def solve(heights):
    for i in range(len(heights)):
        if heights[i] > 1:
            heights[i] -= 1
            if is_non_decreasing(heights):
                return "Yes"
            heights[i] += 1
    return "No"

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(solve(heights))

