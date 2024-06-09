
def is_postal_code(A, B, S):
    if len(S) != A + B + 1:
        return "No"
    if S[A] != "-":
        return "No"
    if not S[A+1:].isdigit():
        return "No"
    return "Yes"

def main():
    A, B = map(int, input().split())
    S = input()
    print(is_postal_code(A, B, S))

if __name__ == '__main__':
    main()

