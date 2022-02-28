import numpy
from game_binary_search import try_guest_hacker, init_game


class GameMatrix:
    def create_game(self):
        self.create_matrix()
        self.position_init_player()
        self.position_init_hacker()

    def create_matrix(self, matrix_width: int = 0, matrix_height: int = 0):
        '''
        1: player
        2: hacker
        direction: DR

        [1][O][O][O]
        [O][O][O][O]
        [O][O][2][O]
        [O][O][O][O]
        '''
        if(matrix_width <= 0):
            self.matrix_width = numpy.random.randint(2, 40)
        else:
            self.matrix_width = matrix_width

        if(matrix_height <= 0):
            self.matrix_height = numpy.random.randint(2, 40)
        else:
            self.matrix_height = matrix_height

        print("Matrix Size:     [" + str(self.matrix_width) +
              "," + str(self.matrix_height) + "]")

        self.matrix = numpy.random.randint(
            1, size=(self.matrix_height, self.matrix_width))

        print(self.matrix)
        print("\n")

    def position_init_player(self, position_player_x: int = 0, position_player_y: int = 0):
        if(self.matrix_width <= 1):
            self.position_player_x = 0
        elif(position_player_x <= 0):
            self.position_player_x = numpy.random.randint(
                0, self.matrix_width - 1)
        else:
            self.position_player_x = position_player_x

        if(self.matrix_height <= 1):
            self.position_player_y = 0
        elif(position_player_y <= 0):
            self.position_player_y = numpy.random.randint(
                0, self.matrix_height - 1)
        else:
            self.position_player_y = position_player_y

        self.matrix[self.position_player_y][self.position_player_x] = 1
        print("Position Player:  [" + str(self.position_player_x) +
              "," + str(self.position_player_y) + "]")

    def position_init_hacker(self, position_hacker_x: int = 0, position_hacker_y: int = 0):
        if(self.matrix_width <= 1):
            self.position_hacker_x = 0
        elif(position_hacker_x <= 0):
            self.position_hacker_x = numpy.random.randint(
                0, self.matrix_width - 1)
        else:
            self.position_hacker_x = position_hacker_x

        if(self.matrix_height <= 1):
            self.position_hacker_y = 0
        elif(position_hacker_y <= 0):
            self.position_hacker_y = numpy.random.randint(
                0, self.matrix_height - 1)
        else:
            self.position_hacker_y = position_hacker_y

        self.matrix[self.position_hacker_y][self.position_hacker_x] = 1
        print("Position Hacker:  [" + str(self.position_hacker_x) +
              "," + str(self.position_hacker_y) + "]")

    def get_direction_hacker(self, position_player_x: int, position_player_y: int):
        if (self.position_hacker_x == position_player_x and self.position_hacker_y == position_player_y):
            print("Hacker Founded")
            return ""

        self.direction_hacker_x = ""
        if (self.position_hacker_x > position_player_x):
            self.direction_hacker_x = "R"
        if (self.position_hacker_x < position_player_x):
            self.direction_hacker_x = "L"

        self.direction_hacker_y = ""
        if (self.position_hacker_y > position_player_y):
            self.direction_hacker_y = "D"
        if (self.position_hacker_y < position_player_y):
            self.direction_hacker_y = "U"

        self.direction_hacker = self.direction_hacker_y + self.direction_hacker_x
        print("Direction Hacker: [" + self.direction_hacker + "]")

        return self.direction_hacker

    def play_game(self):
        init_game()

        position_player_x = self.position_player_x
        position_player_y = self.position_player_y

        turn = 1
        while(True):
            print("Turn #" + str(turn))

            position_player_x_init = position_player_x
            position_player_y_init = position_player_y

            direction_hacker = self.get_direction_hacker(
                position_player_x, position_player_y)
            position_player = try_guest_hacker(
                direction_hacker, self.matrix_width, self.matrix_height, position_player_x, position_player_y)

            position_player_x = position_player[0]
            position_player_y = position_player[1]
            direction_hacker = self.get_direction_hacker(
                position_player_x, position_player_y)
            if (direction_hacker == ""):
                print("WON!!!!!!!!! in " + str(turn) + " turns")
                return [turn, True]

            # Stop loop after much too tentative of failure.
            if(turn >= 25):
                print("FAILED!!!!!!!!! in " + str(turn) + " turns")
                return [turn, False]

            self.matrix[position_player_y_init][position_player_x_init] = 0
            self.matrix[position_player_y][position_player_x] = 1
            print(self.matrix)

            turn = turn + 1
