
def split_integer(n, values):
    values.sort(reverse=True)
    alice_sum = 0
    bob_sum = 0
    for i in range(n):
        if i % 2 == 0:
            alice_sum += values[i]
        else:
            bob_sum += values[i]
    return alice_sum, bob_sum

def main():
    n = int(input())
    values = list(map(int, input().split()))
    alice_sum, bob_sum = split_integer(n, values)
    print(alice_sum, bob_sum)

if __name__ == '__main__':
    main()

