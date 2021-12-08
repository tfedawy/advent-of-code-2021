package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Board struct {
	size         int
	grid         [][]int
	marked       [][]bool
	rowTally     []int
	columnTally  []int
	winningGuess int
	isWinner     bool
}

func NewBoard(grid [][]int) *Board {
	size := len(grid)
	marked := make([][]bool, size)
	for i := range marked {
		marked[i] = make([]bool, size)
	}
	rowTally := make([]int, size)
	columnTally := make([]int, size)
	isWinner := false
	return &Board{size: size, grid: grid, marked: marked, rowTally: rowTally, columnTally: columnTally, isWinner: isWinner}
}

func (board Board) markGuess(guess int) Board {
	for r, row := range board.grid {
		for c, val := range row {
			if val == guess {
				board.marked[r][c] = true
				board.rowTally[r]++
				board.columnTally[c]++
				if board.rowTally[r] == board.size || board.columnTally[c] == board.size {
					board.winningGuess = guess
					board.isWinner = true

				}
				return board
			}
		}
	}
	return board
}

func (board Board) score() int {
	score := 0
	for r, row := range board.marked {
		for c, val := range row {
			if !val {
				score += board.grid[r][c] * board.winningGuess
			}
		}
	}

	return score
}

func main() {

	fileName := "data/day4.txt"
	input := getData(fileName)

	guesses, inputData, err := dataPrep(input)
	if err != nil {
		fmt.Println("board or guesses have a non number value")
		return
	}

	boards := populateBoards(inputData)
	winners := play(guesses, boards)

	fmt.Println("Part 1 answer:", part1(winners))
	fmt.Println("Part 2 answer:", part2(winners))

}

func getData(f string) []string {
	file, err := os.Open(f)
	if err != nil {
		fmt.Println(err)
	}

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		l := scanner.Text()
		if strings.TrimSpace(l) != "" {
			lines = append(lines, scanner.Text())
		}
	}

	return lines
}

func dataPrep(input []string) ([]int, [][]int, error) {
	var guesses []int
	var data [][]int

	for _, n := range strings.Split(input[0], ",") {
		guessNumber, err := strconv.Atoi(n)
		if err != nil {
			return nil, nil, err
		}
		guesses = append(guesses, guessNumber)
	}

	for _, line := range input[1:] {
		s := strings.Split(line, " ")
		var numericData = make([]int, 0, 5)

		for _, n := range s {
			if strings.TrimSpace(n) != "" {
				number, _ := strconv.Atoi(n)
				numericData = append(numericData, number)
			}
		}
		data = append(data, numericData)

	}

	return guesses, data, nil
}

func populateBoards(inputData [][]int) []Board {
	boardSize := len(inputData[0])
	numberOfBoards := len(inputData) / boardSize
	boards := make([]Board, 0, numberOfBoards)
	grid := make([][]int, 0, 5)

	for i, line := range inputData {
		if i%5 == 0 && i > 0 {
			boards = append(boards, *NewBoard(grid))
			grid = make([][]int, 0, 5)
		}
		grid = append(grid, line)
	}

	return boards

}

func play(guesses []int, boards []Board) []Board {
	winners := make([]Board, 0, len(boards))
	for _, guess := range guesses {
		for j, board := range boards {
			if !board.isWinner {
				boards[j] = board.markGuess(guess)
				if boards[j].isWinner {
					winners = append(winners, boards[j])
				}
			}
		}
	}

	return winners
}

func part1(winners []Board) int {
	return winners[0].score()
}
func part2(winners []Board) int {
	return winners[len(winners)-1].score()
}
