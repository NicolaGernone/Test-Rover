from dataclasses import dataclass

from src.core.command import MoveCommand, TurnCommand
from src.core.plateau import Plateau


@dataclass
class Rover:
    """
    Represents a rover on the plateau.
    """

    x: int
    y: int
    orientation: str
    plateau: Plateau

    COMMANDS = {
        Turn.LEFT.value: lambda: TurnCommand(Turn.LEFT),
        Turn.RIGHT.value: lambda: TurnCommand(Turn.RIGHT),
        "M": MoveCommand,
    }

    def process_commands(self, commands) -> None:
        """
        Processes a list of commands.

        Args:
            commands (str): A string of commands where each character is a command.
        """
        for command in commands:
            self.COMMANDS[command]().execute(self)

    def __str__(self):
        return f"{self.x} {self.y} {self.orientation}"
