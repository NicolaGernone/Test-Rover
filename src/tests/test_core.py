import pytest

from src.core.mission_control import MissionControl
from src.core.plateau import Plateau
from src.core.rover import Rover


def test_move_command():
    plateau = Plateau(5, 5)
    rover = Rover(1, 2, "N", plateau)
    rover.process_commands("M")
    assert rover.x == 1
    assert rover.y == 3
    assert rover.orientation == "N"


def test_turn_command():
    plateau = Plateau(5, 5)
    rover = Rover(1, 2, "N", plateau)
    rover.process_commands("R")
    assert rover.x == 1
    assert rover.y == 2
    assert rover.orientation == "E"


def test_mission_control():
    plateau = Plateau(5, 5)
    rover1 = Rover(1, 2, "N", plateau)
    rover2 = Rover(3, 3, "E", plateau)
    mission_control = MissionControl([(rover1, "LMLMLMLMM"), (rover2, "MMRMMRMRRM")])
    output = mission_control.run()
    assert output == [(1, 3, "N"), (5, 1, "E")]
