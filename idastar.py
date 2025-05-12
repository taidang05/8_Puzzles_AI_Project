from collections import deque
from helper import apply_action, get_actions, manhattan_distance

def ida_star(initial_state, goal_state):
    """
    Tìm đường đi từ initial_state đến goal_state bằng IDA* (dùng đệ quy).
    Trả về danh sách hành động hoặc None nếu không tìm thấy.
    """
    threshold = manhattan_distance(initial_state, goal_state)
    space = [0]     
    while True:
        result, new_threshold = dfs_recursive(initial_state, goal_state, threshold, [], set(),space)
        if result is not None:
            print(f"Found at depth: {len(result)}, actions: {result}")
            return result,len(result),space[0]
        if new_threshold == float('inf'):
            return None,0,space[0]
        threshold = new_threshold

def dfs_recursive(state, goal_state, threshold, actions, visited,space):
    """
    Hàm đệ quy để tìm kiếm theo chiều sâu với ngưỡng threshold.
    """
    f_cost = len(actions) + manhattan_distance(state, goal_state)
    
    if f_cost > threshold:
        return None, f_cost
    
    if state == goal_state:
        return actions, threshold
    
    state_tuple = tuple(map(tuple, state))
    if state_tuple in visited:
        return None, threshold
    
    visited.add(state_tuple)
    min_cost = float('inf')
    
    for action in get_actions(state):
        new_state = apply_action(state, action)
        new_state_tuple = tuple(map(tuple, new_state))
        
        if new_state_tuple not in visited:
            space[0] += 1
            result, cost = dfs_recursive(new_state, goal_state, threshold, actions + [action], visited,space)
            if result is not None:
                return result, threshold
            min_cost = min(min_cost, cost)
    
    return None, min_cost