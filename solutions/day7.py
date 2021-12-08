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


# Sum of numbers from 1 to n is called Triangular Number, and is calculated using the Guass formula n * (n+1) /2
def triangular_number(n):
    return int(n * (n + 1) / 2)


# The median minimizes the sum of absolute deviation. Proof and explanation can be found at:
# https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm
# So for part 1, we just need to get the median position and calculate the consumption
def part1(crabs):
    target = np.median(crabs)

    consumption = sum([abs(i - target) for i in crabs])

    return int(consumption)


# The mean minimizes the square differences between the positions and the target position.
# but since the position needs to be integer, we calculate the floor and ceiling and take the minimum of the two
def part2(crabs):
    mean_position = np.mean(crabs)
    floor = np.floor(mean_position)
    ceiling = np.ceil(mean_position)
    floor_consumption = sum([triangular_number(abs(i - floor)) for i in crabs])
    ceiling_consumption = sum([triangular_number(abs(i - ceiling)) for i in crabs])

    return min(floor_consumption, ceiling_consumption)


def main():
    day = 7
    crabs = data_prep(day)

    answer1 = part1(crabs)
    answer2 = part2(crabs)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
