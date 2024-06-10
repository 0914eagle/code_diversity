
def get_time_needed(start_section, end_section, n_floors, m_sections, c_l, c_e, v, q):
    # Initialize a dictionary to store the time needed to reach each section from the start section
    time_needed = {start_section: 0}
    
    # Loop through each section and calculate the time needed to reach it from the start section
    for section in range(1, m_sections + 1):
        if section == start_section:
            continue
        elif section in c_l:
            time_needed[section] = time_needed[section - 1] + 1
        elif section in c_e:
            time_needed[section] = time_needed[section - 1] + v
        else:
            time_needed[section] = time_needed[section - 1] + 1
    
    # Loop through each query and calculate the minimum time needed to reach the end section
    for query in range(q):
        start_floor, start_section = map(int, input().split())
        end_floor, end_section = map(int, input().split())
        time_needed_query = 0
        if start_floor == end_floor:
            time_needed_query = time_needed[end_section] - time_needed[start_section]
        elif abs(start_floor - end_floor) == 1:
            time_needed_query = time_needed[end_section] - time_needed[start_section] + v
        else:
            time_needed_query = time_needed[end_section] - time_needed[start_section] + (abs(start_floor - end_floor) - 1) * v
        print(time_needed_query)
    
def main():
    n_floors, m_sections, c_l, c_e, v = map(int, input().split())
    q = int(input())
    get_time_needed(1, 1, n_floors, m_sections, c_l, c_e, v, q)

if __name__ == '__main__':
    main()

