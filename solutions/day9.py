from collections import deque


class Point:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def is_low(self):
        for neighbor in self.neighbors:
            if neighbor.val <= self.val:
                return False
        return True

    def risk_level(self):
        return self.val + 1


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [list(i) for i in input_data]
    input_data = [list(map(int, i)) for i in input_data]
    return input_data


def construct_height_map(input_data):
    points = []
    for r, row in enumerate(input_data):
        points.append([])
        for c, value in enumerate(row):
            new_point = Point(value)
            points[r].append(new_point)
    for r, row in enumerate(points):
        for c, point in enumerate(row):
            if r >= 1:
                point.neighbors.append(points[r - 1][c])
            if c >= 1:
                point.neighbors.append(points[r][c - 1])
            if r < len(points) - 1:
                point.neighbors.append(points[r + 1][c])
            if c < len(points[r]) - 1:
                point.neighbors.append(points[r][c + 1])
    return points


# Breadth First Search approach. The one used in the solution
def find_single_basin_BFS(point, visited):
    queue = deque()
    queue.append(point)
    basin = set()

    while queue:
        current = queue.popleft()
        visited.add(current)
        basin.add(current)
        for neighbor in current.neighbors:
            if neighbor not in visited and neighbor.val != 9:
                queue.append(neighbor)

    return basin


def find_all_basins_BFS(height_map):
    basins = []
    visited = set()
    for row in height_map:
        for point in row:
            if point not in visited and point.val != 9:
                basin = find_single_basin_BFS(point, visited)
                if len(basin) > 0:
                    basins.append(basin)
    return basins


# Recursive approach kept for reference. 8x slower than BFS
def find_single_basin_recursive(point, visited, basin):
    visited.append(point)
    basin.add(point)

    for neighbor in point.neighbors:
        if neighbor not in visited and neighbor.val != 9:
            basin = find_single_basin_recursive(neighbor, visited, basin)

    return basin


def find_all_basins_recursive(height_map):
    basins = []
    visited = []
    for row in height_map:
        for point in row:
            if point not in visited and point.val != 9:
                basin = find_single_basin_recursive(point, visited, set())
                if len(basin) > 0:
                    basins.append(basin)
    return basins


def print_height_map(height_map, basins, colors='random'):
    bold = '\033[1m'
    green = '\u001b[38;2;0;255;0m'
    red = '\u001b[38;2;255;0;0m'
    blue_shade = '\u001b[38;2;0;0;255m'
    normal = '\033[0m'
    basins_length = []
    for basin in basins:
        length = len(basin)
        if length not in basins_length:
            basins_length.append(length)
    basins_length = sorted(basins_length)
    print(len(basins), 'basins found, with', len(basins_length), 'unique basin sizes')
    for row in height_map:
        for point in row:
            for basin in basins:
                if point in basin:
                    if colors == 'blue':
                        blue_value = 255 - len(basins_length) + basins_length.index(len(basin))
                        blue_shade = '\u001b[38;2;58;150;' + str(blue_value) + 'm'
                    else:
                        r = str((255 - (basins_length.index(len(basin)) * len(basin) * 5)) % 255)
                        b = str((255 - (basins_length.index(len(basin)) * len(basin) * 12)) % 255)
                        g = str((255 - (basins_length.index(len(basin)) * len(basin) * 17)) % 255)
                        blue_shade = '\u001b[38;2;' + r + ';' + b + ';' + g + 'm'
                    break
            if point.is_low():
                print(bold + green + str(point.val) + normal, end='')
            elif point.val != 9:
                print(blue_shade + str(point.val) + normal, end='')
            else:
                print(red + str(point.val) + normal, end='')
        print()


def part1(height_map):
    total_risk = 0
    for row in height_map:
        for point in row:
            if point.is_low():
                total_risk += point.risk_level()
    return total_risk


def part2(basins):
    product = 1
    basins_lengths = []
    for b in basins:
        basins_lengths.append(len(b))
    basins_lengths = sorted(basins_lengths)
    for b in sorted(basins_lengths)[-3:]:
        product *= b
    return product


def main():
    day = 9
    input_data = data_prep(day)
    height_map = construct_height_map(input_data)
    # basins = find_all_basins_recursive(height_map)
    basins = find_all_basins_BFS(height_map)

    # print_height_map(height_map, basins)
    answer1 = part1(height_map)
    answer2 = part2(basins)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
