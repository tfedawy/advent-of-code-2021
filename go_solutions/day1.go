package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	fileName := "data/day1.txt"
	input := getData(fileName)

	data := make([]int, 0, len(input))
	for _, line := range input {
		lineData, _ := strconv.Atoi(line)
		data = append(data, lineData)
	}

	larger := 0
	for i := 1; i < len(data); i++ {
		if data[i] > data[i-1] {
			larger++
		}
	}
	fmt.Println("Part 1 answer: ", larger)

	larger = 0
	currentSum := 0
	previousSum := 0
	for i := 1; i < len(data)-2; i++ {
		currentSum = 0
		previousSum = 0

		for j := 0; j < 3; j++ {
			currentSum += data[i+j]
			previousSum += data[i-1+j]
		}

		if currentSum > previousSum {
			larger++
		}
	}

	fmt.Println("Part 2 answer: ", larger)
}

func getData(f string) []string {
	file, err := os.Open(f)
	if err != nil {
		fmt.Println(err)
	}

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}
