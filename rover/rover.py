from marsrover.rover.directions import Directions


class Rover(Directions):

    def __init__(self,plateau,position,facing):

        self.plateau = plateau
        self.position = position
        self.facing = facing


    def turn_left(self):
        self.facing = Directions.turn_left_side[self.facing]


    def turn_right(self):
        self.facing = Directions.turn_right_side[self.facing]


    def increase_y(self):
        if self.position.y + 1 > self.plateau.height:
            raise IndexError("You are trying to go out of the plateau")
        else:
            self.position.y += 1

    def increase_x(self):
        if self.position.x + 1 > self.plateau.width:
            raise IndexError("You are trying to go out of the plateau")
        else:
            self.position.x += 1

    def decrease_y(self):
        if self.position.y - 1 < self.plateau.min_height:
            raise IndexError("You are trying to go out of the plateau")
        else:
            self.position.y -= 1

    def decrease_x(self):
        if self.position.x - 1 < self.plateau.min_width:
            raise IndexError("You are trying to go out of the plateau")
        else:
            self.position.x -= 1


    def move(self):
        if self.facing == 'N':
            self.increase_y()

        elif self.facing == 'E':
            self.increase_x()

        elif self.facing == 'S':
            self.decrease_y()

        elif self.facing == 'W':
            self.decrease_x()

    def input_commands(self,command):
        if command == 'L':
            self.turn_left()
        elif 'R' == command:
            self.turn_right()
        elif 'M' == command:
            self.move()
        else:
            print('The command is not valid')

    def run_commands(self,commands):
        for i in commands:
            self.input_commands(i)














