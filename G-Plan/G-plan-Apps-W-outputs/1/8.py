
def min_turns_needed(camera_angle):
    min_turns = abs(camera_angle) % 360 // 90 + (1 if abs(camera_angle) % 360 != 0 else 0)
    return min_turns

if __name__ == "__main__":
    camera_angle = int(input())
    print(min_turns_needed(camera_angle))
