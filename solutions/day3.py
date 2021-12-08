def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [i.split()[0] for i in input_data]
    input_data = [list(map(int, i)) for i in input_data]

    return input_data


def get_dec(number_list):
    return int("".join(str(i) for i in number_list), 2)


def part1(data):
    counts = []
    for j in range(len(data[0])):
        counts.append(sum(i[j] for i in data))

    counts = [i / len(data) for i in counts]
    gamma_bin = [1 * (i >= 0.5) for i in counts]
    epsilon_bin = [1 * (i < 0.5) for i in counts]

    power_consumption = get_dec(gamma_bin) * get_dec(epsilon_bin)

    return power_consumption


def part2(data):
    j = 0
    oxygen_data = data.copy()
    while j < len(oxygen_data[0]) and len(oxygen_data) > 1:
        criteria = 1 * ((sum(i[j] for i in oxygen_data) / len(oxygen_data)) >= 0.5)
        new_data = []
        for i in oxygen_data:
            if i[j] == criteria:
                new_data.append(i)

        oxygen_data = new_data
        j += 1

    oxygen_dec = get_dec(oxygen_data[0])

    j = 0
    carbon_data = data.copy()
    while j < len(carbon_data[0]) and len(carbon_data) > 1:
        criteria = 1 * ((sum(i[j] for i in carbon_data) / len(carbon_data)) < 0.5)
        new_data = []
        for i in carbon_data:
            if i[j] == criteria:
                new_data.append(i)

        carbon_data = new_data
        j += 1

    carbon_dec = get_dec(carbon_data[0])

    return oxygen_dec * carbon_dec


def main():
    day = 3
    input_data = data_prep(day)

    answer1 = part1(input_data)
    answer2 = part2(input_data)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
