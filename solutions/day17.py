import re


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = re.split('[=.,]', input_data)
    input_data = [int(input_data[i]) for i in [1, 3, 5, 7]]
    min_x, max_x, min_y, max_y = input_data

    return min_x, max_x, min_y, max_y


def find_velocities(min_x, max_x, min_y, max_y):
    valid_initial_velocity = {}
    for x in range(max_x + 1):
        for y in range(min_y, -min_y + 1):
            reached_target = False
            max_height = 0
            x_velocity = x
            y_velocity = y
            x_position = 0
            y_position = 0
            while True:
                x_position += x_velocity
                y_position += y_velocity
                if y_position > max_height:
                    max_height = y_position
                if min_x <= x_position <= max_x and min_y <= y_position <= max_y:
                    reached_target = True
                    break
                elif x_position > max_x or y_position < min_y:
                    break
                if x_velocity > 0:
                    x_velocity -= 1
                elif x_velocity < 0:
                    x_velocity += 1
                y_velocity -= 1
            if reached_target:
                valid_initial_velocity[(x, y)] = max_height
    return valid_initial_velocity


def triangular_number(n):
    return int(n * (n + 1) / 2)


def part1(valid_initial_velocity):
    return max(valid_initial_velocity.values())


def part2(valid_initial_velocity):
    return len(valid_initial_velocity)


def main():
    day = 17
    min_x, max_x, min_y, max_y = data_prep(day)
    valid_initial_velocity = find_velocities(min_x, max_x, min_y, max_y)

    answer1 = part1(valid_initial_velocity)
    answer2 = part2(valid_initial_velocity)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
