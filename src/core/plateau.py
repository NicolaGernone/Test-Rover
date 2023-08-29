from dataclasses import dataclass


@dataclass
class Plateau:
    """
    Represents the rectangular plateau on Mars.
    """

    width: int
    height: int

    def is_within_bounds(self, x: int, y: int) -> bool:
        """
        Checks if a point is within the bounds of the plateau.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
            width (int): The width of the plateau.
            height (int): The height of the plateau.

        Returns:
            bool: True if the point is within the bounds, False otherwise.
        """
        if (x <= self.width and y <= self.height) and (x >= 0 and y >= 0):
            return True
        raise ValueError("The rover has moved out of the plateau's bounds.")
