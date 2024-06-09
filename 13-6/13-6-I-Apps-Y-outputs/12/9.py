
def is_triangle_possible(sticks):
    sticks.sort()
    for i in range(len(sticks)):
        if sticks[i] < sticks[i-1] + sticks[i-2]:
            return "possible"
    return "impossible"

def main():
    num_sticks = int(input())
    sticks = list(map(int, input().split()))
    print(is_triangle_possible(sticks))

if __name__ == '__main__':
    main()

