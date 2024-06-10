
def get_max_value(S):
    x = 0
    for s in S:
        if s == "I":
            x += 1
        else:
            x -= 1
    return x

def main():
    N = int(input())
    S = input()
    print(get_max_value(S))

if __name__ == '__main__':
    main()

