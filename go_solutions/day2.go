package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Command struct {
	Direction string
	Magnitude int
}

func main() {

	fileName := "data/day2.txt"
	input := getData(fileName)

	var data []Command
	var command Command

	for _, line := range input {
		s := strings.Split(line, " ")
		command.Direction = s[0]
		command.Magnitude, _ = strconv.Atoi(s[1])
		data = append(data, command)
	}

	horizontal := 0
	depth := 0

	for _, c := range data {
		if c.Direction == "forward" {
			horizontal += c.Magnitude
		} else if c.Direction == "down" {
			depth += c.Magnitude
		} else {
			depth -= c.Magnitude
		}
	}

	fmt.Println("Part 1 answer: ", horizontal*depth)

	horizontal = 0
	depth = 0
	aim := 0

	for _, c := range data {
		if c.Direction == "forward" {
			horizontal += c.Magnitude
			depth += aim * c.Magnitude
		} else if c.Direction == "down" {
			aim += c.Magnitude
		} else {
			aim -= c.Magnitude
		}
	}

	fmt.Println("Part 2 answer: ", horizontal*depth)
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
