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
