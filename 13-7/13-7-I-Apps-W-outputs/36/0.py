
def find_subsequence(a, b):
    # Find the longest common subsequence of a and b
    lcs = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                lcs.append(a[i])
                break
    # If the longest common subsequence is not empty, return it
    if lcs:
        return lcs
    # If the longest common subsequence is empty, return False
    else:
        return False

def main():
    # Read the input data
    with open("input.txt", "r") as f:
        t = int(f.readline())
        for _ in range(t):
            n, m = map(int, f.readline().split())
            a = list(map(int, f.readline().split()))
            b = list(map(int, f.readline().split()))
            # Call the find_subsequence function and print the result
            result = find_subsequence(a, b)
            if result:
                print("YES")
                print(len(result))
                print(" ".join(map(str, result)))
            else:
                print("NO")

if __name__ == '__main__':
    main()

