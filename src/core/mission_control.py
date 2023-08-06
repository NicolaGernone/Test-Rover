from src.core.plateau import Plateau


class MissionControl:
    """
    Represents the mission control that manages the rovers on the plateau.
    """

    def __init__(self, rovers_and_commands):
        """
        Initializes the mission control with the plateau and the rovers and their commands.

        Args:
            plateau (Plateau): The plateau on which the rovers are.
            rovers_and_commands (list): A list of tuples where each tuple contains a rover and its commands.
        """
        self.rovers_and_commands = rovers_and_commands
        self.final_positions = []

    def run(self):
        """
        Runs the mission.

        Returns:
            list: A list of tuples where each tuple contains the final position and orientation of a rover.
        """
        for rover, commands in self.rovers_and_commands:
            rover.process_commands(commands)
            if not rover.plateau.is_within_bounds(x=rover.x, y=rover.y):
                raise ValueError("The rover has moved out of the plateau's bounds.")
            self.final_positions.append((rover.x, rover.y, rover.orientation))
        return self.final_positions
