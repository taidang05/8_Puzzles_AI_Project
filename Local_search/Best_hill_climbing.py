from helper import apply_action, get_actions, manhattan_distance,state_to_tuple


def steepest_ascent_hill_climbing(initial_state, goal_state):
    current_state = initial_state
    current_h = manhattan_distance(current_state, goal_state)
    path = []  # Lưu đường đi
    nodes_expanded = 0  
    while True:
        nodes_expanded += 1
        actions = get_actions(current_state)
        if current_h == 0:  # Đích 
            print(path)
            return path,len(path),nodes_expanded

        best_state = current_state
        best_h = current_h
        best_action = None

        for action in actions:
            new_state = apply_action(current_state, action)
            new_h = manhattan_distance(new_state, goal_state)
            if new_h < best_h:
                best_state = new_state
                best_h = new_h
                best_action = action

        if best_h < current_h:
            current_state = best_state
            current_h = best_h
            path.append(best_action)  # Thêm hành động vào đường đi
        else:
            return path,len(path),nodes_expanded
