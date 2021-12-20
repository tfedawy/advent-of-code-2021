import ast
import math
from collections import deque


class SnailFishNumber:
    def __init__(self, number, parent=None):
        self.parent = parent
        self.value = None
        self.left = None
        self.right = None
        self.next_right = None
        self.next_left = None
        if isinstance(number, list):
            self.build(number)
        else:
            self.value = number
        connect(self)

    def build(self, number):
        left = number[0]
        right = number[1]
        self.left = SnailFishNumber(left, self)
        self.right = SnailFishNumber(right, self)

    def get_number(self):
        if self.value is not None:
            return self.value
        left = self.left.get_number()
        right = self.right.get_number()
        return [left, right]

    def get_next_real_numbers(self):
        next_left = self.next_left
        next_right = self.next_right
        parent = self.parent
        while not next_left and parent:
            next_left = parent.next_left
            parent = parent.parent
        while not next_right and parent:
            next_right = parent.next_right
            parent = parent.parent
        return next_left, next_right

    def explode(self):
        stack = deque()
        stack.append([self, 1])
        while stack:
            current, depth = stack.pop()
            if current:
                if current.value is None and depth == 5:
                    # print('Explosion', current)
                    left_real_number, right_real_number = current.get_next_real_numbers()
                    if left_real_number and left_real_number.value is not None:
                        left_real_number.value += current.left.value
                    elif left_real_number:
                        left_real_number.right.value += current.left.value
                    if right_real_number and right_real_number.value is not None:
                        right_real_number.value += current.right.value
                    elif right_real_number:
                        right_real_number.left.value += current.right.value
                    current.value, current.left, current.right = 0, None, None
                    return True
                stack.append([current.right, depth + 1])
                stack.append([current.left, depth + 1])

    def split(self):
        stack = deque()
        stack.append(self)
        while stack:
            current = stack.pop()
            if current:
                if current.value and current.value >= 10:
                    split_value = [math.floor(current.value / 2), math.ceil(current.value / 2)]
                    current.build(split_value)
                    current.value = None
                    connect(current)
                    return True
                stack.append(current.right)
                stack.append(current.left)

    def reduce(self):
        while self.explode():
            connect(self)
            self.reduce()
        if self.split():
            connect(self)
            self.reduce()

    def get_magnitude(self):
        if self.value:
            return self.value
        left = self.left
        right = self.right
        if left:
            left = self.left.get_magnitude()
        if right:
            right = self.right.get_magnitude()
        if left is None:
            left = 0
        if right is None:
            right = 0
        return 3 * left + 2 * right

    def __str__(self):
        left = self.left.__str__()
        right = self.right.__str__()
        return f'Value: {self.value}\nleft: {left}\nright: {right}'

    def __repr__(self):
        return self.__str__()


def connect(root):
    if root is None:
        return
    if root.left:
        root.left.next_right = root.right
    if root.right:
        root.right.next_left = root.left
    if root.next_left is not None and root.left:
        root.left.next_left = root.next_left.right
    if root.next_right is not None and root.right:
        root.right.next_right = root.next_right.left
    connect(root.left)
    connect(root.right)
    return


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [ast.literal_eval(n) for n in input_data]
    return input_data


def part1(input_data):
    snail_fish_number = SnailFishNumber([input_data[0], input_data[1]])
    snail_fish_number.reduce()
    for i in range(2, len(input_data)):
        snail_fish_number = SnailFishNumber([snail_fish_number.get_number(), input_data[i]])
        snail_fish_number.reduce()
    return snail_fish_number.get_magnitude()


def part2(input_data):
    max_magnitude = 0
    for i, number1 in enumerate(input_data):
        for j, number2 in enumerate(input_data):
            if number1 != number2:
                snail_fish_number = SnailFishNumber([number1, number2])
                snail_fish_number.reduce()
                magnitude = snail_fish_number.get_magnitude()
                if magnitude > max_magnitude:
                    max_magnitude = magnitude
    return max_magnitude


def main():
    day = '18'
    input_data = data_prep(day)

    answer1 = part1(input_data)
    answer2 = part2(input_data)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
