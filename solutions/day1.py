def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = list(map(int, input_data))

    return input_data


def part1(data):
    answer = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            answer += 1

    return answer


def part2(data):
    answer = 0
    for i in range(1, len(data) - 2):
        if sum(data[i:i + 3]) > sum(data[i - 1:i + 2]):
            answer += 1

    return answer


def main():
    day = 1
    input_data = data_prep(day)

    answer1 = part1(input_data)
    answer2 = part2(input_data)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
