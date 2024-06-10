
def get_immediate_subordinates(bosses):
    subordinates = [0] * len(bosses)
    for i in range(1, len(bosses)):
        subordinates[bosses[i]] += 1
    return subordinates

def main():
    n = int(input())
    bosses = list(map(int, input().split()))
    subordinates = get_immediate_subordinates(bosses)
    for i in range(n):
        print(subordinates[i])

if __name__ == '__main__':
    main()

