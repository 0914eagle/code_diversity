
def can_remove_elements(arr):
    # Check if all elements in the array are the same
    if len(set(arr)) == 1:
        return True
    
    # Check if any two elements differ by more than 1
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) > 1:
                return False
    
    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print("YES" if can_remove_elements(arr) else "NO")

if __name__ == '__main__':
    main()

