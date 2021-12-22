package main

import (
	"fmt"
)

type gameState struct {
	positionOne int
	scoreOne    int
	positionTwo int
	scoreTwo    int
	turn        bool
}

func main() {

	cache := map[gameState][]int{}
	initialState := gameState{
		positionOne: 2,
		scoreOne:    0,
		positionTwo: 10,
		scoreTwo:    0,
		turn:        true,
	}
	winOne, WinTwo := QuantumGame(initialState, cache)
	fmt.Println("Part 2 answer:", winOne, WinTwo)

}

func calculateNewPosition(position int, step int) int {
	newP := position + step
	if newP%10 == 0 {
		return 10
	} else {
		return newP % 10
	}
}

func QuantumGame(state gameState, cache map[gameState][]int) (int, int) {
	steps := map[int]int{6: 7, 5: 6, 7: 6, 8: 3, 4: 3, 9: 1, 3: 1}
	var winOne int
	var winTwo int
	if state.turn {
		var newPosition int
		var newScore int
		for step, count := range steps {
			newPosition = calculateNewPosition(state.positionOne, step)
			newScore = state.scoreOne + newPosition
			if newScore >= 21 {
				winOne += count
			} else {
				newState := gameState{
					positionOne: newPosition,
					scoreOne:    newScore,
					positionTwo: state.positionTwo,
					scoreTwo:    state.scoreTwo,
					turn:        false,
				}
				if val, ok := cache[newState]; ok {
					wins := val
					winOne += wins[0] * count
					winTwo += wins[1] * count
				} else {
					wOne, wTwo := QuantumGame(newState, cache)
					winOne += wOne * count
					winTwo += wTwo * count
					cache[newState] = []int{wOne, wTwo}
				}

			}
		}
	} else {
		var newPosition int
		var newScore int
		for step, count := range steps {
			newPosition = calculateNewPosition(state.positionTwo, step)
			newScore = state.scoreTwo + newPosition
			if newScore >= 21 {
				winTwo += count
			} else {
				newState := gameState{
					positionOne: state.positionOne,
					scoreOne:    state.scoreOne,
					positionTwo: newPosition,
					scoreTwo:    newScore,
					turn:        true,
				}
				if val, ok := cache[newState]; ok {
					wins := val
					winOne += wins[0] * count
					winTwo += wins[1] * count
				} else {
					wOne, wTwo := QuantumGame(newState, cache)
					winOne += wOne * count
					winTwo += wTwo * count
					cache[newState] = []int{wOne, wTwo}
				}

			}
		}
	}
	return winOne, winTwo
}
