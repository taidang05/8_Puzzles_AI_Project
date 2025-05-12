import heapq
from helper import apply_action, get_actions, manhattan_distance

def greedy(initial_state, goal_state):
    """
    Finds a path from initial_state to goal_state using greedy best-first search with the Manhattan distance heuristic.
    Returns the path as a list of actions (e.g., ["Up", "Left", "Down"]).
    If no path is found, returns None.
    """
    queue = [(manhattan_distance(initial_state, goal_state), initial_state, [])]
    visited = set()
    tmp=0
    nodes_expanded = 0
    while queue:
        nodes_expanded += 1
        tmp, state, actions = heapq.heappop(queue)

        if state == goal_state:
            print(tmp)
            return actions,len(actions),nodes_expanded

        if tuple(map(tuple, state)) in visited:
            continue

        visited.add(tuple(map(tuple, state)))

        for action in get_actions(state):
            new_state = apply_action(state, action)

            if tuple(map(tuple, new_state)) not in visited:
                heapq.heappush(queue, (manhattan_distance(new_state, goal_state), new_state, actions + [action]))

    return None,0,nodes_expanded