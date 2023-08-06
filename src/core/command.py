from src.config.choices import DIRECTIONS, TURNS


class Command:
    """
    Represents a command that can be executed by a rover.
    """

    def execute(self, rover):
        """
        Executes the command on the given rover.

        Args:
            rover (Rover): The rover on which to execute the command.
        """
        raise NotImplementedError


class MoveCommand(Command):
    """
    Represents a move command that can be executed by a rover.
    """

    def execute(self, rover):
        """
        Executes the move command on the given rover.

        Args:
            rover (Rover): The rover on which to execute the command.
        """
        dx, dy = DIRECTIONS[rover.orientation]
        new_x, new_y = rover.x + dx, rover.y + dy
        if rover.plateau.is_within_bounds(x=new_x, y=new_y):
            rover.x, rover.y = new_x, new_y


class TurnCommand(Command):
    """
    Represents a turn command that can be executed by a rover.
    """

    def __init__(self, direction):
        """
        Initializes the turn command with the direction.

        Args:
            direction (str): The direction to turn ('L' for left, 'R' for right).
        """
        self.direction = direction

    def execute(self, rover):
        """
        Executes the turn command on the given rover.

        Args:
            rover (Rover): The rover on which to execute the command.
        """
        rover.orientation = TURNS[self.direction][rover.orientation]
