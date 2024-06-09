
def f1(N, L):
    # Calculate the sum of the flavors of all apples
    total_flavor = sum(range(L, L+N))
    # Calculate the sum of the flavors of the remaining apples after eating one
    remaining_flavor = sum(range(L+1, L+N))
    # Return the difference between the two sums
    return abs(total_flavor - remaining_flavor)

def f2(N, L):
    # Calculate the sum of the flavors of all apples
    total_flavor = sum(range(L, L+N))
    # Calculate the sum of the flavors of the remaining apples after eating one
    remaining_flavor = sum(range(L+1, L+N))
    # Return the difference between the two sums
    return abs(total_flavor - remaining_flavor)

if __name__ == '__main__':
    N, L = map(int, input().split())
    print(f1(N, L))
    print(f2(N, L))

