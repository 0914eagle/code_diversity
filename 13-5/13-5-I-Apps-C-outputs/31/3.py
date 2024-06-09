
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    return N, a

def smash_gems(a, x):
    smashed_gems = set()
    for i in range(len(a)):
        if i % x == 0:
            smashed_gems.add(i)
    return smashed_gems

def get_earned_money(a, smashed_gems):
    earned_money = 0
    for i in range(len(a)):
        if i not in smashed_gems:
            earned_money += a[i]
    return earned_money

def get_max_earned_money(a):
    max_earned_money = 0
    for x in range(1, len(a)):
        smashed_gems = smash_gems(a, x)
        earned_money = get_earned_money(a, smashed_gems)
        if earned_money > max_earned_money:
            max_earned_money = earned_money
    return max_earned_money

if __name__ == '__main__':
    N, a = get_input()
    print(get_max_earned_money(a))

