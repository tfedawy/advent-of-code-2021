import re
import numpy as np
from collections import defaultdict


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [re.split('[=.,]', i) for i in input_data]
    instructions = [i[0].split(' ')[0] for i in input_data]
    projections = [[int(j[i]) for i in [1, 3, 5, 7, 9, 11]] for j in input_data]
    cuboids = [tuple(tuple(c[i:i + 2]) for i in range(0, 6, 2)) for c in projections]
    return instructions, projections, cuboids


def projections_overlap(p1: tuple, p2: tuple) -> bool:
    p1, p2 = sorted((p1, p2))
    return True if p1[1] >= p2[0] else False


def projections_intersection(p1: tuple, p2: tuple) -> tuple:
    return max(p1[0], p2[0]), min(p1[1], p2[1])


def cubes_overlap(c1: tuple, c2: tuple) -> bool:
    return all(map(projections_overlap, c1, c2))


def cubes_intersection(c1: tuple, c2: tuple) -> tuple:
    if cubes_overlap(c1, c2):
        return tuple(map(projections_intersection, c1, c2))


def cube_volume(cuboid):
    volume = 1
    for axis in cuboid:
        volume *= axis[1] - axis[0] + 1
    return volume


def part1(instructions, coordinates):
    coordinates = np.array(coordinates)
    coordinates += 50
    region_size = 102
    cubes = np.zeros((region_size, region_size, region_size))
    for i, coordinate in enumerate(coordinates):
        x1, x2 = max(coordinate[0], 0), min(coordinate[1] + 1, 101)
        y1, y2 = max(coordinate[2], 0), min(coordinate[3] + 1, 101)
        z1, z2 = max(coordinate[4], 0), min(coordinate[5] + 1, 101)
        if instructions[i] == 'on':
            cubes[x1:x2, y1:y2, z1:z2] = 1
        else:
            cubes[x1:x2, y1:y2, z1:z2] = 0
    return int(cubes.sum())


def part2(instructions, cuboids):
    on_volume = 0
    counts = defaultdict(int)
    for i, instruction in enumerate(instructions):
        on = True if instruction == 'on' else False
        cuboid = cuboids[i]
        new_counts = defaultdict(int)
        for projection, count in counts.items():
            intersection = cubes_intersection(cuboid, projection)
            if intersection:
                new_counts[intersection] -= count
        if on:
            new_counts[cuboid] += 1
        for projections, new_count in new_counts.items():
            counts[projections] += new_count
    for cuboid, count in counts.items():
        on_volume += cube_volume(cuboid) * count
    return on_volume


def main():
    day = 22
    instructions, projections, cuboids = data_prep(day)

    answer1 = part1(instructions, projections)
    answer2 = part2(instructions, cuboids)

    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
