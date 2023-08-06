def process_output(output_list):
    """
    Process the output.

    Args:
        output (list): A list of tuples where each tuple contains the final position and orientation of a rover.

    Returns:
        str: The output string.
    """
    return '\n'.join([' '.join(map(str, t)) for t in output_list])
