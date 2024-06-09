
def check_postal_code(A, B, S):
    if len(S) != A + B + 1:
        return "No"
    if S[A] != "-":
        return "No"
    for i in range(A + 1, len(S)):
        if not S[i].isdigit():
            return "No"
    return "Yes"

def main():
    A, B = map(int, input().split())
    S = input()
    print(check_postal_code(A, B, S))

if __name__ == '__main__':
    main()

