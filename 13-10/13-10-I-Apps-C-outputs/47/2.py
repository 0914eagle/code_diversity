
def get_skill_level(player_id, match_list):
    skill_level = 0
    for match in match_list:
        if match[0] == player_id:
            skill_level += 1
        elif match[1] == player_id:
            skill_level -= 1
    return skill_level

def is_consistent(match_list):
    skill_levels = []
    for i in range(len(match_list)):
        skill_levels.append(get_skill_level(i, match_list))
    for i in range(len(match_list)):
        for j in range(i+1, len(match_list)):
            if skill_levels[i] > skill_levels[j] and match_list[i][1] != match_list[j][0]:
                return False
    return True

def main():
    num_players, num_matches = map(int, input().split())
    match_list = []
    for _ in range(num_matches):
        match = list(map(int, input().split()))
        match_list.append(match)
    print("consistent" if is_consistent(match_list) else "inconsistent")

if __name__ == '__main__':
    main()

