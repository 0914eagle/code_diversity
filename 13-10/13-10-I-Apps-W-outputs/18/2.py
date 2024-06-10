
def get_last_cafe(cafes):
    last_visit = max(cafes)
    for i in range(len(cafes)):
        if cafes[i] == last_visit:
            return i

def solve(n, cafes):
    cafes.sort()
    last_cafe = get_last_cafe(cafes)
    return last_cafe + 1

if __name__ == '__main__':
    n = int(input())
    cafes = list(map(int, input().split()))
    print(solve(n, cafes))

