import unittest
from marsrover.rover.plateau import Plateau
from marsrover.rover.position import Position
from marsrover.rover.rover import Rover


class TestPlateau(unittest.TestCase):
    def test_constructor(self):
        plateau = Plateau(5, 9)

        self.assertEqual(plateau.width, 5)
        self.assertEqual(plateau.height, 9)


class TestPosition(unittest.TestCase):
    def test_constructor(self):
        position = Position(4, 6)
        self.assertEqual(position.x, 4)
        self.assertEqual(position.y, 6)


class TestRover(unittest.TestCase):
    def test_constructor(self):
        plateau = Plateau(4,8)
        position = Position(2, 4)
        compass = "N"
        rover = Rover(plateau, position, compass)
        self.assertEqual(plateau.width,4)
        self.assertEqual(plateau.height,8)
        self.assertEqual(position.x,2)
        self.assertEqual(position.y,4)

    def test_turn_left_method(self):
        plateau = Plateau(4, 8)
        position = Position(2, 4)
        rover = Rover(plateau, position, "N")
        rover.turn_left()
        self.assertEqual(rover.facing,"W")

    def test_turn_right_method(self):
        plateau = Plateau(4, 8)
        position = Position(2, 4)
        rover = Rover(plateau, position, "N")
        rover.turn_right()
        self.assertEqual(rover.facing, "E")

    def test_moving_forward_method_when_facing_north(self):
        plateau = Plateau(5, 5)
        position = Position(2, 2)
        rover = Rover(plateau, position, "N")
        rover.move()
        self.assertEqual(position.y,3)

    def test_moving_forward_method_when_facing_east(self):
        plateau = Plateau(5, 5)
        position = Position(2, 2)
        rover = Rover(plateau, position, "E")
        rover.move()
        self.assertEqual(position.x,3)

    def test_moving_forward_method_when_facing_south(self):
        plateau = Plateau(5, 5)
        position = Position(2, 2)
        rover = Rover(plateau, position, "S")
        rover.move()
        self.assertEqual(position.y,1)

    def test_moving_forward_method_when_facing_west(self):
        plateau = Plateau(5, 5)
        position = Position(2, 2)
        rover = Rover(plateau, position, "W")
        rover.move()
        self.assertEqual(position.x, 1)

    def test_goint_out_of_plateau_raises_exception(self):
        plateau = Plateau(5, 5)
        position = Position(5, 5)
        rover = Rover(plateau, position, "N")
        with self.assertRaises(IndexError):
            rover.move()


if __name__ == '__main__':
    unittest.main()