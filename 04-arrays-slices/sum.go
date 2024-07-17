package main

func Sum(numbers []int) int {
	sum := 0
	for _, number := range numbers {
		sum += number
	}
	return sum
}

func SumAll(numbersToSum ...[]int) []int {
	result := make([]int, len(numbersToSum))
	for i, slice := range numbersToSum {
		result[i] = Sum(slice)
	}
	return result
}

func SumAllTails(numbersToSum ...[]int) []int {
	result := make([]int, len(numbersToSum))
	for i, slice := range numbersToSum {
		if len(slice) > 1 {
			result[i] = Sum(slice[1:])
		} else {
			result[i] = Sum(slice)
		}
	}
	return result
}
