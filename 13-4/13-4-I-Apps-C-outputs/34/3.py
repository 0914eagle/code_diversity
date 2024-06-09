
def count_powers_of_two(n, e):
    count = 0
    for i in range(n+1):
        if str(i).find(str(2**e)) != -1:
            count += 1
    return count

def main():
    n, e = map(int, input().split())
    print(count_powers_of_two(n, e))

if __name__ == '__main__':
    main()

