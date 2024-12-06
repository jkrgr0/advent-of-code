#!/usr/bin/env python3
"""Day 5. Guard Gallivant."""

from aocd import get_data

puzzle_input = get_data(day=6, year=2024)


class ObstacleError(Exception):
    """Custom exception raised when an obstacle is encountered."""


def step(
    matrix: list[list[str]],
    pos_marker: str,
    obstacle_marker: str,
    direction: str,
    position: tuple[int, int],
) -> tuple[list[list[str]], tuple[int, int]]:
    """Move a position marker within a 2D matrix in the specified direction.

    Args:
        matrix (list[list[str]]): A 2D list representing the matrix.
        pos_marker (str): The character marking the current position.
        obstacle_marker (str): The character representing obstacles.
        direction (str): The direction to move the marker.
            Options are "up", "right", "down", or "left".
        position (tuple[int, int]): A tuple representing the current position
            (row, colum) of the marker.

    Raises:
        ValueError: If the provided direction is invalid.
        IndexError: If the move goes out of the matrix boundaries.
        ObstacleError: If the move encounters an obstacle.

    Returns:
        tuple[list[list[str]], tuple[int, int]]:
            - The updated 2D matrix after the move.
            - A tuple with the new position (row, column) of the marker.

    """
    x, y = position
    match direction:
        case "up":
            t_x = x - 1
            t_y = y
        case "right":
            t_x = x
            t_y = y + 1
        case "down":
            t_x = x + 1
            t_y = y
        case "left":
            t_x = x
            t_y = y - 1
        case _:
            msg = "Invalid direction."
            raise ValueError(msg)

    if t_y == -1 or t_x == -1:
        raise IndexError

    if matrix[t_x][t_y] == obstacle_marker:
        raise ObstacleError
    matrix[t_x][t_y] = pos_marker
    matrix[x][y] = "X"
    return matrix, t_x, t_y


def find_position(matrix: list[list[str]], marker: str) -> tuple[int, int]:
    """Find the position of a given value in a 2D matrix.

    Args:
        matrix (list[list[str]]): A 2D list representing the matrix.
        marker (str): The marker to search for in the 2D matrix.

    Returns:
        tuple[int, int]: A tuple representing the row and column indices of
            the found position of the marker.

    """
    for r, matrix_i in enumerate(matrix):
        for c, value in enumerate(matrix_i):
            if value == marker:
                return r, c
    return None


def navigate_matrix(
    puzzle_input: str,
    pos_marker: str = "^",
    obstacle_marker: str = "#",
    directions: list[str] | None = None,
) -> list[tuple[int, int]]:
    """Navigate a matrix based on directional movement rules, avoiding obstacles and boundaries.

    Args:
        puzzle_input (str): A multiline string representing the matrix.
        pos_marker (str, optional): The character marking the starting position.
            Defaults to "^".
        obstacle_marker (str, optional): The character representing obstacles.
            Defaults to "#".
        directions (list[str] | None, optional): The order of directions to attempt
            when moving. Default is ["up", "right", "down", "left"].

    Raises:
        ValueError: If the position marker was not found in the 2D matrix.

    Returns:
        list[tuple[int, int]]: A list of unique positions visited during navigation.

    """  # noqa: E501
    if directions is None:
        directions = ["up", "right", "down", "left"]

    matrix: list[list[str]] = [list(line) for line in puzzle_input.splitlines()]
    direction = directions[0]
    current_pos = find_position(matrix, pos_marker)
    if not current_pos:
        msg = f"Start marker '{pos_marker}' not found in the matrix."
        raise ValueError(msg)

    pos_history: list[tuple[int, int]] = [current_pos]

    while True:
        try:
            matrix, *current_pos = step(
                matrix,
                pos_marker,
                obstacle_marker,
                direction,
                current_pos,
            )

            if current_pos not in pos_history:
                pos_history.append(current_pos)
        except ObstacleError:
            directions.append(directions.pop(0))
            direction = directions[0]
        except IndexError:
            break

    return pos_history


visited_positions = navigate_matrix(puzzle_input)

print(
    "The guard visited the following amount of distinct positions: ",
    len(visited_positions),
)
