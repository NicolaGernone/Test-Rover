import pytest
from src.processes.process_output import process_output


def test_process_output_valid():
    input_list = [(1, 2, "N"), (3, 3, "E")]
    expected_output = "1 2 N\n3 3 E"
    assert process_output(input_list) == expected_output


def test_process_output_empty():
    input_list = []
    expected_output = ""
    assert process_output(input_list) == expected_output


def test_process_output_various():
    input_list = [(4, 4, "S"), (0, 0, "W"), (2, 3, "E")]
    expected_output = "4 4 S\n0 0 W\n2 3 E"
    assert process_output(input_list) == expected_output
