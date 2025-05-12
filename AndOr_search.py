from helper import apply_action, get_actions

def or_search(state, goal_state, visited,depth,nodes_expanded):
    if depth == 0:
        return None  # Stop recursion if depth limit is reached
    nodes_expanded += 1
    # Check if the current state is the goal state
    if state == goal_state:
        return [],nodes_expanded      # Goal reached, return an empty path

    # Convert state to tuple for hashing
    state_tuple = tuple(tuple(row) for row in state)
    if state_tuple in visited:
        return None  # Avoid cycles
    visited.add(state_tuple)

    # Explore all possible actions
    for action in get_actions(state):
        new_state = apply_action(state, action)
        subplan = or_search(new_state, goal_state, visited,depth-1)
        if subplan is not None:
            return [action] + subplan  # Append the action to the path

    return None  # No valid action found

def and_or_search(state, goal_state):
    visited = set()
    depth_limit = 100  # Increase depth limit if needed
    return or_search(state, goal_state, visited,depth_limit,0)