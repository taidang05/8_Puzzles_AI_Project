from collections import deque
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper import apply_action, get_actions

def bfs(initial_state, goal_state):
    """
    Tìm đường đi từ trạng thái ban đầu (initial_state) đến trạng thái mục tiêu (goal_state)
    bằng thuật toán tìm kiếm theo chiều rộng (Breadth-First Search).
    Trả về đường đi dưới dạng danh sách các hành động (ví dụ: ["Up", "Left", "Down"]).
    Nếu không tìm thấy đường đi, trả về None.
    """
    queue = deque([(initial_state, [])]) 
    visited = set()  # Tập hợp các trạng thái đã được duyệt
    nodes_expanded = 0
    while queue:
        nodes_expanded += 1
        state, actions = queue.popleft()  # Lấy trạng thái và đường đi từ đầu hàng đợi
        if state == goal_state:
            return actions,len(actions) ,nodes_expanded

        for action in get_actions(state):
            new_state = apply_action(state, action)

            # Nếu trạng thái mới chưa được duyệt, thêm vào tập visited và hàng đợi
            if tuple(map(tuple, new_state)) not in visited:
                visited.add(tuple(map(tuple, new_state)))
                queue.append((new_state, actions + [action]))

    return None,0,nodes_expanded