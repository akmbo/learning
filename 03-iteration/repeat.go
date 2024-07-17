package iteration

// Repeat takes a string and int and repeats the string n times
func Repeat(char string, count int) string {
	var result string
	for i := 0; i < count; i++ {
		result += char
	}
	return result
}
