
def get_experience_and_money(a, b):
    # Calculate the total experience and money gained from working on all projects
    total_experience = sum(a)
    total_money = sum(b)
    return total_experience, total_money

def get_min_days(a, b, p, q):
    # Initialize variables
    min_days = 0
    experience = 0
    money = 0

    # Loop through each project
    for i in range(len(a)):
        # Calculate the experience and money gained from working on the current project
        experience_i, money_i = get_experience_and_money(a[i], b[i])

        # Check if working on the current project will give us enough experience and money
        if experience_i + experience >= p and money_i + money >= q:
            # If so, return the current number of days
            return min_days
        else:
            # If not, calculate the number of days needed to reach the required experience and money
            days_needed = (p - experience_i - experience) / (experience_i - experience)
            days_needed = max(days_needed, (q - money_i - money) / (money_i - money))

            # Update the minimum number of days and experience and money
            min_days = max(min_days, days_needed)
            experience += experience_i * days_needed
            money += money_i * days_needed

    # If we reach the end of the loop and still don't have enough experience and money, return the current number of days
    return min_days

if __name__ == '__main__':
    n, p, q = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(get_min_days(a, b, p, q))

