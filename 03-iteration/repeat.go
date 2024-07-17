package iteration

const repeatCount = 5

func Repeat(char string) string {
	var result string
	for i := 0; i < repeatCount; i++ {
		result += char
	}
	return result
}
