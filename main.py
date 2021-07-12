from marsrover.rover.position import Position
from marsrover.rover.plateau import Plateau
from marsrover.rover.rover import Rover


def main():
    plateau = Plateau(5, 5)
    position = Position(1, 2)
    compass = 'N'
    rover = Rover(plateau, position, compass)
    rover.run_commands("LMLMLMLMM")
    print(rover.position.x, rover.position.y, rover.facing)
    #it prints 1 3 N

    plateau = Plateau(5,5)
    position = Position(3,3)
    compass = 'E'
    rover = Rover(plateau,position,compass)
    rover.run_commands("MMRMMRMRRM")
    print(rover.position.x,rover.position.y,rover.facing)
    #it prints 5 1 E

if __name__ == "__main__":
    main()
