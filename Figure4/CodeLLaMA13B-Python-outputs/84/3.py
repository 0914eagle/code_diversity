def solve(N):
    
    # your code here
    return bin(N).replace("0b", "")

if __name__ == "__main__":
    print(solve(1000))