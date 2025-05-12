from collections import deque
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper import apply_action, get_actions, state_to_tuple
import time



def dfs(initial_state, goal_state):
    """
    Depth-First Search (DFS) for solving the 8-Puzzle problem.
    """
    stack = deque([(initial_state, [], 0)]) 
    visited = set()
    mxdepth = 0
    nodes_expanded = 0
    while stack:
        nodes_expanded += 1
        state, actions, curentdepth = stack.pop() 
        mxdepth = max(mxdepth, curentdepth)
        if state == goal_state:
            print(f"Max depth reached: {mxdepth}")
            return actions,len(actions),nodes_expanded

        state_tuple = state_to_tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for action in get_actions(state):
            new_state = apply_action(state, action)
            new_state_tuple = state_to_tuple(new_state)

            if new_state_tuple not in visited:
                stack.append((new_state, actions + [action], curentdepth + 1))


    return None,0,nodes_expanded


