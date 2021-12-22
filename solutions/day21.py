import itertools
from collections import defaultdict
from operator import attrgetter
from functools import lru_cache

import numpy as np


def calculate_new_position(position, step):
    return (position + step) % 10


def calculate_new_score(score, position):
    return score + position + 1


class Player:
    def __init__(self, number, position):
        self._number = number
        self._position = position
        self._score = 0

    def advance_position(self, step):
        self._position = calculate_new_position(self._position, step)
        self._score = calculate_new_score(self._score, self._position)

    def __str__(self):
        return f'Player {self._number}, Position: {self._position + 1}, Score: {self._score}'

    def __repr__(self):
        return self.__str__()

    @property
    def position(self):
        return self._position

    @property
    def score(self):
        return self._score

    @property
    def number(self):
        return self._number


class QuantumPlayer(Player):
    def __init__(self, number, position):
        self.number_of_wins = 0
        Player.__init__(self, number, position)

    def __str__(self):
        return f'Player {self._number}, Won: {self.number_of_wins:,} games'

    def __repr__(self):
        return self.__str__()


class DicraDiceGame:
    def __init__(self, players: [Player], winning_score=1000):
        self.players = players
        self.turn = 0
        self.die = 0
        self.winning_score = winning_score
        self.winner = None
        self.loser = None

    def roll_deterministic_die(self):
        self.die = (self.die + 3) % 100

    def step_size(self):
        return 3 * (self.die + 1) + 3

    def _play_round(self):
        self.players[self.turn % 2].advance_position(self.step_size())
        self.turn += 1
        self.roll_deterministic_die()

    def play(self):
        while max(self.players, key=attrgetter('score')).score < self.winning_score:
            self._play_round()
        self.winner = max(self.players, key=attrgetter('score'))
        self.loser = min(self.players, key=attrgetter('score'))

    def __str__(self):
        return f'Turn: {self.turn}\n{self.players[0]}\n{self.players[1]}'


class QuantumDicraDiceGame:
    def __init__(self, players: [QuantumPlayer], winning_score=21, die_sides=3):
        self.players = players
        self.die_sides = die_sides
        self.winning_score = winning_score
        self.steps = self.get_steps_frequency()
        self.initial_state = ((self.players[0].position, self.players[1].position), (0, 0), 0)
        self.number_of_games = 0
        self.winner = None
        self.loser = None

    def get_steps_frequency(self):
        rolls_perms = itertools.combinations_with_replacement(range(1, self.die_sides + 1), self.die_sides)
        rolls_perms = [p for p in set(map(itertools.permutations, rolls_perms))]
        steps = defaultdict(int)
        rolls = set()
        for perm in rolls_perms:
            for p in perm:
                rolls.add(p)
        for roll in rolls:
            steps[sum(roll)] += 1
        return steps

    @lru_cache(maxsize=None)
    def _play_round(self, new_state):
        positions, scores, turn = new_state
        new_positions = list(positions)
        new_scores = list(scores)
        wins = np.zeros(2)
        for step, count in self.steps.items():
            new_positions[turn] = calculate_new_position(positions[turn], step)
            new_scores[turn] = calculate_new_score(scores[turn], new_positions[turn])
            if new_scores[turn] >= self.winning_score:
                wins[turn] += count
            else:
                new_state = (tuple(new_positions), tuple(new_scores), 1 - turn)
                wins += self._play_round(new_state) * count
        return wins

    def play(self):
        number_of_wins = self._play_round(self.initial_state)
        self.number_of_games = int(sum(number_of_wins))
        self.players[0].number_of_wins = int(number_of_wins[0])
        self.players[1].number_of_wins = int(number_of_wins[1])
        self.winner = max(self.players, key=attrgetter('number_of_wins'))
        self.loser = min(self.players, key=attrgetter('number_of_wins'))

    def __str__(self):
        return f'A total of {self.number_of_games:,} games were played\n{self.players[0]}\n{self.players[1]}'

    def __repr__(self):
        return self.__str__()


def get_data(day):
    text_file = open('../data/day' + str(day) + ".txt", "r")
    input_data = text_file.read()
    text_file.close()
    return input_data


def data_prep(day):
    input_data = get_data(day)
    input_data = input_data.split('\n')
    input_data = [i.split() for i in input_data]
    starting_positions = [int(i[-1]) - 1 for i in input_data]
    return starting_positions


def part1(player1_pos, player2_pos, winning_score):
    players = [Player(1, player1_pos), Player(2, player2_pos)]
    game = DicraDiceGame(players, winning_score)
    game.play()
    # print(game)
    return game.turn * 3 * game.loser.score


def part2(player1_pos, player2_pos, winning_score, die_sides):
    players = [QuantumPlayer(1, player1_pos), QuantumPlayer(2, player2_pos)]
    quantum_game = QuantumDicraDiceGame(players, winning_score, die_sides)
    quantum_game.play()
    # print(quantum_game)
    return quantum_game.winner


def main():
    day = 21
    player1_starting_pos, player2_starting_pos = data_prep(day)

    answer1 = part1(player1_starting_pos, player2_starting_pos, 1000)
    answer2 = part2(player1_starting_pos, player2_starting_pos, 21, 3)

    print(f'Day {day} part 1 answer: {answer1}')
    print(f'Day {day} part 2 answer: {answer2}')


if __name__ == "__main__":
    main()
