
def get_max_value(S):
    x = 0
    max_value = 0
    for i in range(len(S)):
        if S[i] == "I":
            x += 1
        else:
            x -= 1
        max_value = max(max_value, x)
    return max_value

def main():
    N = int(input())
    S = input()
    print(get_max_value(S))

if __name__ == '__main__':
    main()

