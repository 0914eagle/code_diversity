
def is_multiple_of_A(n, A):
    return n % A == 0

def get_sum_congruent_to_C_modulo_B(A, B, C):
    # Initialize a list to store the selected integers
    selected_integers = []

    # Iterate from 1 to infinity
    for i in range(1, float('inf')):
        # Check if the current integer is a multiple of A
        if is_multiple_of_A(i, A):
            # Add the current integer to the list of selected integers
            selected_integers.append(i)

            # Check if the sum of the selected integers is congruent to C modulo B
            if sum(selected_integers) % B == C:
                # If it is, return YES
                return "YES"

    # If we reach this point, it means that no combination of selected integers results in a sum congruent to C modulo B
    # Return NO
    return "NO"

if __name__ == '__main__':
    A, B, C = map(int, input().split())
    print(get_sum_congruent_to_C_modulo_B(A, B, C))

