import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper import apply_action, get_actions, state_to_tuple


def depth_limited_search(state, goal_state, actions, depth_limit, visited, curDepth, nodes_expanded):
    """
    Depth-Limited Search (DLS) sử dụng đệ quy cho bài toán 8-Puzzle.
    Trả về danh sách hành động nếu tìm thấy đích, None nếu không.
    """
    if curDepth > depth_limit:
        return None, 0, nodes_expanded
    
    if state == goal_state:
        return actions, len(actions), nodes_expanded

    for action in get_actions(state):
        new_state = apply_action(state, action)
        new_state_tuple = state_to_tuple(new_state)

        if new_state_tuple not in visited:
            visited.add(new_state_tuple)
            nodes_expanded += 1
            result, cost, space = depth_limited_search(new_state, goal_state, actions + [action], depth_limit, visited, curDepth + 1, nodes_expanded)
            if result is not None:
                return result, cost, space
            visited.remove(new_state_tuple)

    return None, 0, nodes_expanded

def ids(initial_state, goal_state):
    """
    Iterative Deepening Search (IDS) cho bài toán 8-Puzzle.
    Trả về danh sách hành động dẫn đến đích, hoặc None nếu không tìm thấy.
    """
    depth_limit = 0 
    while True:
        visited = set()
        state_tuple = state_to_tuple(initial_state)
        visited.add(state_tuple)
        result, cost, space = depth_limited_search(initial_state, goal_state, [], depth_limit, visited, 0, 0)
        if result is not None:
            return result, cost, space
        depth_limit += 1
        print(depth_limit)

