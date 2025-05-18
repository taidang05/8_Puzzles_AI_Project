import random
import heapq
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper import apply_action, get_actions, manhattan_distance, state_to_tuple
# Hàm cho Genetic Algorithm
def fitness(state, goal_state):
    """Hàm fitness: -khoảng cách Manhattan để tối đa hóa fitness"""
    return -manhattan_distance(state, goal_state)

def generate_random_valid_state():
    """Sinh trạng thái ngẫu nhiên hợp lệ cho 8-puzzle"""
    state = np.arange(9).reshape(3, 3).tolist()
    random.shuffle(state)
    while not is_solvable(state):
        random.shuffle(state)
    return state

def is_solvable(state):
    """Kiểm tra trạng thái có thể đạt trạng thái đích"""
    flat_state = [tile for row in state for tile in row]
    inversions = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if flat_state[i] != 0 and flat_state[j] != 0 and flat_state[i] > flat_state[j]:
                inversions += 1
    return inversions % 2 == 0

def tournament_selection(population, fitness_scores, k=3):
    """Chọn lọc dạng tournament: chọn cá thể tốt nhất trong k cá thể ngẫu nhiên"""
    tournament = random.sample(list(zip(population, fitness_scores)), k)
    return max(tournament, key=lambda x: x[1])[0]

def pmx_crossover(parent1, parent2):
    """Lai ghép PMX cho hai hoán vị trong 8-puzzle"""
    # Chuyển ma trận 3x3 thành mảng 1D để thực hiện PMX
    flat_parent1 = [tile for row in parent1 for tile in row]
    flat_parent2 = [tile for row in parent2 for tile in row]
    
    size = len(flat_parent1)
    child1, child2 = flat_parent1[:], flat_parent2[:]
    start, end = sorted(random.sample(range(size), 2))
    
    # Tạo ánh xạ cho các phần tử trong đoạn [start, end]
    mapping1_to_2 = {}
    mapping2_to_1 = {}
    for i in range(start, end + 1):
        child1[i] = flat_parent2[i]  # Sao chép đoạn từ parent2 sang child1
        child2[i] = flat_parent1[i]  # Sao chép đoạn từ parent1 sang child2
        mapping1_to_2[flat_parent1[i]] = flat_parent2[i]
        mapping2_to_1[flat_parent2[i]] = flat_parent1[i]
    
    # Điều chỉnh các phần tử ngoài đoạn
    for i in list(range(0, start)) + list(range(end + 1, size)):
        # Với child1
        value = flat_parent1[i]
        while value in mapping1_to_2 and value in [child1[j] for j in range(start, end + 1)]:
            value = mapping1_to_2[value]
        child1[i] = value
        # Với child2
        value = flat_parent2[i]
        while value in mapping2_to_1 and value in [child2[j] for j in range(start, end + 1)]:
            value = mapping2_to_1[value]
        child2[i] = value
    
    # Chuyển mảng 1D về ma trận 3x3
    child1 = [child1[i:i+3] for i in range(0, 9, 3)]
    child2 = [child2[i:i+3] for i in range(0, 9, 3)]
    
    return child1, child2

def mutate(state):
    """Đột biến: hoán đổi hai ô ngẫu nhiên (trừ ô trống)"""
    state = [row[:] for row in state]
    flat_state = [tile for row in state for tile in row]
    idx1, idx2 = random.sample([i for i in range(9) if flat_state[i] != 0], 2)
    flat_state[idx1], flat_state[idx2] = flat_state[idx2], flat_state[idx1]
    return [flat_state[i:i+3] for i in range(0, 9, 3)]

def convert_to_actions(final_state, initial_state):
    """Chuyển trạng thái thành chuỗi hành động bằng A*"""
    queue = [(manhattan_distance(initial_state, final_state), initial_state, [], 0)]
    visited = {state_to_tuple(initial_state): 0}
    
    while queue:
        _, state, actions, g = heapq.heappop(queue)
        if state == final_state:
            return actions
        
        state_tuple = state_to_tuple(state)
        if state_tuple in visited and visited[state_tuple] <= g:
            continue
        visited[state_tuple] = g
        
        for action in get_actions(state):
            new_state = apply_action(state, action)
            new_state_tuple = state_to_tuple(new_state)
            new_g = g + 1
            if new_state_tuple not in visited or visited[new_state_tuple] > new_g:
                new_total_cost = new_g + manhattan_distance(new_state, final_state)
                heapq.heappush(queue, (new_total_cost, new_state, actions + [action], new_g))
    
    return []  # Không tìm thấy đường đi

