# from helper import apply_action, get_actions

# def belief_state_search(start_state, goal_state):

#     queue = [(start_state)]  # (state, actions, cost)
#     visited = set()

#     while queue:
#         current_list_state = queue.pop(0)  # Use pop(0) for BFS
#         flag = True
#         for state in current_list_state:
#             if state not in goal_state:
#                 flag = False
#                 break

#         if flag:
#             return True
        
#         for state in current_list_state:
#                 new_state = apply_action(state, action)
#                 if new_state not in visited:                    visited.add(new_state)
#                     queue.append(new_state)
#     return False
#             for action in get_actions(state):
#                 new_state = apply_action(state, action)
#                 if new_state not in visited:
#                     visited.add(new_state)
#                     queue.append(new_state)
#     return False


