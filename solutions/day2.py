def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [[line.split()[0], int(line.split()[1])] for line in input_data]

    return input_data


def part1(data):
    horizontal = 0
    depth = 0
    for line in data:
        if line[0] == 'up':
            depth -= line[1]
        if line[0] == 'down':
            depth += line[1]
        if line[0] == 'forward':
            horizontal += line[1]

    return horizontal * depth


def part2(data):
    horizontal = 0
    depth = 0
    aim = 0
    for line in data:
        if line[0] == 'up':
            aim -= line[1]
        if line[0] == 'down':
            aim += line[1]
        if line[0] == 'forward':
            horizontal += line[1]
            depth += line[1] * aim

    return horizontal * depth


def main():
    day = 2
    input_data = data_prep(day)

    answer1 = part1(input_data)
    answer2 = part2(input_data)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
