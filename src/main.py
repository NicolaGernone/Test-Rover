import sys
from core.mission_control import MissionControl
from processes.process_input import process_input
from processes.process_output import process_output
from utils.logger import get_logger

logger = get_logger()


def main():
    """
    The main function of the script.
    """
    try:
        print("Please select the input method:")
        print("1. From a text file")
        print("2. From the terminal")
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            filename = input("Please enter the path to the text file: ")
            with open(filename, "r") as f:
                input_str = f.read()
        elif choice == "2":
            print("Please enter the commands (Press Ctrl+D when you're done):")
            input_str = sys.stdin.read()
        else:
            print("Invalid choice. Exiting...")
            logger.info("Invalid choice. Exiting...")
            return

        logger.info("Start to process the string")
        rovers_and_commands = process_input(input_str)
        mission_control = MissionControl(rovers_and_commands)
        output = mission_control.run()
        logger.info("End to the processing and output sequence")
        print(process_output(output))
    except FileNotFoundError:
        print(f"File {filename} not found.")
        logger.exception(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        logger.exception(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
