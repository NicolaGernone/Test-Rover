from dataclasses import dataclass
from config.choices import COMMANDS
from core.plateau import Plateau

@dataclass
class Rover:
    """
    Represents a rover on the plateau.
    """

    x: int
    y: int
    orientation: str
    plateau: Plateau

    def process_commands(self, commands):
        """
        Processes a list of commands.

        Args:
            commands (str): A string of commands where each character is a command.
        """
        for command in commands:
            COMMANDS[command](self).execute()

    def __str__(self):
        return f"{self.x} {self.y} {self.orientation}"
