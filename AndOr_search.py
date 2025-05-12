import time
import heapq
from collections import deque
from helper import apply_action, get_actions, manhattan_distance, state_to_tuple

def and_or_search(initial_state, goal_state, max_iterations=100000):
    counter = 0
    path = []    # Đường đi
    visited = set()  # Tập hợp trạng thái đã thăm
    # Hàng đợi ưu tiên: (heuristic, state, actions, depth)
    queue = [(manhattan_distance(initial_state, goal_state), initial_state, [])]
    parent = {}  # Lưu mối quan hệ cha-con

    while queue:
        counter += 1
        if counter > max_iterations:
            break

        h, state, actions = heapq.heappop(queue)

        state_tuple = state_to_tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        # Kiểm tra đích
        if manhattan_distance(state, goal_state) == 0:
            path = actions
            return path, len(path), counter

        # AND Node: Tạo tất cả trạng thái con
        children = []
        for action in get_actions(state):
            new_state = apply_action(state, action)
            new_state_tuple = state_to_tuple(new_state)
            if new_state_tuple in visited:
                continue
            new_h = manhattan_distance(new_state, goal_state)
            children.append((new_h, new_state, actions + [action]))

        # OR Node: Chọn tối đa 3 nhánh tốt nhất
        children.sort(key=lambda x: x[0])  # Sắp xếp theo heuristic
        for i in range(min(3, len(children))):
            new_h, new_state, new_actions = children[i]
            new_state_tuple = state_to_tuple(new_state)
            parent[new_state_tuple] = state_tuple
            heapq.heappush(queue, (new_h, new_state, new_actions))

    # Không tìm thấy
    path = []
    return path, 0, counter