
def can_divide_array(a):
    # Calculate the sum of all elements in the array
    sum_array = sum(a)
    # Calculate the sum of elements in the first half of the array
    sum_first_half = sum(a[:len(a)//2])
    # Check if the sum of elements in the first half is equal to the sum of elements in the second half
    if sum_first_half == sum_array - sum_first_half:
        return True
    else:
        return False

def move_element(a, index, new_index):
    # Move the element at the given index to the new index
    a.insert(new_index, a.pop(index))
    return a

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # Check if the array can be divided after moving one element
    if can_divide_array(a):
        print("YES")
    else:
        # Find the index of the element that can be moved to divide the array
        for i in range(len(a)):
            for j in range(len(a)):
                if i != j and can_divide_array(move_element(a, i, j)):
                    print("YES")
                    break
            else:
                continue
            break
        else:
            print("NO")

