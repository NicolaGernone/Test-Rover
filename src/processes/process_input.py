from core.plateau import Plateau
from core.rover import Rover
from utils.logger import get_logger

logger = get_logger()

def normalize_input_string(input_str):
    """
    Convert input string letters to uppercase and ensure there are spaces between characters.

    Args:
        input_str (str): The original input string.

    Returns:
        str: The normalized input string.
    """
    input_str = input_str.upper()
    
    formatted_parts = []
    for part in input_str.strip().split('\n'):
        if len(part) > 1 and not part.isdigit():
            formatted_parts.append(tuple(part.strip().split()))
        else:
            formatted_parts.append(tuple(part.split()))
    return formatted_parts

def split_adjacent_chars(chars):
    """
    Split strings with more than one character into individual characters.

    Args:
        chars (list of str): List of characters and strings.

    Returns:
        list of str: List of individual characters.
    """
    result = []
    for char in chars:
        # Extend the result list with individual characters from each string
        result.extend(tuple(char))
    return result


def validate_orientation(orientation):
    """
    Validate rover orientation.

    Args:
        orientation (str): The rover orientation.

    Raises:
        ValueError: If orientation is invalid.
    """
    if orientation not in ['N', 'E', 'S', 'W']:
        raise ValueError(f"Invalid orientation {orientation}")


def validate_commands(commands):
    """
    Validate rover commands.

    Args:
        commands (list of str): The rover commands.

    Raises:
        ValueError: If any command is invalid.
    """
    if any(command not in ['L', 'R', 'M'] for command in commands):
        raise ValueError(f"Invalid commands {commands}")


def process_input(input_str):
    """
    Process the input string.

    Args:
        input_str (str): The input string.

    Returns:
        tuple: A tuple containing the plateau and a list of rovers and their commands.
    """
    try:
        lines = normalize_input_string(input_str)
        plateau_width, plateau_height = map(int, lines[0])
        plateau = Plateau(plateau_width, plateau_height)
        rovers_and_commands = []
        
        for i in range(1, len(lines), 2):
            x, y, orientation = split_adjacent_chars(lines[i])
            validate_orientation(orientation)
            x, y = int(x), int(y)
            rover = Rover(x, y, orientation, plateau)
            commands = split_adjacent_chars(lines[i + 1])
            validate_commands(commands)
            rovers_and_commands.append((rover, commands))
        
        return rovers_and_commands
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        logger.exception(f"Invalid input: {ve}")
        raise

