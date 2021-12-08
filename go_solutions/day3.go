package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {

	fileName := "data/day3.txt"
	input := getData(fileName)

	var data [][]string

	for _, line := range input {
		s := strings.Split(line, "")
		data = append(data, s)
	}

	fmt.Println("Part 1 answer:", part1(data))
	fmt.Println("Part 2 answer:", part2(data))

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

func mostCommonDigit(data [][]string, index int) int {
	count := 0
	for _, n := range data {
		if n[index] == "1" {
			count++
		}
	}
	if count > len(data)/2 {
		return 1
	} else {
		return 0
	}
}

func binaryStringToDecimalInt(bin string) int {
	dec := 0
	exponent := 0
	for i, n := range bin {
		exponent = len(bin) - 1 - i
		if n == 49 {
			dec += int(math.Pow(2, float64(exponent)))
		}
	}
	return dec
}

func stringListToBinString(list []string) string {
	bin := ""
	for _, n := range list {
		if n == "1" {
			bin += n
		} else {
			bin += "0"
		}
	}
	return bin
}

func findTarget(data [][]string, moreOrLess string) [][]string {
	index := 0
	criteria := ""
	for index < 12 && len(data) > 1 {
		var newData [][]string
		if moreOrLess == "more" {
			criteria = strconv.Itoa(mostCommonDigit(data, index))
		} else {
			criteria = strconv.Itoa(1 - mostCommonDigit(data, index))
		}

		for _, n := range data {
			if n[index] == criteria {
				newData = append(newData, n)
			}
		}
		data = newData
		index++
	}
	return data
}

func part1(data [][]string) int {
	count := make([]int, 12)
	var gammaBin string
	var epsilonBin string

	for i, _ := range count {
		count[i] = mostCommonDigit(data, i)
		gammaBin += strconv.Itoa(count[i])
		epsilonBin += strconv.Itoa(1 - count[i])
	}

	powerConsumption := binaryStringToDecimalInt(gammaBin) * binaryStringToDecimalInt(epsilonBin)

	return powerConsumption
}

func part2(data [][]string) int {
	oxygenData := data
	carbonData := data

	oxygenData = findTarget(oxygenData, "more")
	oxygenBin := stringListToBinString(oxygenData[0])

	carbonData = findTarget(carbonData, "less")
	carbonBin := stringListToBinString(carbonData[0])

	return binaryStringToDecimalInt(oxygenBin) * binaryStringToDecimalInt(carbonBin)
}
