import pytest
from factories import PlateauFactory, RoverFactory

from src.processes.process_input import process_input


def test_process_input_valid():
    plateau = PlateauFactory()
    rover1 = RoverFactory(plateau=plateau)
    rover2 = RoverFactory(x=3, y=3, orientation="E", plateau=plateau)
    input_str = "5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"
    expected_output = [
        (rover1, ["L", "M", "L", "M", "L", "M", "L", "M", "M"]),
        (rover2, ["M", "M", "R", "M", "M", "R", "M", "R", "R", "M"]),
    ]

    result = process_input(input_str)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_process_input_invalid():
    input_str = "invalid input"
    with pytest.raises(ValueError):  # Assuming it raises ValueError for invalid inputs
        process_input(input_str)
