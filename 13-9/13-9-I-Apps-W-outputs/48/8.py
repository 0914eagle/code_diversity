
def get_result(upvotes, downvotes, unknown):
    total_votes = upvotes + downvotes
    if upvotes > downvotes:
        return "+"
    elif downvotes > upvotes:
        return "-"
    else:
        return "0"

def is_result_uncertain(upvotes, downvotes, unknown):
    total_votes = upvotes + downvotes
    if unknown == 0:
        return False
    elif total_votes == 0:
        return True
    else:
        return unknown > total_votes // 2

if __name__ == '__main__':
    upvotes, downvotes, unknown = map(int, input().split())
    result = get_result(upvotes, downvotes, unknown)
    if is_result_uncertain(upvotes, downvotes, unknown):
        print("?")
    else:
        print(result)

