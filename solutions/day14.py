from collections import defaultdict


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    polymer_template = input_data[0]
    input_data = [i.split(' -> ') for i in input_data[2:]]
    pair_insertion = {i[0]: i[1] for i in input_data}

    return polymer_template, pair_insertion


# Naive brute force approach
def part1(polymer_template, pair_insertion, steps):
    for step in range(steps):
        new_polymer = []
        for i in range(len(polymer_template)):
            letter = polymer_template[i]
            pair = polymer_template[i:i + 2]
            if pair in pair_insertion:
                new_polymer += [letter + pair_insertion[pair]]
            else:
                new_polymer += [letter]
        polymer_template = ''.join(new_polymer)

    letter_count = defaultdict(int)
    for letter in polymer_template:
        letter_count[letter] += 1
    most_common_letter, least_common_letter = max(letter_count.values()), min(letter_count.values())

    return most_common_letter - least_common_letter


def part2(polymer_template, pair_insertion, steps):
    letter_count = defaultdict(int)
    pairs_count = defaultdict(int)

    for letter in polymer_template:
        letter_count[letter] += 1

    for i in range(len(polymer_template) - 1):
        pair = polymer_template[i:i + 2]
        pairs_count[pair] += 1

    for step in range(steps):
        new_pairs_count = defaultdict(int)
        for pair, count in pairs_count.items():
            if pair in pair_insertion:
                added_letter = pair_insertion[pair]
                letter_count[added_letter] += count
                new_pair_1 = pair[0] + added_letter
                new_pair_2 = added_letter + pair[1]
                new_pairs_count[new_pair_1] += count
                new_pairs_count[new_pair_2] += count
        pairs_count = new_pairs_count.copy()

    most_common_letter, least_common_letter = max(letter_count.values()), min(letter_count.values())
    return most_common_letter - least_common_letter


def main():
    day = 14
    polymer_template, pair_insertion = data_prep(day)

    answer1 = part1(polymer_template, pair_insertion, 10)
    answer2 = part2(polymer_template, pair_insertion, 40)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
