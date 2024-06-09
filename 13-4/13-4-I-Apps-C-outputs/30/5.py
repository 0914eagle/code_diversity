
def get_badge_numbers(start_room, end_room, locks):
    visited = set()
    queue = [(start_room, 0)]
    while queue:
        current_room, badge_number = queue.pop(0)
        if current_room == end_room:
            visited.add(badge_number)
            continue
        for lock in locks:
            if lock[0] == current_room and lock[1] == end_room and lock[2] <= badge_number <= lock[3]:
                visited.add(badge_number)
                break
            elif lock[0] == current_room and lock[1] != end_room and lock[2] <= badge_number <= lock[3]:
                queue.append((lock[1], badge_number))
                break
    return len(visited)

