# Mars Rover Mission

NASA has deployed a squad of robotic rovers to a plateau on Mars. The goal is for these rovers to navigate the plateau and capture a complete view of the terrain to send back to Earth. This repository contains the software to control these rovers based on given instructions and report back their final positions.

## Introduction

The plateau on Mars is rectangular. A rover's position and location is represented by a combination of x and y coordinates and a letter indicating one of the four cardinal compass points. For navigation simplicity, the plateau is divided into a grid. An example of a rover's position could be `0, 0, N`, meaning the rover is at the bottom-left corner of the plateau facing North.

NASA controls a rover by sending a string of letters. The possible letters are:

- `L`: Spin 90 degrees to the left without moving.
- `R`: Spin 90 degrees to the right without moving.
- `M`: Move forward one grid point while maintaining the same heading.

## Usage

### Input Format

The input begins with a line indicating the upper-right coordinates of the plateau. The lower-left coordinates are assumed to be `0,0`. Following this, for each rover, there are two lines of input:

1. The rover's starting position and orientation, e.g., `1 2 N`.
2. A series of instructions telling the rover how to navigate the plateau, e.g., `L M L M L M L M M`.

Rovers execute their instructions sequentially, i.e., the second rover won't start until the first one finishes.

### Running the Script

To run the script, use the following command:

```bash
make run
```


You will be prompted to choose an input method:

1. From a text file
2. From the terminal

Based on your choice, you can provide the instructions either by entering the path to a text file (For a sample input, you can refer to the [code_samples.txt](./code_samples.txt) file.) or typing them directly into the terminal (finishing with ctrl+D).

### Output Format

The output for each rover will be its final coordinates and heading. For the given example, the expected output will be:

```bash
1 3 N
5 1 E
```

### Extra

If you want to run some tests or check some memory usage and timing in the [Makefile](./Makefile) you can find some commands to run this checks.
Follom this instructions:

- Run the setup:

```bash
make setup
```

- Run this command to check memory and timing:

```bash
make profile

make memory-profile

make line-profile
```

- To check tests and coverage:

```bash
make test

make coverage
```

## Observations

I prefer to avoid using Docker to keep the script execution simple and maintain a user-friendly experience. For virtual environment and dependency management, I can utilize Poetry. However, for running the script, I don't need any additional dependencies; it's only required for local testing of memory timing and tests.

To ensure a hassle-free experience for users and prevent potential installation issues with third-party tools, I have decided to refrain from using Docker.
