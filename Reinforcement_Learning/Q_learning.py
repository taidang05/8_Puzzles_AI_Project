import random
import time
import pickle
import numpy as np
from collections import defaultdict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper import is_solvable

# Định nghĩa trạng thái đích
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def q_learning(start_state, episodes=10000, alpha=0.1, gamma=0.9, epsilon_start=1.0, epsilon_end=0.01, epsilon_decay=0.995, q_table_file="q_table.pkl"):
    """Q-learning algorithm for 8-puzzle with Q-table persistence."""
    start_time = time.time()
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    # Load existing Q-table if available
    try:
        with open(q_table_file, "rb") as f:
            q_table = pickle.load(f)
            q_table = defaultdict(lambda: np.zeros(4), q_table)  # Convert back to defaultdict
    except FileNotFoundError:
        q_table = defaultdict(lambda: np.zeros(4))  # Initialize new Q-table

    max_space = len(q_table)

    def state_to_tuple(state):
        return tuple(state)

    def get_action(state, epsilon):
        if random.random() < epsilon:
            valid_actions = []
            zero_idx = state.index(0)
            row, col = zero_idx // 3, zero_idx % 3
            for i, (dr, dc) in enumerate(actions):
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 3 and 0 <= new_col < 3:
                    valid_actions.append(i)
            return random.choice(valid_actions) if valid_actions else random.randint(0, 3)
        else:
            valid_actions = []
            zero_idx = state.index(0)
            row, col = zero_idx // 3, zero_idx % 3
            q_values = q_table[state_to_tuple(state)]
            for i, (dr, dc) in enumerate(actions):
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 3 and 0 <= new_col < 3:
                    valid_actions.append((q_values[i], i))
            if not valid_actions:
                return random.randint(0, 3)
            return max(valid_actions)[1]

    def apply_action(state, action_idx):
        zero_idx = state.index(0)
        row, col = zero_idx // 3, zero_idx % 3
        dr, dc = actions[action_idx]
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            return tuple(new_state), -1  # Reward -1 for each move
        return state, -10  # Penalty for invalid move

    # Training phase
    epsilon = epsilon_start
    for episode in range(episodes):
        state = start_state if episode % 100 == 0 else tuple(random.sample(range(9), 9))  # Random state
        if not is_solvable(state):
            continue
        steps = 0
        while steps < 100:  # Max steps per episode
            action = get_action(state, epsilon)
            next_state, reward = apply_action(state, action)
            if next_state == GOAL_STATE:
                reward = 100  # Reward for reaching goal
            next_q_values = q_table[state_to_tuple(next_state)]
            q_table[state_to_tuple(state)][action] += alpha * (reward + gamma * np.max(next_q_values) - q_table[state_to_tuple(state)][action]
            )
            state = next_state
            steps += 1
            max_space = max(max_space, len(q_table))
            if state == GOAL_STATE:
                break
        epsilon = max(epsilon_end, epsilon * epsilon_decay)

    # Save Q-table to file
    with open(q_table_file, "wb") as f:
        pickle.dump(dict(q_table), f)

    # Inference phase: find path from start_state
    if not is_solvable(start_state):
        return None
    state = start_state
    path = [state]
    visited = {state}
    steps = 0
    while state != GOAL_STATE and steps < 100:
        action = get_action(state, 0)  # Greedy action (epsilon=0)
        next_state, _ = apply_action(state, action)
        if next_state in visited or next_state == state:
            return None  # Stuck or invalid move
        state = next_state
        path.append(state)
        visited.add(state)
        steps += 1
        max_space = max(max_space, len(q_table))

    if state != GOAL_STATE:
        return None

    return {
        "path": path,
        "steps": len(path) - 1,
        "cost": len(path) - 1,
        "time": time.time() - start_time,
        "space": max_space
    }