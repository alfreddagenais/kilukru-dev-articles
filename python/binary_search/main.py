from game_matrix import GameMatrix
from game_binary_search import try_guest_hacker, init_game


def main():
    gameMatrix = GameMatrix()
    gameMatrix.create_game()

    init_game()

    position_player_x = gameMatrix.position_player_x
    position_player_y = gameMatrix.position_player_y

    turn = 1
    while(True):
        print("Turn #" + str(turn))

        position_player_x_init = position_player_x
        position_player_y_init = position_player_y

        direction_hacker = gameMatrix.get_direction_hacker(
            position_player_x, position_player_y)
        position_player = try_guest_hacker(
            direction_hacker, gameMatrix.matrix_width, gameMatrix.matrix_height, position_player_x, position_player_y)

        position_player_x = position_player[0]
        position_player_y = position_player[1]
        direction_hacker = gameMatrix.get_direction_hacker(
            position_player_x, position_player_y)
        if (direction_hacker == ""):
            print("WON!!!!!!!!! in " + str(turn) + " turns")
            break

        # Stop loop after much too tentative of failure.
        if(turn >= 15):
            print("FAILED!!!!!!!!! in " + str(turn) + " turns")
            break

        gameMatrix.matrix[position_player_y_init][position_player_x_init] = 0
        gameMatrix.matrix[position_player_y][position_player_x] = 1
        print(gameMatrix.matrix)

        turn = turn + 1


if __name__ == "__main__":
    main()
