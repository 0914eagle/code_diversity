
def get_max_value(N, S):
    x = 0
    for i in range(N):
        if S[i] == "I":
            x += 1
        else:
            x -= 1
    return max(x, 0)

def main():
    N = int(input())
    S = input()
    print(get_max_value(N, S))

if __name__ == '__main__':
    main()

