
def is_wall_completed(a):
    # Check if all parts of the wall have the same height
    if len(set(a)) == 1:
        return True

    # Check if the wall has no empty spaces inside it
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            return False

    return True


n = int(input())
a = list(map(int, input().split()))

if is_wall_completed(a):
    print("YES")
else:
    print("NO")

