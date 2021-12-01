def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    print(input_data)

    return input_data


def part1():
    pass


def part2():
    pass


def main():
    day = 0
    data = data_prep(day)

    answer1 = part1()
    answer2 = part2()

    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