def genetic_algorithm(initial_state, goal_state, pop_size=30, max_generations=200, mutation_rate=0.3):
    """Thuật toán di truyền cho 8-puzzle"""
    # Khởi tạo quần thể
    population = [generate_random_valid_state() for _ in range(pop_size - 1)]
    population.append(initial_state)
    nodes_expanded = 0
    best_fitness_history = []
    no_improvement_count = 0
    best_fitness_ever = float('-inf')
    
    print(f"Initial state fitness: {fitness(initial_state, goal_state)}")
    print(f"Population size: {pop_size}, Max generations: {max_generations}, Mutation rate: {mutation_rate}")
    
    for generation in range(max_generations):
        # Đánh giá fitness
        fitness_scores = [fitness(state, goal_state) for state in population]
        nodes_expanded += len(population)
        best_fitness = max(fitness_scores)
        best_fitness_history.append(best_fitness)
        
        # Kiểm tra cải thiện
        if best_fitness > best_fitness_ever:
            best_fitness_ever = best_fitness
            no_improvement_count = 0
            print(f"\nNew best fitness found: {best_fitness}")
            best_state = population[fitness_scores.index(best_fitness)]
            print("Best state:")
            for row in best_state:
                print(row)
        else:
            no_improvement_count += 1
        
        # In thông tin tiến trình
        if generation % 5 == 0:
            print(f"\nGeneration {generation}")
            print(f"Best fitness: {best_fitness}")
            print(f"Average fitness: {sum(fitness_scores)/len(fitness_scores):.2f}")
            print(f"No improvement for {no_improvement_count} generations")
        
        # Kiểm tra đích
        if best_fitness == 0:
            best_idx = fitness_scores.index(0)
            actions = convert_to_actions(population[best_idx], initial_state)
            print(f"\nSolution found in generation {generation}!")
            return actions, len(actions), nodes_expanded
        
        # Nếu không cải thiện trong 20 thế hệ, tăng đa dạng
        if no_improvement_count >= 20:
            print("\nNo improvement for too long, increasing diversity...")
            # Giữ lại 5 cá thể tốt nhất
            best_individuals = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)[:5]
            population = [ind[0] for ind in best_individuals]
            # Thêm các cá thể ngẫu nhiên mới
            population.extend([generate_random_valid_state() for _ in range(pop_size - 5)])
            no_improvement_count = 0
            continue
        
        # Giữ lại các cá thể tốt nhất (elitism)
        best_individuals = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)[:5]
        new_population = [ind[0] for ind in best_individuals]
        
        # Tạo thế hệ mới
        while len(new_population) < pop_size:
            # Chọn cha mẹ dựa trên xác suất tỷ lệ với fitness
            total_fitness = sum(fitness_scores)
            if total_fitness == 0:
                parent1, parent2 = random.sample(population, 2)
            else:
                probs = [score/total_fitness for score in fitness_scores]
                parent1 = random.choices(population, weights=probs, k=1)[0]
                parent2 = random.choices(population, weights=probs, k=1)[0]
            
            child1, child2 = pmx_crossover(parent1, parent2)
            
            # Đột biến với tỷ lệ thay đổi theo thời gian
            current_mutation_rate = mutation_rate * (1 - generation/max_generations)
            if random.random() < current_mutation_rate:
                child1 = mutate(child1)
            if random.random() < current_mutation_rate:
                child2 = mutate(child2)
                
            new_population.extend([child1, child2])
        
        # Kiểm tra và tăng đa dạng quần thể nếu cần
        unique_states = set()
        for state in new_population:
            state_tuple = state_to_tuple(state)
            unique_states.add(state_tuple)
        
        if len(unique_states) < pop_size * 0.3:
            print("\nPopulation too similar, adding random individuals...")
            new_random_individuals = [generate_random_valid_state() for _ in range(pop_size // 3)]
            new_population = new_population[:-len(new_random_individuals)] + new_random_individuals
        
        population = new_population
    
    print("\nMax generations reached without finding solution")
    # Trả về trạng thái tốt nhất
    fitness_scores = [fitness(state, goal_state) for state in population]
    best_idx = fitness_scores.index(max(fitness_scores))
    actions = convert_to_actions(population[best_idx], initial_state)
    return actions, len(actions), nodes_expanded

# Hàm chạy chính
if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    print("Starting Genetic Algorithm...")
    print("Initial state:")
    for row in initial_state:
        print(row)
    print("\nGoal state:")
    for row in goal_state:
        print(row)
    path, path_len, nodes = genetic_algorithm(initial_state, goal_state)
    print(f"\nFinal results:")
    print(f"Path: {path}")
    print(f"Path length: {path_len}")
    print(f"Nodes expanded: {nodes}")