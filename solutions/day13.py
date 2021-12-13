import re

import numpy as np


class TransparentPaper:
    def __init__(self, dots):
        self.shape = [max(dots[:, 1]), max(dots[:, 0])]
        self.grid = np.zeros((self.shape[0] + 1, self.shape[1] + 1))
        self.grid[dots[:, 1], dots[:, 0]] = 1

    def sum_dots(self):
        return len(np.where(self.grid > 0)[0])

    def fold(self, instruction):
        axis, f = instruction
        if axis == 'x':
            for col in range(f):
                self.grid[:, col] += self.grid[:, 2 * f - col]
                self.grid[:, 2 * f - col] = 0
            self.shape[1] = f
        if axis == 'y':
            for row in range(f):
                self.grid[row, :] += self.grid[2 * f - row, :]
                self.grid[2 * f - row, :] = 0
            self.shape[0] = f

    def print_paper(self):
        bold = '\033[1m'
        steel_blue = '\u001b[38;2;97;214;214m'
        green = '\u001b[38;2;0;255;0m'
        normal = '\033[0m'
        for row in self.grid[:self.shape[0]]:
            for col, val in enumerate(row[:self.shape[1]]):
                letter = np.floor(col / (self.shape[1] / 8))
                if val > 0:
                    if letter % 2 == 0:
                        print(bold + green + 'o' + normal, end=' ')
                    else:
                        print(bold + steel_blue + 'o' + normal, end=' ')
                else:
                    print(' ', end=' ')
            print()


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n\n')
    dots = input_data[0].split('\n')
    instructions = input_data[1].split('\n')
    dots = np.array([list(map(int, dot.split(','))) for dot in dots])
    instructions = [re.split("[ =]", instruction) for instruction in instructions]
    instructions = [[instruction[2], int(instruction[3])] for instruction in instructions]

    return dots, instructions


def part1(paper, instruction):
    paper.fold(instruction)
    return paper.sum_dots()


def part2(paper, instructions):
    for instruction in instructions:
        paper.fold(instruction)


def main():
    day = 13
    dots, instructions = data_prep(day)
    paper = TransparentPaper(dots)

    answer1 = part1(paper, instructions[0])
    part2(paper, instructions)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer:')
    paper.print_paper()


if __name__ == "__main__":
    main()
