def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [i.split(" ") for i in input_data]
    input_data = [i[:10] + i[-4:] for i in input_data]

    return input_data


def common_letters(number, lookup_number):
    return len(set(number).intersection(set(lookup_number)))


def pattern_decoder(signal, known_numbers_lengths):
    mapped_letters = {}
    five = []
    six = []
    for number in signal:
        if len(number) in known_numbers_lengths:
            mapped_letters[known_numbers_lengths[len(number)]] = number
        elif len(number) == 5:
            five.append(number)
        else:
            six.append(number)
    for number in five:
        if common_letters(number, mapped_letters[4]) == 2:
            mapped_letters[2] = number
        elif common_letters(number, mapped_letters[1]) == 2:
            mapped_letters[3] = number
        else:
            mapped_letters[5] = number
    for number in six:
        if common_letters(number, mapped_letters[1]) == 1:
            mapped_letters[6] = number
        elif common_letters(number, mapped_letters[4]) == 4:
            mapped_letters[9] = number
        else:
            mapped_letters[0] = number

    patterns = {"".join(sorted(pattern)): number for (number, pattern) in mapped_letters.items()}

    return patterns


def identifier_decoder(signal, output, numbers_identifier):
    letter_counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for number in signal:
        for letter in number:
            letter_counts[letter] += 1
    unscrambled = []
    for number in output:
        total = 0
        for letter in number:
            total += letter_counts[letter]
        unscrambled.append(numbers_identifier[total])
    return unscrambled


# noinspection SpellCheckingInspection
def numbers_identifiers():
    numbers_patterns = {0: 'cagedb', 1: 'ab', 2: 'gcdfa', 3: 'fbcad', 4: 'eafb',
                        5: 'cdfbe', 6: 'cdfgeb', 7: 'dab', 8: 'acedgfb', 9: 'cefabd'}
    letter_counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for key, value in numbers_patterns.items():
        for letter in value:
            letter_counts[letter] += 1
    numbers_identifier = {}
    for key, value in numbers_patterns.items():
        total = 0
        for letter in value:
            total += letter_counts[letter]
        numbers_identifier[total] = key
    return numbers_identifier


def part1(entries, known_numbers_lengths):
    count = 0
    for entry in entries:
        output = entry[-4:]
        for n in output:
            if len(n) in known_numbers_lengths:
                count += 1
    return count


# Alternative method using deduction
def part2_pattern_matching(entries, known_numbers_lengths):
    total = 0
    for entry in entries:
        signal = entry[:10]
        output = entry[-4:]
        patterns = pattern_decoder(signal, known_numbers_lengths)
        four_digits = ''
        for n in output:
            sorted_number_pattern = "".join(sorted(n))
            four_digits += str(patterns[sorted_number_pattern])
        total += int(four_digits)

    return total


def part2(entries):
    total = 0
    for entry in entries:
        signal = entry[:10]
        output = entry[-4:]
        output = identifier_decoder(signal, output, numbers_identifiers())
        four_digits = ''
        for n in output:
            four_digits += str(n)
        total += int(four_digits)

    return total


def main():
    day = 8
    entries = data_prep(day)
    known_numbers_lengths = {2: 1, 3: 7, 4: 4, 7: 8}
    answer1 = part1(entries, known_numbers_lengths)
    answer2 = part2(entries)
    # answer2_2 = part2_pattern_matching(entries, known_numbers_lengths))
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')
    # print(f'Day {day} part 2_v2 answer: {answer2_2}')


if __name__ == "__main__":
    main()
