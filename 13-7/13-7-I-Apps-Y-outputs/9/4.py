
def count_possible_passwords(N):
    return N * N * N

def main():
    N = int(input())
    print(count_possible_passwords(N))

if __name__ == '__main__':
    main()

