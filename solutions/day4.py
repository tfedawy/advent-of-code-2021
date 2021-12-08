class Board:
    def __init__(self, values):
        self.size = len(values)
        self.values = values
        self.marked = [[0] * self.size for _ in range(self.size)]
        self.marked_values = []
        self.rows_tally = [0] * self.size
        self.columns_tally = [0] * self.size
        self.is_winner = False
        self.winning_guess = None

    def mark_guess(self, guess):
        for row in range(self.size):
            for column in range(self.size):
                if self.values[row][column] == guess:
                    self.marked_values.append(guess)
                    self.marked[row][column] = 1
                    self.rows_tally[row] += 1
                    self.columns_tally[column] += 1
                    if self.rows_tally[row] == self.size or self.columns_tally[column] == self.size:
                        self.is_winner = True
                        self.winning_guess = guess
                    return

    def get_score(self):
        score = 0
        for row in range(self.size):
            for column in range(self.size):
                if self.marked[row][column] == 0:
                    score += self.values[row][column] * self.winning_guess
        return score

    def print_board(self):
        # Formatting variables
        bold = '\033[1m'
        light_green = '\u001b[38;2;0;200;0m'
        green = '\u001b[38;2;0;255;0m'
        normal = '\033[0m'

        for row in range(self.size):
            for col in range(self.size):
                if self.marked[row][col] == 1:
                    value = str(self.values[row][col])
                    if self.rows_tally[row] == self.size or self.columns_tally[col] == self.size:
                        print(bold + green + value.ljust(4) + normal, end=' ')
                    else:
                        print(light_green + value.ljust(4) + normal, end=' ')
                else:
                    value = str(self.values[row][col])
                    print(value.ljust(4), end=' ')
            print()
        print()


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n\n')
    guesses = [int(i) for i in input_data[0].split(',')]
    b = [i.split('\n') for i in input_data[1:]]
    boards = []
    for i in range(len(b)):
        board_values = []
        for j in range(len(b[i])):
            board_values.append(list(map(int, b[i][j].split())))
        boards.append(Board(board_values))

    return guesses, boards


def play(guesses, boards):
    winners = []
    number_of_boards = len(boards)
    # print('##### Game started #####')
    for g, guess in enumerate(guesses):
        # print('Guess', g + 1, 'is:', guess)
        for b, board in enumerate(boards):
            if not board.is_winner:
                if guess not in board.marked_values:
                    board.mark_guess(guess)
                    if board.is_winner:
                        # rank = len(winners) + 1
                        winners.append(board)
                        # print('\nBoard', b, 'just won!! 🎉🎉\nRank:', rank, '\nScore:', board.get_score())
                        # board.print_board()
                        if len(winners) == number_of_boards:
                            return winners
    return winners


def part1(winners):
    return winners[0].get_score()


def part2(winners):
    return winners[-1].get_score()


def main():
    day = 4
    guesses, boards = data_prep(day)
    winners = play(guesses, boards)

    answer1 = part1(winners)
    answer2 = part2(winners)
    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
