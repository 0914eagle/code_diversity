
def get_vertical_dominoes(s):
    n = len(s)
    dominoes = [0] * n
    for i in range(n):
        if s[i] == "L":
            dominoes[i] -= 1
        elif s[i] == "R":
            dominoes[i] += 1
    for i in range(1, n):
        dominoes[i] += dominoes[i-1]
    return sum(1 for x in dominoes if x != 0)

def main():
    n = int(input())
    s = input()
    print(get_vertical_dominoes(s))

if __name__ == '__main__':
    main()

