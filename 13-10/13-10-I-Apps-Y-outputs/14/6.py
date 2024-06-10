
def get_groups(N):
    groups = []
    for i in range(1, N+1):
        if i % 3 == 0:
            groups.append(i)
    return len(groups)

def main():
    N = int(input())
    print(get_groups(N))

if __name__ == '__main__':
    main()

