import re

import numpy as np


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [re.split(',| -> ', i) for i in input_data]
    input_data = [np.array(list(map(int, i))) for i in input_data]
    input_data = np.array(input_data)
    return input_data


def count_horizontal_and_vertical_points(lines, points_grid):
    for line in lines:
        # Same x
        x1, x2, y1, y2 = line[0], line[2], line[1], line[3]
        if x1 == x2:
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            points_grid[min_y: max_y + 1, x1] += 1
        # Same y
        if y1 == y2:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            points_grid[y1, min_x: max_x + 1] += 1


def generate_diagonal_range(p1, p2):
    if p1 < p2:
        return [i for i in range(p1, p2 + 1)]
    else:
        return [i for i in range(p1, p2 - 1, -1)]


def part1(p1_lines, grid_size):
    p1_points = np.zeros((grid_size[0], grid_size[1]))

    count_horizontal_and_vertical_points(p1_lines, p1_points)

    return len(np.where(p1_points > 1)[1])


def part2(p2_lines, grid_size):
    p2_points = np.zeros((grid_size[0], grid_size[1]))

    count_horizontal_and_vertical_points(p2_lines, p2_points)

    for line in p2_lines:
        x1, x2, y1, y2 = line[0], line[2], line[1], line[3]
        if abs(x2 - x1) == abs(y2 - y1):
            x_range = generate_diagonal_range(x1, x2)
            y_range = generate_diagonal_range(y1, y2)

            for i in range(len(x_range)):
                p2_points[y_range[i], x_range[i]] += 1

    return len(np.where(p2_points > 1)[0])


def main():
    day = 5
    # noinspection DuplicatedCode
    lines = data_prep(day)
    grid_size = [max(lines[:, i]) for i in range(4)]
    grid_size = [max(grid_size[0], grid_size[2]) + 1, max(grid_size[1], grid_size[3]) + 1]

    answer1 = part1(lines, grid_size)
    answer2 = part2(lines, grid_size)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
