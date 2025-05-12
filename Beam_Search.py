import heapq
from helper import apply_action, get_actions, manhattan_distance, state_to_tuple

def beam_search(initial_state, goal_state, beam_width=2):
    """
    Tìm đường đi từ initial_state đến goal_state bằng Beam Search.
    Trả về danh sách hành động dẫn đến đích, hoặc [] nếu không tìm thấy.
    Sử dụng manhattan_distance làm heuristic.
    """
    # Hàng đợi: (h(n), state, actions, depth)
    queue = [(manhattan_distance(initial_state, goal_state), initial_state, [])]
    visited = set([state_to_tuple(initial_state)])  # Tránh lặp vô hạn
    nodes_expanded = 0
    while queue:
        nodes_expanded += 1
        # Lấy top beam_width trạng thái
        candidates = []
        
        # Xử lý các trạng thái ở mức hiện tại
        for h, state, actions in queue:
            if state == goal_state:
                return actions,len(actions),nodes_expanded
                
                
            # Tạo trạng thái lân cận
            for action in get_actions(state):
                new_state = apply_action(state, action)
                new_state_tuple = state_to_tuple(new_state)
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    new_h = manhattan_distance(new_state, goal_state)
                    candidates.append((new_h, new_state, actions + [action]))

        # Sắp xếp và chọn top beam_width trạng thái cho mức tiếp theo
        queue = sorted(candidates, key=lambda x: x[0])[:beam_width]
        
        if not queue:
            break
            
    return [],0,nodes_expanded  # Không tìm thấy đường đi

