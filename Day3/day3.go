package main

import (
	"bufio"
	"os"
	"strconv"
)

type Symbol struct {
	Row    int
	Column int
	Value  string
	Length int
}

type Gear struct {
	Row             int
	Column          int
	Value           string
	AdjacentNumbers []int
}

func isNumeric(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}

func readInputData(path string) []string {
	file, _ := os.Open("input.txt")
	defer file.Close()

	var fileLines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fileLines = append(fileLines, scanner.Text())
	}
	return fileLines
}

func executePart1(lines []string) {
	var numbers []Symbol

	for rowIndex, line := range lines {

		startIndexIfString := -1
		newNumberChars := ""
		lengthOfCurrentValue := 0
		for i := 0; i < len(line); i++ {
			currentValue := string(line[i])

			// Found non numeric char
			if currentValue != "." && !isNumeric(currentValue) {
				numbers = append(numbers, Symbol{rowIndex, i, currentValue, 1})
				continue
			}
			// Found a numeric
			if isNumeric(currentValue) {
				lengthOfCurrentValue += 1
				// If we already started to parse a number
				if startIndexIfString > -1 {
					newNumberChars += currentValue
				} else {
					startIndexIfString = i
					newNumberChars = currentValue
				}

				// If next is not numeric or end of line, add to list
				if (i == (len(line) - 1)) || !isNumeric(string(line[i+1])) {
					numbers = append(numbers, Symbol{rowIndex, startIndexIfString, newNumberChars, lengthOfCurrentValue})
					lengthOfCurrentValue = 0
					startIndexIfString = -1
				}

			} else if startIndexIfString > -1 {
				lengthOfCurrentValue = 0
				startIndexIfString = -1
			}
		}
	}

	var validNumbers []Symbol
	// For each row, check if value has adjacents on current row, below or above
	for i := 0; i < len(numbers); i++ {
		currentValue := numbers[i]
		// print(currentValue.Value)
		if isNumeric(currentValue.Value) {
			hasAdjacent := false
			for i := 0; i < len(numbers); i++ {
				otherValue := numbers[i]
				if !isNumeric(otherValue.Value) { // Only check symbols
					if otherValue.Row == currentValue.Row { // check on same row
						if otherValue.Column == (currentValue.Column+currentValue.Length) || // ajacent to the right
							(otherValue.Column) == currentValue.Column-1 { // ajacent to the left
							hasAdjacent = true
						}
					} else if otherValue.Row == currentValue.Row-1 || otherValue.Row == currentValue.Row+1 { //check on row above and below
						if otherValue.Column < (currentValue.Column+currentValue.Length+1) &&
							otherValue.Column > currentValue.Column-2 {
							hasAdjacent = true
						}
					}
				}
				if hasAdjacent {
					validNumbers = append(validNumbers, currentValue)
					break
				}
			}

		}
	}

	DEBUG_rows := make(map[int]int)
	for i := 0; i < 140; i++ {
		DEBUG_rows[i] = 0
	}

	// Calculate total sum
	sum := 0
	for i := 0; i < len(validNumbers); i++ {

		tempValue, _ := strconv.Atoi(validNumbers[i].Value)
		sum += tempValue
		DEBUG_rows[validNumbers[i].Row] = DEBUG_rows[validNumbers[i].Row] + 1
	}
	println(strconv.Itoa(sum))

	// for i := 0; i < len(DEBUG_rows); i++ {
	// 	println(strconv.Itoa(i) + "  " + strconv.Itoa(DEBUG_rows[i]))
	// }
}

func executePart2(lines []string) {
	var numbers []Symbol
	var gears []Gear

	for rowIndex, line := range lines {

		startIndexIfString := -1
		newNumberChars := ""
		lengthOfCurrentValue := 0
		for i := 0; i < len(line); i++ {
			currentValue := string(line[i])

			// Found non numeric char
			// if currentValue != "." && !isNumeric(currentValue) {
			if currentValue == "*" {
				gears = append(gears, Gear{rowIndex, i, currentValue, make([]int, 0)})
				continue
			}
			// Found a numeric
			if isNumeric(currentValue) {
				lengthOfCurrentValue += 1
				// If we already started to parse a number
				if startIndexIfString > -1 {
					newNumberChars += currentValue
				} else {
					startIndexIfString = i
					newNumberChars = currentValue
				}

				// If next is not numeric or end of line, add to list
				if (i == (len(line) - 1)) || !isNumeric(string(line[i+1])) {
					numbers = append(numbers, Symbol{rowIndex, startIndexIfString, newNumberChars, lengthOfCurrentValue})
					lengthOfCurrentValue = 0
					startIndexIfString = -1
				}

			} else if startIndexIfString > -1 {
				lengthOfCurrentValue = 0
				startIndexIfString = -1
			}
		}
	}

	var validGears []Gear
	// For each row, check if value has adjacents on current row, below or above
	for i := 0; i < len(gears); i++ {
		currentGear := gears[i]
		numberOfAdjacents := 0

		for i := 0; i < len(numbers); i++ {
			currentValue := numbers[i]
			currentNumericValue, _ := strconv.Atoi(currentValue.Value)

			if currentValue.Row == currentGear.Row { // check on same row
				if (currentValue.Column == (currentGear.Column + 1)) || // ajacent to the right
					(currentValue.Column) == currentGear.Column-currentValue.Length { // ajacent to the left
					currentGear.AdjacentNumbers = append(currentGear.AdjacentNumbers, currentNumericValue)
					numberOfAdjacents++
				}
			} else if currentValue.Row == currentGear.Row-1 || currentValue.Row == currentGear.Row+1 { //check on row above and below
				if currentValue.Column < (currentGear.Column+2) &&
					currentValue.Column > (currentGear.Column-currentValue.Length-1) {
					currentGear.AdjacentNumbers = append(currentGear.AdjacentNumbers, currentNumericValue)
					numberOfAdjacents++
				}
			}
		}
		if numberOfAdjacents == 2 {
			validGears = append(validGears, currentGear)
		}
	}

	// Calculate total sum
	sum := 0
	for i := 0; i < len(validGears); i++ {
		currentGearRatio := (validGears[i].AdjacentNumbers[0] * validGears[i].AdjacentNumbers[1])
		sum += currentGearRatio
	}
	println(strconv.Itoa(sum))
}

func main() {
	lines := readInputData("input.txt")

	executePart1(lines)
	executePart2(lines)
}
