package racer

import (
	"net/http"
)

func Racer(a, b string) (winner string) {
	result := make(chan string)

	go func() {
		http.Get(a)
		result <- a
	}()
	go func() {
		http.Get(b)
		result <- b
	}()

	winner = <-result

	return
}
