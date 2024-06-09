
def get_adjacent_islands(n, a, b):
    # Find the empty pedestal and the island with the desired statue
    empty_pedestal = a.index(0)
    desired_statue = b[empty_pedestal]

    # Find the island directly adjacent to the empty pedestal
    adjacent_island = (empty_pedestal - 1) % n
    if adjacent_island < 0:
        adjacent_island += n

    # Check if the island with the desired statue is adjacent to the empty pedestal
    if b[adjacent_island] == desired_statue:
        return True
    else:
        return False

def is_rearrangement_possible(n, a, b):
    # Base case: If the number of islands is 1, return True
    if n == 1:
        return True

    # Recursive case: If the number of islands is greater than 1, check if the islanders can rearrange the statues in the existing network
    if get_adjacent_islands(n, a, b):
        # If the islanders can move the statue in the existing network, recursively check if the islanders can rearrange the statues in the remaining islands
        return is_rearrangement_possible(n-1, a, b)
    else:
        # If the islanders cannot move the statue in the existing network, return False
        return False

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES") if is_rearrangement_possible(n, a, b) else print("NO")

