from collections import deque


class ALU:
    def __init__(self, instructions):
        self.instructions = instructions

    def validate(self, n):
        z = 0
        n = self.queue_n(n)
        if 0 in n:
            return False
        for i in range(14):
            sequence = i * 18
            w = n.popleft()
            z = self._process_instruction(z, w, sequence)
        return z == 0

    def _process_instruction(self, z, w, sequence):
        z_divisor = int(self.instructions[sequence + 4][-1])
        x_addition = int(self.instructions[sequence + 5][-1])
        y_addition = int(self.instructions[sequence + 15][-1])
        if w == z % 26 + x_addition:
            return z // z_divisor
        else:
            return (z // z_divisor) * 26 + w + y_addition

    @staticmethod
    def queue_n(n):
        n = list(str(n))
        n = list(map(int, n))
        return deque(n)


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    instructions = [line.split(' ') for line in input_data]
    return instructions


def calculate_monad(monad, alu):
    z = []
    for i in range(14):
        sequence = i * 18
        divisor, x, y = map(int, [alu.instructions[sequence + j][-1] for j in [4, 5, 15]])
        if divisor == 1:
            z.append((i, y))
        elif divisor == 26:
            j, y = z.pop()
            monad[i] = monad[j] + x + y
            if monad[i] > 9:
                monad[j] -= monad[i] - 9
                monad[i] = 9
            elif monad[i] < 1:
                monad[j] += 1 - monad[i]
                monad[i] = 1
    return ''.join(map(str, monad))


def part1(alu):
    monad = calculate_monad([9] * 14, alu)
    if alu.validate(monad):
        return monad


def part2(alu):
    monad = calculate_monad([1] * 14, alu)
    if alu.validate(monad):
        return monad


def main():
    day = 24
    instructions = data_prep(day)
    alu = ALU(instructions)

    answer1 = part1(alu)
    answer2 = part2(alu)

    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
