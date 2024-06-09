
def f1(n, p, q, a, b):
    # Calculate the total experience and money gained from working on all projects
    total_experience = sum(a)
    total_money = sum(b)
    
    # Initialize the minimum number of days needed to achieve the dream
    min_days = 0
    
    # Loop through each project and calculate the number of days needed to achieve the dream
    for i in range(n):
        # Calculate the number of days needed to gain the required experience and money from this project
        days_needed = (p - total_experience) / a[i]
        days_needed += (q - total_money) / b[i]
        
        # Update the minimum number of days needed to achieve the dream
        min_days = max(min_days, days_needed)
    
    return min_days

def f2(...):
    # Your code here

if __name__ == '__main__':
    n = int(input())
    p = int(input())
    q = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(n, p, q, a, b))

