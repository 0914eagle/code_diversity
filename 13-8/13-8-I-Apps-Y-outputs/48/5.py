
def get_correct_choice(A, B):
    # Convert A and B to sets to remove duplicates
    A_set = set(A)
    B_set = set(B)
    
    # Find the element that is not in both sets
    correct_choice = A_set.symmetric_difference(B_set).pop()
    
    return correct_choice

def main():
    A, B = map(int, input().split())
    print(get_correct_choice(A, B))

if __name__ == '__main__':
    main()

