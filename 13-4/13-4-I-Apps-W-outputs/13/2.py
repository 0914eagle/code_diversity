
import sys
import math

def f1(N, K):
    # f1 should return the priority value for a patient with severity S and waiting time W
    return S + K * W

def f2(T, M, S):
    # f2 should return the name of the patient who will be treated next
    return M

def f3(T, M):
    # f3 should return the name of the patient who will be treated next
    return M

if __name__ == '__main__':
    N, K = map(int, input().split())
    patients = []
    for i in range(N):
        Q, T, M, S = map(int, input().split())
        if Q == 1:
            patients.append((T, M, S))
        elif Q == 2:
            if not patients:
                print("doctor takes a break")
            else:
                patient = max(patients, key=lambda x: f1(x[2], K))
                print(patient[1])
                patients.remove(patient)
        elif Q == 3:
            if M in [p[1] for p in patients]:
                patients.remove((T, M, S))
            else:
                print("false alarm")

