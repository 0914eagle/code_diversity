
def get_large_bouquets(n, a):
    large_bouquets = 0
    for i in range(n):
        if a[i] % 2 == 1:
            large_bouquets += 1
        else:
            for j in range(i+1, n):
                if a[i] + a[j] % 2 == 1:
                    large_bouquets += 1
                    break
    return large_bouquets

