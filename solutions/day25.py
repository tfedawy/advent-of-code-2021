import numpy as np


class SeaFloor:
    def __init__(self, grid):
        self.grid = grid
        self.shape = (len(self.grid), len(self.grid[0]))
        self.movement_grid = np.zeros(self.shape)
        self.steps = 1

    def move(self):
        moved_right = True
        moved_down = True
        while moved_right or moved_down:
            moved_right = self.move_right()
            moved_down = self.move_down()
            if moved_right or moved_down:
                self.steps += 1

    def move_right(self):
        moved = False
        for r, row in enumerate(self.grid):
            for c, sea_cucumber in enumerate(row):
                previous_c = c - 1
                if sea_cucumber == '.':
                    if self.grid[r][previous_c] == '>':
                        self.movement_grid[r][previous_c] = 1
        for r, row in enumerate(self.grid):
            for c, sea_cucumber in enumerate(row):
                next_c = (c + 1) % (self.shape[1])
                if sea_cucumber == '>' and self.movement_grid[r][c] == 1:
                    self.movement_grid[r][c] = 0
                    moved = True
                    self.grid[r][next_c] = sea_cucumber
                    self.grid[r][c] = '.'
        return moved

    def move_down(self):
        moved = False
        for r, row in enumerate(self.grid):
            previous_r = r - 1
            for c, sea_cucumber in enumerate(row):
                if sea_cucumber == '.':
                    if self.grid[previous_r][c] == 'v':
                        self.movement_grid[previous_r][c] = 1

        for r, row in enumerate(self.grid):
            next_r = (r + 1) % (self.shape[0])
            for c, sea_cucumber in enumerate(row):
                if sea_cucumber == 'v' and self.movement_grid[r][c] == 1:
                    moved = True
                    self.movement_grid[r][c] = 0
                    self.grid[next_r][c] = sea_cucumber
                    self.grid[r][c] = '.'
        return moved

    def display(self):
        for row in self.grid:
            for col in row:
                print(col, end='')
            print()


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [list(line) for line in input_data]
    return input_data


def part1(sea_floor):
    sea_floor.move()
    return sea_floor.steps


def main():
    day = '25'
    grid = data_prep(day)
    sea_floor = SeaFloor(grid)

    answer1 = part1(sea_floor)
    sea_floor.display()

    print(f'Day {day} part 1 answer: {answer1}')
    print(f'\n🎄🎄🎄MERRY CHRISTMAS🎄🎄🎄')


if __name__ == "__main__":
    main()
