from collections import deque


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    return input_data


def lines_parser(lines):
    right_legal_dict = {'}': '{', ']': '[', ')': '(', '>': '<'}
    left_legal_dict = {value: key for (key, value) in right_legal_dict.items()}
    corrupting_characters = []
    completion_lists = []

    for line in lines:
        stack = deque()
        stack.append(line[0])
        uncorrupted = True
        incomplete = False
        completion_list = []
        for i in range(1, len(line)):
            character = line[i]
            if character in right_legal_dict:
                if right_legal_dict[character] == stack[-1]:
                    stack.pop()
                else:
                    corrupting_characters.append(character)
                    uncorrupted = False
                    break
            else:
                stack.append(character)
        while len(stack) > 0 and uncorrupted:
            incomplete = True
            completion_character = left_legal_dict[stack.pop()]
            completion_list.append(completion_character)
        if incomplete:
            completion_lists.append(completion_list)

    return corrupting_characters, completion_lists


def part1(corrupting_characters):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for character in corrupting_characters:
        score += points[character]

    return score


def part2(completion_lists):
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    total_score = []
    for completion_list in completion_lists:
        score = 0
        for character in completion_list:
            score = score * 5 + points[character]
        total_score.append(score)

    total_score = sorted(total_score)
    middle = int(len(total_score) / 2)
    return total_score[middle]


def main():
    day = 10
    lines = data_prep(day)
    corrupting_characters, completion_lists = lines_parser(lines)

    answer1 = part1(corrupting_characters)
    answer2 = part2(completion_lists)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
