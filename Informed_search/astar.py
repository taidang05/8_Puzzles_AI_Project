import heapq
from helper import apply_action, get_actions, manhattan_distance

def a_star(initial_state, goal_state):

    queue = [(manhattan_distance(initial_state, goal_state), initial_state, [], 0)] # hàng đợi ưu tiên
    visited = {}
    nodes_expanded = 0
    while queue:
        nodes_expanded += 1
        _, state, actions, g = heapq.heappop(queue)
        if state == goal_state:
            return actions,len(actions),nodes_expanded

        state_tuple = tuple(map(tuple, state))
        if state_tuple in visited and visited[state_tuple] <= g:
            continue
        visited[state_tuple] = g

        for action in get_actions(state):
            new_state = apply_action(state, action)
            new_state_tuple = tuple(map(tuple, new_state))

            new_actions = actions + [action]
            new_g = g + 1
            new_total_cost = new_g + manhattan_distance(new_state, goal_state)
            if new_state_tuple not in visited or visited[new_state_tuple] > new_g:
                heapq.heappush(queue, (new_total_cost, new_state, new_actions, new_g))
    return None,0,nodes_expanded
