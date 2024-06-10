
def get_appearances(table, a, b):
    appearances = 0
    for i in range(a, b+1):
        appearances += table[i]
    return appearances

def main():
    q = int(input())
    table = [0] * 1000000001
    table[1] = 1
    for i in range(2, 1000000001):
        table[i] = table[i-1] + int(str(table[i-1])[::-1])
    for i in range(q):
        a, b = map(int, input().split())
        print(get_appearances(table, a, b))

if __name__ == '__main__':
    main()

