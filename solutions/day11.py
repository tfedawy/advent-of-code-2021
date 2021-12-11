class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.neighbors = []
        self.flashed_this_round = False

    def increase_energy(self):
        if not self.flashed_this_round:
            self.energy += 1
            if self.energy > 9:
                self.flash()

    def flash(self):
        self.flashed_this_round = True
        self.energy = 0
        for neighbor in self.neighbors:
            neighbor.increase_energy()


class OctopusGrid:
    def __init__(self, grid):
        self.grid = []
        for row in range(len(grid)):
            self.grid.append([])
            for o_energy in grid[row]:
                self.grid[row].append(Octopus(o_energy))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                for r in range(-1, 2):
                    for c in range(-1, 2):
                        if r == 0 and c == 0:
                            pass
                        else:
                            neighbor_row = row + r
                            neighbor_col = col + c
                            if 0 <= neighbor_row < len(self.grid) and 0 <= neighbor_col < len(self.grid[row]):
                                self.grid[row][col].neighbors.append(self.grid[neighbor_row][neighbor_col])
        self.step_flash_count = 0
        self.total_flash_count = 0

    def simulate_step(self):
        self.step_flash_count = 0
        for row in self.grid:
            for octopus in row:
                octopus.increase_energy()
        for row in self.grid:
            for octopus in row:
                if octopus.flashed_this_round:
                    self.step_flash_count += 1
                    self.total_flash_count += 1
                    octopus.flashed_this_round = False

    def print_grid(self):
        bold = '\033[1m'
        light_green = '\u001b[38;2;0;200;0m'
        green = '\u001b[38;2;0;255;0m'
        normal = '\033[0m'
        for row in self.grid:
            for octopus in row:
                if octopus.energy == 0:
                    if self.step_flash_count == len(self.grid) ** 2:
                        print(bold + green + str(octopus.energy) + normal, end=' ')
                    else:
                        print(bold + light_green + str(octopus.energy) + normal, end=' ')
                else:
                    print(octopus.energy, end=' ')
                    pass
            print()
        print()


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [[int(n) for n in i] for i in input_data]
    return input_data


def part1(octopus_grid, steps):
    for step in range(steps):
        octopus_grid.simulate_step()
        # print('Step', step + 1, 'Total Flash Count:', octopus_grid.total_flash_count)
    return octopus_grid.total_flash_count


def part2(octopus_grid):
    step = 0
    while octopus_grid.step_flash_count != len(octopus_grid.grid) ** 2:
        step += 1
        octopus_grid.simulate_step()
        # print('After step:', step, 'Flash Count:', octopus_grid.step_flash_count)
        # octopus_grid.print_grid()
    return step


def main():
    day = 11
    octopus_data = data_prep(day)
    octopus_grid1 = OctopusGrid(octopus_data)
    octopus_grid2 = OctopusGrid(octopus_data)

    answer1 = part1(octopus_grid1, 100)
    answer2 = part2(octopus_grid2)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
