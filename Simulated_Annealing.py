import random
import math
from helper import apply_action, get_actions, manhattan_distance

def simulated_annealing(initial_state, goal_state, max_iterations=1000, initial_temp=20.0, cooling_rate=0.995):
    """
    Tìm đường đi từ initial_state đến goal_state bằng Simulated Annealing.
    Trả về danh sách hành động dẫn đến đích, hoặc [] nếu không tìm thấy.
    Sử dụng manhattan_distance làm heuristic.
    """
    current_state = initial_state
    current_h = manhattan_distance(current_state, goal_state)
    best_h = current_h
    best_path = []
    current_path = []
    temp = initial_temp

    for i in range(max_iterations):
        # Kiểm tra đích
        if current_h == 0:
            return current_path

        actions = get_actions(current_state)

        # Chọn ngẫu nhiên một hành động
        action = random.choice(actions)
        new_state = apply_action(current_state, action)
        new_h = manhattan_distance(new_state, goal_state)
        delta_h = new_h - current_h

        # Chấp nhận trạng thái mới dựa trên nhiệt độ
        if delta_h < 0 or random.random() < math.exp(-delta_h / temp):
            current_state = new_state
            current_h = new_h
            current_path.append(action)
            
            # Cập nhật trạng thái tốt nhất
            if current_h < best_h:
                best_h = current_h
                best_path = current_path.copy()

        # Giảm nhiệt độ
        temp *= cooling_rate
        if temp <= 1:  # Ngưỡng nhiệt độ tối thiểu
            break
    return best_path



