
def f1(h1, a1, x1, y1, h2, a2, x2, y2):
    # Calculate the minimum time it takes for Xaniar to reach a1
    time_xaniar = (a1 - h1) // x1 + 1
    
    # Calculate the minimum time it takes for Abol to reach a2
    time_abol = (a2 - h2) // x2 + 1
    
    # Return the minimum of the two times
    return min(time_xaniar, time_abol)

def f2(h1, a1, x1, y1, h2, a2, x2, y2):
    # Calculate the minimum time it takes for Xaniar to reach a1
    time_xaniar = (a1 - h1) // x1 + 1
    
    # Calculate the minimum time it takes for Abol to reach a2
    time_abol = (a2 - h2) // x2 + 1
    
    # Return the minimum of the two times
    return min(time_xaniar, time_abol)

if __name__ == '__main__':
    m = int(input())
    h1, a1 = map(int, input().split())
    x1, y1 = map(int, input().split())
    h2, a2 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    print(f1(h1, a1, x1, y1, h2, a2, x2, y2))

