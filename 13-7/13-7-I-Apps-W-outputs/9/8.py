
def get_friends(friends_list, k):
    friends = set()
    for friend in friends_list:
        if friend[0] not in friends:
            friends.add(friend[0])
        if friend[1] not in friends:
            friends.add(friend[1])
    return list(friends)

def get_predicted_friends(friends_list, k):
    predicted_friends = {}
    for friend in friends_list:
        if friend[0] not in predicted_friends:
            predicted_friends[friend[0]] = set()
        if friend[1] not in predicted_friends:
            predicted_friends[friend[1]] = set()
        predicted_friends[friend[0]].add(friend[1])
        predicted_friends[friend[1]].add(friend[0])
    for user in predicted_friends:
        predicted_friends[user] = list(predicted_friends[user])
    return predicted_friends

def main():
    m, k = map(int, input().split())
    friends_list = []
    for i in range(m):
        a, b = map(int, input().split())
        friends_list.append((a, b))
    friends = get_friends(friends_list, k)
    predicted_friends = get_predicted_friends(friends_list, k)
    for user in sorted(predicted_friends):
        print(f"{user}: {len(predicted_friends[user])}")
        for friend in predicted_friends[user]:
            print(friend, end=" ")
        print()

if __name__ == '__main__':
    main()

