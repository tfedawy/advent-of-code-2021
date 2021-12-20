import itertools
from collections import defaultdict

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


class Scanner:
    def __init__(self, number, readings):
        self.number = number
        self.readings = readings
        self._position = (0, 0, 0)
        self.rotation = (0, 1, 2)

    def rotate(self, perm, perm_sign):
        self.rotation = perm
        self.readings = self.readings[:, perm] * perm_sign

    def adjust_readings_relative_to_zero(self, relative_position):
        self._position = tuple(relative_position)
        self.readings -= relative_position

    @property
    def position(self):
        return self._position

    def __str__(self):
        return f'{self.number},\t\t\tRelative Position: {self._position},\t\tRotation: {self.rotation}'

    def __repr__(self):
        return self.__str__()


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n\n')
    input_data = [i.split('\n') for i in input_data]
    input_data = [[i.split(',') for i in j] for j in input_data]
    scanners = []
    for s in input_data:
        number = int(s[0][0].split(' ')[2])
        readings = np.array([list(map(int, i)) for i in s[1:]])
        scanners.append(Scanner(number, readings))
    return scanners


def multiplier(n):
    if n > 0:
        return 1
    else:
        return -1


def column(n):
    return abs(n) - 1


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) + abs(point1[2] - point2[2])


def get_column_permutations(number_of_columns):
    col_permutations = set(itertools.permutations(range(1, number_of_columns + 1), number_of_columns))
    col_signs = set(itertools.permutations([1, -1] * number_of_columns, number_of_columns))
    permutations = []
    for col_permutation in col_permutations:
        for col_sign in col_signs:
            permutation = []
            for i in range(3):
                permutation.append(list(col_permutation)[i] * list(col_sign)[i])
            permutations.append(tuple(permutation))
    permutations_signs = set([tuple(map(multiplier, i)) for i in permutations])
    permutations = set([tuple(map(column, i)) for i in permutations])
    return permutations, permutations_signs


def get_relative_position(base_reading, relative_reading, perms, perms_signs):
    for perm in perms:
        for perm_sign in perms_signs:
            reading_permutation = relative_reading[:, perm] * tuple(perm_sign)
            deltas = []
            positions = []
            positions_dict = defaultdict(int)
            for i, reading in enumerate(base_reading):
                deltas.append(reading_permutation - reading)
            for delta in deltas:
                for d in delta:
                    positions.append(tuple(d))
            for position in positions:
                positions_dict[position] += 1
            if positions_dict[max(positions_dict, key=positions_dict.get)] >= 12:
                return np.array(max(positions_dict, key=positions_dict.get)), tuple(perm), tuple(perm_sign)
    return None, None, None


def plot_beacons(scanners, beacons):
    scanners_positions = [scanner.position for scanner in scanners]
    beacons_positions = [list(beacon) for beacon in beacons]
    scanners_positions_df = pd.DataFrame(scanners_positions, columns=['x', 'y', 'z'])
    beacons_positions_df = pd.DataFrame(beacons_positions, columns=['x', 'y', 'z'])
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(scanners_positions_df.x, scanners_positions_df.y, scanners_positions_df.z,
               color='g', label='Scanner')
    ax.scatter(beacons_positions_df.x, beacons_positions_df.y, beacons_positions_df.z,
               color='r', label='Beacon')
    ax.set_xlabel('Horizontal position')
    ax.set_ylabel('Vertical Position')
    ax.set_zlabel('Depth')
    ax.legend()
    plt.show()


def part1(scanners):
    perms, perms_signs = get_column_permutations(len(scanners[0].readings[0]))
    fixed_scanners = [scanners[0]]
    while len(fixed_scanners) < len(scanners):
        for scanner in scanners:
            if scanner not in fixed_scanners:
                for fixed_scanner in fixed_scanners:
                    relative_pos, perm, perm_sign = get_relative_position(fixed_scanner.readings, scanner.readings,
                                                                          perms, perms_signs)
                    if relative_pos is not None:
                        scanner.rotate(perm, perm_sign)
                        scanner.adjust_readings_relative_to_zero(relative_pos)
                        fixed_scanners.append(scanner)
                        # print('\u2705 Mapped Scanner', scanner)
                        break
    beacons = set()
    for scanner in scanners:
        for reading in scanner.readings:
            beacons.add(tuple(reading))
    return len(beacons), beacons


def part2(scanners):
    max_distance = 0
    for scanner1 in scanners:
        for scanner2 in scanners:
            distance = manhattan_distance(scanner1.position, scanner2.position)
            if distance > max_distance:
                max_distance = distance
    return max_distance


def main():
    day = 19
    scanners = data_prep(day)

    answer1, beacons = part1(scanners)
    answer2 = part2(scanners)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')
    plot_beacons(scanners, beacons)


if __name__ == "__main__":
    main()
