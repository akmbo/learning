package main

import "fmt"

const (
	spanish = "Spanish"
	french  = "French"

	englishHelloPrefix = "Hello, "
	spanishHelloPrefix = "Hola, "
	frenchPrefix       = "Bonjour, "
)

func Hello(name string, language string) string {
	prefix := greetingPrefix(language)

	if name == "" {
		return prefix + "World"
	}
	return prefix + name
}

func greetingPrefix(language string) (prefix string) {
	switch language {
	case spanish:
		prefix = spanishHelloPrefix
	case french:
		prefix = frenchPrefix
	default:
		prefix = englishHelloPrefix
	}
	return
}

func main() {
	fmt.Println(Hello("world", "English"))
}
