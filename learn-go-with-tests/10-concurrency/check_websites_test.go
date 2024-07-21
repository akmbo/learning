package concurrency

import (
	"maps"
	"testing"
)

func mockWebsiteChecker(url string) bool {
	return url != "waat://furhurterw.geds"
}

func TestCheckWebsites(t *testing.T) {
	websites := []string{
		"http://google.com",
		"https://blog.gypsydave5.com",
		"waat://furhurterw.geds",
	}

	want := map[string]bool{
		"http://google.com":           true,
		"https://blog.gypsydave5.com": true,
		"waat://furhurterw.geds":      false,
	}

	got := CheckWebsites(mockWebsiteChecker, websites)

	if !maps.Equal(got, want) {
		t.Fatalf("wanted %v, got %v", want, got)
	}
}
