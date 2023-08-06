import pytest

from src.main import main


def test_main_file_input_valid(mocker):
    # Mock user input for choice and a valid filename
    mocker.patch("builtins.input", side_effect=["1", "code_samples.txt"])

    # Mock file content
    mock_file_content = "5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"
    mocker.patch("builtins.open", mocker.mock_open(read_data=mock_file_content))

    # Capture print statements
    captured_output = mocker.patch("builtins.print")

    main()

    # Assert the expected output from the main function
    captured_output.assert_called_with("1 3 N\n5 1 E")


def test_main_terminal_input_valid(mocker):
    # Mock user input for choice and commands
    mocker.patch("builtins.input", side_effect=["2"])
    mocker.patch(
        "sys.stdin.read", return_value="5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"
    )

    # Capture print statements
    captured_output = mocker.patch("builtins.print")

    main()

    # Assert the expected output from the main function
    captured_output.assert_called_with("1 3 N\n5 1 E")


def test_main_invalid_choice(mocker):
    # Mock user input for an invalid choice
    mocker.patch("builtins.input", return_value="3")

    # Capture print statements
    captured_output = mocker.patch("builtins.print")

    main()

    # Check if the right error message is printed
    captured_output.assert_called_with("Invalid choice. Exiting...")


def test_main_file_not_found(mocker):
    # Mock user input for choice and an invalid filename
    mocker.patch("builtins.input", side_effect=["1", "nonexistent.txt"])

    # Simulate FileNotFoundError
    mocker.patch("builtins.open", side_effect=FileNotFoundError)

    # Capture print statements
    captured_output = mocker.patch("builtins.print")

    main()

    # Check if the right error message is printed
    error_msg = "FileNotFoundError\n"
    captured_output.assert_called()
    assert captured_output.call_args[0][0] == error_msg


def test_main_general_exception(mocker):
    # Mock user input for choice and commands, but simulate an exception during reading
    mocker.patch("builtins.input", side_effect=["2"])
    mocker.patch("sys.stdin.read", side_effect=Exception("Some unexpected error"))

    # Capture print statements
    captured_output = mocker.patch("builtins.print")

    main()

    # Check if the right error message is printed
    error_msg = f"Exception: Some unexpected error\n"
    captured_output.assert_called()
    assert captured_output.call_args[0][0] == error_msg
