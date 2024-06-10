
def can_divide(arr):
    # Calculate the sum of the elements in the array
    sum_arr = sum(arr)
    # Calculate the sum of the elements in the first half of the array
    sum_first_half = sum(arr[:len(arr)//2])
    # Calculate the sum of the elements in the second half of the array
    sum_second_half = sum(arr[len(arr)//2:])
    # If the sums of the first and second half are equal, return True
    if sum_first_half == sum_second_half:
        return True
    # If the sums of the first and second half are not equal, try moving an element to the other half
    for i in range(len(arr)):
        # If the element is in the first half, move it to the second half
        if i < len(arr)//2:
            arr.append(arr.pop(i))
        # If the element is in the second half, move it to the first half
        else:
            arr.insert(0, arr.pop(i))
        # Calculate the new sum of the first half
        sum_first_half = sum(arr[:len(arr)//2])
        # Calculate the new sum of the second half
        sum_second_half = sum(arr[len(arr)//2:])
        # If the sums of the first and second half are equal, return True
        if sum_first_half == sum_second_half:
            return True
    # If no move can make the division possible, return False
    return False

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    if can_divide(arr):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

