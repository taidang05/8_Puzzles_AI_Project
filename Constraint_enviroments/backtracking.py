import random
from helper import apply_action, get_actions, manhattan_distance

def backtracking(initial_state, goal_state, callback=None):
    """
    Tìm đường đi từ initial_state đến goal_state bằng thuật toán Backtracking.
    Bắt đầu từ trạng thái trống và điền số theo thứ tự các ô kề nhau, từ nhỏ đến lớn.
    Sử dụng heuristic để tăng tốc độ tìm kiếm.
    Trả về danh sách hành động dẫn đến đích, hoặc None nếu không tìm thấy.
    """
    # Khởi tạo trạng thái trống
    empty_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    nodes_expanded = 0
    
    def is_valid_state(state):
        """Kiểm tra xem trạng thái có hợp lệ không"""
        # Kiểm tra các số từ 0-8 chỉ xuất hiện một lần
        # numbers = set()
        # for row in state:
        #     for num in row:
        #         if num < 0 or num > 8 or num in numbers:
        #             return False
        #         numbers.add(num)
        return True
    
    def get_neighbors(i, j):
        """Lấy danh sách các ô kề với ô (i,j)"""
        neighbors = []
        # Kiểm tra 4 hướng: trên, dưới, trái, phải
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                neighbors.append((ni, nj))
        return neighbors
    
    def get_next_empty(state, last_i, last_j):
        """Lấy ô trống tiếp theo dựa trên heuristic"""
        # Nếu chưa điền ô nào, bắt đầu từ ô (0,0)
        if last_i is None or last_j is None:
            return (0, 0) if state[0][0] == 0 else None
        
        # Tìm ô có ít lựa chọn nhất
        min_choices = float('inf')
        best_pos = None
        
        # Ưu tiên các ô kề với ô vừa điền
        neighbors = get_neighbors(last_i, last_j)
        for ni, nj in neighbors:
            if state[ni][nj] == 0:
                # Đếm số lựa chọn có thể cho ô này
                choices = count_available_choices(state, ni, nj)
                if choices < min_choices:
                    min_choices = choices
                    best_pos = (ni, nj)
        
        if best_pos:
            return best_pos
            
        # Nếu không tìm thấy ô kề phù hợp, tìm ô trống có ít lựa chọn nhất
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    choices = count_available_choices(state, i, j)
                    if choices < min_choices:
                        min_choices = choices
                        best_pos = (i, j)
        
        return best_pos
    
    def count_available_choices(state, i, j):
        """Đếm số lựa chọn có thể cho ô (i,j) dựa trên các ràng buộc"""
        used = set()
        
        # Kiểm tra các số đã được sử dụng trong toàn bộ bảng
        for row in state:
            for num in row:
                if num != 0:
                    used.add(num)
        
        # Trả về số lượng các số có thể điền
        return 9 - len(used)
    
    def evaluate_state(state):
        """Đánh giá trạng thái hiện tại dựa trên khoảng cách đến goal state"""
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    # Tìm vị trí của số này trong goal state
                    for gi in range(3):
                        for gj in range(3):
                            if goal_state[gi][gj] == state[i][j]:
                                distance += abs(i - gi) + abs(j - gj)
        return distance
    
    def backtrack(state, used_numbers, last_i=None, last_j=None):
        nonlocal nodes_expanded
        nodes_expanded += 1
        
        # Gọi callback để cập nhật giao diện
        if callback:
            callback(state)
        
        # Nếu đã điền đủ 9 số
        if len(used_numbers) == 9:
            # Kiểm tra xem trạng thái có phải là goal state không
            if state == goal_state:
                return []
            return None
        
        # Lấy ô trống tiếp theo
        next_pos = get_next_empty(state, last_i, last_j)
        if next_pos is None:
            return None
            
        i, j = next_pos
        
        # Tạo danh sách các số chưa sử dụng và sắp xếp theo heuristic
        available_numbers = list(set(range(9)) - used_numbers)
        
        # Sắp xếp các số dựa trên heuristic
        def get_number_score(num):
            # Thử điền số và đánh giá
            state[i][j] = num
            score = evaluate_state(state)
            state[i][j] = 0
            return score
        
        available_numbers.sort(key=get_number_score)
        
        # Nếu đây là ô đầu tiên, ưu tiên điền số 1
        # if last_i is None and last_j is None and 1 in available_numbers:
        #     available_numbers.remove(1)
        #     available_numbers.insert(0, 1)
        
        for num in available_numbers:
            # Thử điền số
            state[i][j] = num
            used_numbers.add(num)
            
            # Kiểm tra tính hợp lệ của trạng thái
            if is_valid_state(state):
                # Thử điền tiếp
                result = backtrack(state, used_numbers, i, j)
                if result is not None:
                    return result
            
            # Nếu không thành công, quay lui
            state[i][j] = 0
            used_numbers.remove(num)
            # Gọi callback để cập nhật giao diện sau khi quay lui
            if callback:
                callback(state)
        
        return None
    
    # Bắt đầu backtracking từ trạng thái trống
    result = backtrack(empty_state, set())
    if result is None:
        return None, 0, nodes_expanded
    return result, len(result), nodes_expanded 