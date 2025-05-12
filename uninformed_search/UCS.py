import heapq
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper import apply_action, get_actions

def ucs(initial_state, goal_state):
    priority_queue = []
    heapq.heappush(priority_queue, (0, initial_state, []))  # (cost, state, path)
    visited = set()
    nodes_expanded = 0
    while priority_queue:
        cost, state, path = heapq.heappop(priority_queue)
        nodes_expanded += 1
        if state == goal_state:
            return path,len(path),nodes_expanded    

        # Convert state to tuple for hashing
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        # Generate all possible actions and their resulting states
        for action in get_actions(state):
            new_state = apply_action(state, action)
            new_state_tuple = tuple(tuple(row) for row in new_state)

            if new_state_tuple not in visited:
                # Add the new state to the priority queue with updated cost
                heapq.heappush(priority_queue, (cost + 1, new_state, path + [action]))
    return None,0,nodes_expanded
