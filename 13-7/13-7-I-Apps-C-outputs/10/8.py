
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def solve(N, a, b):
    # Initialize the variables
    alf_candy = 0
    beata_candy = 0
    alf_candy_list = []
    beata_candy_list = []
    
    # Loop through the candy list
    for i in range(N):
        # Check if the candy is liked by both siblings
        if a[i] == b[i]:
            # If both like it, give it to Alf
            alf_candy += a[i]
            alf_candy_list.append('A')
        # Check if the candy is liked by only one sibling
        elif a[i] != b[i]:
            # If Alf likes it, give it to Alf
            if a[i] > b[i]:
                alf_candy += a[i]
                alf_candy_list.append('A')
            # If Beata likes it, give it to Beata
            else:
                beata_candy += b[i]
                beata_candy_list.append('B')
    
    # Return the solution
    return ''.join(alf_candy_list)

def main():
    N, a, b = get_input()
    print(solve(N, a, b))

if __name__ == '__main__':
    main()

