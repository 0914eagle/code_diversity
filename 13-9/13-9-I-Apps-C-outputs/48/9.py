
def predict_temperature(temperatures):
    n = len(temperatures)
    if n == 1:
        return temperatures[0]
    else:
        ap = is_arithmetic_progression(temperatures)
        if ap:
            a, d = temperatures[0], temperatures[1] - temperatures[0]
            return a + (n + 1) * d
        else:
            return temperatures[n - 1]

def is_arithmetic_progression(temperatures):
    n = len(temperatures)
    if n == 1:
        return True
    else:
        a, d = temperatures[0], temperatures[1] - temperatures[0]
        for i in range(2, n):
            if temperatures[i] != a + i * d:
                return False
        return True

temperatures = [int(input()) for _ in range(int(input()))]
print(predict_temperature(temperatures))

