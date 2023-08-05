from core.plateau import Plateau
from core.rover import Rover
from utils.logger import get_logger

logger = get_logger()

def process_input(input_str):
    """
    Process the input string.

    Args:
        input_str (str): The input string.

    Returns:
        tuple: A tuple containing the plateau and a list of rovers and their commands.
    """
    try:
        lines = input_str.strip().split('\n')
        plateau_width, plateau_height = map(int, lines[0].split())
        plateau = Plateau(plateau_width, plateau_height)
        rovers_and_commands = []
        for i in range(1, len(lines), 2):
            x, y, orientation = lines[i].split()
            if orientation not in ['N', 'E', 'S', 'W']:
                raise ValueError(f"Invalid orientation {orientation}")
            x, y = int(x), int(y)
            rover = Rover(x, y, orientation, plateau)
            commands = lines[i + 1]
            if any(command not in ['L', 'R', 'M'] for command in commands):
                raise ValueError(f"Invalid commands {commands}")
            rovers_and_commands.append((rover, commands))
        return plateau, rovers_and_commands
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        logger.exception(f"Invalid input: {ve}")
        raise
