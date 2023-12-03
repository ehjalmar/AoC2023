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
				// Store completed number
				//numbers = append(numbers, Symbol{rowIndex, startIndexIfString, newNumberChars, lengthOfCurrentValue})
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

	for i := 0; i < len(DEBUG_rows); i++ {
		println(strconv.Itoa(i) + "  " + strconv.Itoa(DEBUG_rows[i]))
	}
}

func main() {
	lines := readInputData("day3.txt")

	executePart1(lines)

}
