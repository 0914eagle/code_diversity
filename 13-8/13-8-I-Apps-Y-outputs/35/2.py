
def get_immediate_subordinates(members, bosses):
    subordinates = [0] * len(members)
    for i in range(1, len(members)):
        subordinates[bosses[i]] += 1
    return subordinates

def main():
    members = int(input())
    bosses = list(map(int, input().split()))
    subordinates = get_immediate_subordinates(members, bosses)
    for i in range(members):
        print(subordinates[i])

if __name__ == '__main__':
    main()

