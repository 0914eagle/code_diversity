
def get_number_of_integers_with_odd_digits(N):
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

def main():
    N = int(input())
    print(get_number_of_integers_with_odd_digits(N))

if __name__ == '__main__':
    main()

