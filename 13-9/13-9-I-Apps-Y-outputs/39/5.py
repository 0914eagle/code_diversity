
def is_possible(a, b, c):
    # Initialize a list to store the selected integers
    selected_integers = []
    
    # Loop through all multiples of a until the sum is congruent to c modulo b
    for i in range(a, b+1, a):
        selected_integers.append(i)
        if sum(selected_integers) % b == c:
            return True
    
    # If the sum is not congruent to c modulo b after looping through all multiples of a, return False
    return False

def main():
    a, b, c = map(int, input().split())
    if is_possible(a, b, c):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

