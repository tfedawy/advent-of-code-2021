from collections import deque


# Not needed in this problem, but included for potential future use
def shortest_path_to_end(graph, source, destination):
    visited = []
    queue = deque()
    queue.append([source, [source]])
    path = []

    while queue:
        node, path = queue.popleft()
        if node == destination:
            return path
        for dst in graph[node]:
            if dst not in visited:
                visited.append(dst)
                queue.append([dst, path + [dst]])
    return path


# Returns the actual paths as well as the count
def find_paths(graph, repeat_allowed):
    stack = deque()
    stack.append([['start'], ['start'], False])
    count = 0
    paths = []
    while stack:
        path, small_caves, small_cave_repeated = stack.pop()
        for cave in graph[path[-1]]:
            if cave == 'end':
                count += 1
                paths.append(path + [cave])
            elif cave.islower():
                if cave not in small_caves:
                    new_small_caves = small_caves.copy()
                    new_small_caves.append(cave)
                    stack.append([path + [cave], new_small_caves, small_cave_repeated])
                elif cave != 'start' and repeat_allowed and not small_cave_repeated:
                    stack.append([path + [cave], small_caves, True])
            else:
                stack.append([path + [cave], small_caves, small_cave_repeated])
    return count, paths


# Returns only the count of the paths
def count_paths(graph, repeat_allowed):
    stack = deque()
    stack.append(['start', ['start'], False])
    count = 0
    while stack:
        cave, small_caves, small_cave_repeated = stack.pop()
        for neighbor in graph[cave]:
            if neighbor == 'end':
                count += 1
            elif neighbor.islower():
                if neighbor not in small_caves:
                    new_small_caves = small_caves.copy()
                    new_small_caves.append(neighbor)
                    stack.append([neighbor, new_small_caves, small_cave_repeated])
                elif neighbor != 'start' and repeat_allowed and not small_cave_repeated:
                    stack.append([neighbor, small_caves, True])
            else:
                stack.append([neighbor, small_caves, small_cave_repeated])
    return count


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [i.split('-') for i in input_data]
    adjacency_dict = {}
    for i in input_data:
        src, dst = i
        if src not in adjacency_dict:
            adjacency_dict[src] = []
        if dst not in adjacency_dict:
            adjacency_dict[dst] = []
        adjacency_dict[src].append(dst)
        adjacency_dict[dst].append(src)

    return adjacency_dict


def part1(graph, version='count_only'):
    if version == 'count_only':
        count = count_paths(graph, False)
    else:
        count, paths = find_paths(graph, False)
    # print(paths)
    return count


def part2(graph, version='count_only'):
    if version == 'count_only':
        count = count_paths(graph, True)
    else:
        count, paths = find_paths(graph, True)
    # print(paths)
    return count


def main():
    day = 12
    graph = data_prep(day)

    answer1 = part1(graph)
    answer2 = part2(graph)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
