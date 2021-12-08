import numpy as np


# noinspection DuplicatedCode
def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split(',')
    input_data = np.array([int(i) for i in input_data])
    return input_data


def fish_growth(fish, days):
    fish_population = [0] * 9
    for i in fish:
        fish_population[i] += 1

    for d in range(days):
        fish_population[:-1], fish_population[8] = fish_population[1:], fish_population[0]
        fish_population[6] += fish_population[8]

    return sum(fish_population)


def main():
    day = 6
    fish = data_prep(day)
    p1_days = 80
    p2_days = 256

    answer1 = fish_growth(fish, p1_days)
    answer2 = fish_growth(fish, p2_days)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
