import numpy as np

# Helper functions 

def get_actions(state):
    actions = []

    row, col = find_blank(state)

    if row > 0:
        actions.append("Up")
    if row < 2:
        actions.append("Down")
    if col > 0:
        actions.append("Left")
    if col < 2:
        actions.append("Right")

    return actions


def apply_action(state, action):
    new_state = [row[:] for row in state]

    row, col = find_blank(new_state)

    if action == "Up":
        new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
    elif action == "Down":
        new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
    elif action == "Left":
        new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
    elif action == "Right":
        new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]

    return new_state



def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
            
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_i, goal_j = find_tile(goal_state, state[i][j])
                distance += abs(i - goal_i) + abs(j - goal_j)
            else:
                goal_i, goal_j = 2, 2  # Vị trí đích của ô trống
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def find_tile(state, tile):
    """
    Returns the row and column indices of the given tile in the given state.
    """
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return i, j
            
