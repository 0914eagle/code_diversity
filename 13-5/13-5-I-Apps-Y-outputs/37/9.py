
def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

def can_finish_all_assignments(N, M, A):
    days_spent = 0
    for i in range(M):
        days_spent += A[i]
        if days_spent > N:
            return False
    return True

def get_max_hangout_days(N, M, A):
    if not can_finish_all_assignments(N, M, A):
        return -1
    
    days_spent = 0
    max_hangout_days = 0
    for i in range(M):
        days_spent += A[i]
        max_hangout_days = max(max_hangout_days, N - days_spent)
    return max_hangout_days

if __name__ == '__main__':
    N, M, A = get_input()
    print(get_max_hangout_days(N, M, A))

