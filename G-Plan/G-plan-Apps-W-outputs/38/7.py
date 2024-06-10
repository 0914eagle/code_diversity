
def calculate_rainfall_leak(L, K, T1, T2, H):
    def calculate_water_level(rainfall):
        water_level = 0
        for t in range(int(T1 + T2)):
            if t < T1:
                water_level += rainfall - K
            else:
                water_level -= K
            if water_level < 0:
                water_level = 0
        return water_level

    low = 0
    high = 1000
    while high - low > 1e-6:
        mid = (low + high) / 2
        if calculate_water_level(mid) < H:
            low = mid
        else:
            high = mid

    return low, high

if __name__ == "__main__":
    L, K, T1, T2, H = map(float, input().split())
    result = calculate_rainfall_leak(L, K, T1, T2, H)
    print("{:.6f} {:.6f}".format(result[0], result[1]))
