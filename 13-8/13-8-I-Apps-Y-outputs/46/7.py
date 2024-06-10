
def get_input():
    n = int(input())
    values = list(map(int, input().split()))
    return n, values

def get_largest_sum(values):
    values.sort(reverse=True)
    alice_sum = 0
    bob_sum = 0
    for i in range(len(values)):
        if i % 2 == 0:
            alice_sum += values[i]
        else:
            bob_sum += values[i]
    return alice_sum, bob_sum

def main():
    n, values = get_input()
    alice_sum, bob_sum = get_largest_sum(values)
    print(alice_sum, bob_sum)

if __name__ == '__main__':
    main()

