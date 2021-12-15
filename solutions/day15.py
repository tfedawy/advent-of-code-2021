import heapq as hp
from collections import defaultdict

import numpy as np


class Graph:
    def __init__(self, grid):
        self.points = None
        self.graph = None
        self.shape = None
        self.construct_graph_from_grid(grid)

    def construct_graph_from_grid(self, grid):
        shape = (len(grid), len(grid[0]))
        points = {}
        graph = defaultdict(list)
        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                neighbors = [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]
                point = (r, c)
                points[point] = value
                for neighbor_row, neighbor_col in neighbors:
                    if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[r]):
                        graph[point].append((neighbor_row, neighbor_col))
        self.points = points
        self.graph = graph
        self.shape = shape

    def expand(self, factor=5):
        expanded_grid = np.ones((self.shape[0] * factor, self.shape[1] * factor))
        for point, risk in self.points.items():
            expanded_grid[point] = risk
        for r in range(self.shape[0]):
            for i in range(1, factor):
                expanded_grid[r + self.shape[0] * i, :] = (expanded_grid[r, :] + i)
        for c in range(self.shape[1]):
            for i in range(1, factor):
                expanded_grid[:, c + self.shape[1] * i] = (expanded_grid[:, c] + i)
        for point, risk in self.points.items():
            expanded_grid[point] = risk
        expanded_grid[np.where(expanded_grid > 9)] += 1
        expanded_grid[np.where(expanded_grid > 9)] = expanded_grid[np.where(expanded_grid > 9)] % 10

        self.construct_graph_from_grid(expanded_grid)
        return expanded_grid

    def print_graph(self, path=None):
        bold = '\033[1m'
        green = '\u001b[38;2;0;255;0m'
        normal = '\033[0m'
        if not path:
            path = []
        for row in range(self.shape[0]):
            for col in range(self.shape[1]):
                value = int(self.points[row, col])
                if (row, col) in path:
                    print(bold + green + str(value) + normal, end=' ')
                else:
                    print(value, end=' ')
            print()

    def print_expansion(self):
        normal = '\033[0m'
        for row in range(self.shape[0]):
            for col in range(self.shape[1]):
                level = (max(row // 10, col // 10) + 1) * 100
                blue_value = (255 + level) % 255
                blue_shade = '\u001b[38;2;58;150;' + str(blue_value) + 'm'
                value = int(self.points[row, col])
                print(blue_shade + str(value) + normal, end=' ')
            print()

    def dijkstra(self, source):
        shortest_path_set = {}
        shortest_path = {source: None}
        nodes_to_visit = {point: np.inf for point in self.points}
        nodes_to_visit[source] = 0
        dist = nodes_to_visit.copy()
        nodes_to_visit = [(distance, point) for point, distance in nodes_to_visit.items()]
        hp.heapify(nodes_to_visit)
        while len(shortest_path_set) < len(self.points):
            current_node_distance, current_node = hp.heappop(nodes_to_visit)
            shortest_path_set[current_node] = current_node_distance

            for neighbor in self.graph[current_node]:
                if neighbor not in shortest_path_set:
                    distance = shortest_path_set[current_node] + self.points[current_node]
                    if distance < dist[neighbor]:
                        dist[neighbor] = distance
                        hp.heappush(nodes_to_visit, (distance, neighbor))
                        shortest_path[neighbor] = current_node
        return shortest_path_set, shortest_path

    # Difference from Dijkstra's _algorithm is that it stops as soon as it reaches the destination
    def a_star(self, source, destination):
        shortest_path_set = {}
        shortest_path = {source: None}
        nodes_to_visit = {point: np.inf for point in self.points}
        nodes_to_visit[source] = 0
        nodes_to_visit = [(distance, point) for point, distance in nodes_to_visit.items()]
        hp.heapify(nodes_to_visit)
        while nodes_to_visit:
            current_node_distance, current_node = hp.heappop(nodes_to_visit)
            shortest_path_set[current_node] = current_node_distance
            if current_node == destination:
                return shortest_path_set, shortest_path
            for neighbor in self.graph[current_node]:
                distance = current_node_distance + self.points[current_node]
                if neighbor not in shortest_path_set:
                    distance = current_node_distance + self.points[current_node]
                    shortest_path_set[neighbor] = distance
                    shortest_path[neighbor] = current_node
                    hp.heappush(nodes_to_visit, (distance, neighbor))
                else:
                    if distance < shortest_path_set[neighbor]:
                        shortest_path_set[neighbor] = distance
                        shortest_path[neighbor] = current_node
                        hp.heappush(nodes_to_visit, (distance, neighbor))


def backtrack_path(path, end):
    backtracked_path = [end]
    node = path[end]
    while node:
        backtracked_path.append(node)
        node = path[node]
    return backtracked_path


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    grid = get_data(day)
    grid = grid.split('\n')
    grid = [list(map(int, list(i))) for i in grid]
    return grid


def part1(graph, source):
    destination = (graph.shape[0] - 1, graph.shape[1] - 1)
    risk_dict, paths = graph.dijkstra(source)
    # risk_dict, paths = graph.a_star(source, destination)
    # path = backtrack_path(paths, destination)
    # graph.print_graph(path)
    total_risk = risk_dict[destination] - graph.points[source] + graph.points[destination]
    return total_risk


def part2(graph, source):
    graph.expand(5)
    destination = (graph.shape[0] - 1, graph.shape[1] - 1)
    risk_dict, paths = graph.dijkstra(source)
    # risk_dict, paths = graph.a_star(source, destination)
    # path = backtrack_path(paths, destination)
    # graph.print_graph(path)
    # graph.print_expansion()
    total_risk = risk_dict[destination] - graph.points[source] + graph.points[destination]
    return int(total_risk)


def main():
    day = 15
    grid = data_prep(day)
    graph = Graph(grid)
    source = (0, 0)

    answer1 = part1(graph, source)
    answer2 = part2(graph, source)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')
    # graph.print_expansion()


if __name__ == "__main__":
    main()
