min_x = 0
min_y = 0


def init_game():
    global min_x, min_y
    min_x = 0
    min_y = 0


def get_position_middle(max, current):
    return int(abs((max - current) / 2))


def get_position_middle_reversed(min, current):
    result = get_position_middle(min, current)
    if result == 0:
        result = 1
    return result


def try_guest_hacker_v1(direction_hacker, matrix_width, matrix_height, player_x, player_y):
    position_move_y = 0
    if "U" in direction_hacker:
        position_move_y = min(0, player_y - 1)

    if "D" in direction_hacker:
        position_move_y = max(matrix_height - 1, player_y + 1)

    position_move_x = 0
    if "L" in direction_hacker:
        position_move_x = min(0, player_x - 1)

    if "R" in direction_hacker:
        position_move_x = max(matrix_width - 1, player_x + 1)

    return [position_move_x, position_move_y]


def try_guest_hacker(direction_hacker, matrix_width, matrix_height, player_x, player_y):
    '''
    [[0 0 0 0 2 1 0 0]
    [0 0 0 0 0 0 0 0]]
    '''
    global min_x, min_y

    max_x = matrix_width
    max_y = matrix_height

    player_new_x = player_x
    player_new_y = player_y

    position_move_x = 0
    position_move_y = 0

    if "U" in direction_hacker:
        max_y = player_new_y
        position_move_y = 0 - get_position_middle_reversed(min_y, player_new_y)

    if "D" in direction_hacker:
        min_y = player_new_y
        position_move_y = get_position_middle(max_y, player_new_y)

    if "L" in direction_hacker:
        max_x = player_new_x
        position_move_x = 0 - get_position_middle_reversed(min_x, player_new_x)

    if "R" in direction_hacker:
        min_x = player_new_x
        position_move_x = get_position_middle(max_x, player_new_x)

    player_new_x = player_new_x + position_move_x
    player_new_y = player_new_y + position_move_y

    return [player_new_x, player_new_y]
